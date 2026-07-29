import importlib
import difflib
import warnings

from .schema_registry import (
    KEY_LABEL_REGISTRY,
    resolve_key_label,
)


class ProviderFactory:
    _cache: dict = {}
    _files_map: dict | None = None

    @staticmethod
    def resolve_group(key_label: str, group: str | None) -> str:
        """
        Return the provider group for a key_label.

        Priority:
          1. Explicit group passed by the user — always wins.
          2. Registry lookup from KEY_LABEL_REGISTRY.
          3. Raise a helpful SchemaError with a fuzzy "did you mean?" suggestion.
        """
        if group:
            return group.lower()

        normalized = key_label.lower()
        canonical_key_label = resolve_key_label(normalized)
        if canonical_key_label != normalized:
            warnings.warn(
                f"[Schema Deprecation] '{key_label}' is deprecated and will be treated as '{canonical_key_label}'. "
                f"Update your schema to use the canonical key_label.",
                DeprecationWarning,
                stacklevel=3,
            )
            key_label = canonical_key_label

        resolved = KEY_LABEL_REGISTRY.get(key_label)
        if resolved:
            # Quick duplicate-file check: warn if same basename exists in multiple groups
            try:
                if ProviderFactory._files_map is None:
                    # build once
                    from pathlib import Path
                    pkg_root = Path(__file__).resolve().parent
                    providers_root = pkg_root / "providers"
                    files_map: dict[str, list[str]] = {}
                    if providers_root.exists():
                        for p in providers_root.rglob('*.py'):
                            name = p.name
                            group = p.parent.name
                            files_map.setdefault(name, []).append(group)
                    ProviderFactory._files_map = files_map
                dup_groups = ProviderFactory._files_map.get(
                    f"{key_label}.py", [])
                if len(dup_groups) > 1 and resolved not in dup_groups:
                    # if registry resolves to a group but the file exists elsewhere, warn
                    warnings.warn(
                        f"Provider key_label '{key_label}' exists in multiple groups: {', '.join(dup_groups)}. "
                        f"Registry chooses '{resolved}'. Use explicit 'group' to disambiguate.",
                        UserWarning,
                    )
                elif len(dup_groups) > 1:
                    warnings.warn(
                        f"Provider key_label '{key_label}' exists in multiple groups: {', '.join(dup_groups)}. "
                        f"Registry maps it to '{resolved}'. Use explicit 'group' to disambiguate if needed.",
                        UserWarning,
                    )
            except Exception:
                # non-fatal — discovery is best-effort
                ProviderFactory._files_map = ProviderFactory._files_map or {}
            return resolved
        close = difflib.get_close_matches(
            key_label, KEY_LABEL_REGISTRY.keys(), n=3, cutoff=0.6)
        hint = f" Did you mean: {', '.join(close)}?" if close else ""
        raise ValueError(
            f"[Schema Error] Unknown key_label '{key_label}'."
            f"{hint}\n"
            f"  → Either fix the typo, or pass 'group' explicitly if this is a custom provider."
        )

    @staticmethod
    def create(key_label: str, group: str | None = None, **kwargs):
        """
        Dynamically load and instantiate a provider class.

        Module path : providers/{group}/{key_label}.py
        Class name  : {KeyLabelPascalCase}Provider

        group is optional — it will be auto-resolved from the registry when omitted.
        """
        normalized = key_label.lower()
        canonical_key_label = resolve_key_label(normalized)
        if canonical_key_label != normalized:
            warnings.warn(
                f"[Schema Deprecation] '{key_label}' is deprecated and will be treated as '{canonical_key_label}'. "
                f"Update your schema to use the canonical key_label.",
                DeprecationWarning,
                stacklevel=3,
            )
            key_label = canonical_key_label
            normalized = canonical_key_label

        resolved_group = ProviderFactory.resolve_group(key_label, group)
        import_group = (group or resolved_group).lower()

        module_path = f"{__package__}.providers.{import_group}.{normalized}"
        class_name = "".join(word.capitalize()
                             for word in key_label.split("_")) + "Provider"
        cache_key = (import_group, normalized)

        try:
            if cache_key in ProviderFactory._cache:
                provider_class = ProviderFactory._cache[cache_key]
            else:
                module = importlib.import_module(module_path)
                provider_class = getattr(module, class_name)
                ProviderFactory._cache[cache_key] = provider_class

            # Only pass kwargs that the provider's __init__ supports.
            try:
                import inspect

                sig = inspect.signature(provider_class.__init__)
                params = sig.parameters
                accepts_kwargs = any(
                    p.kind == inspect.Parameter.VAR_KEYWORD for p in params.values()
                )
                if not accepts_kwargs:
                    filtered = {k: v for k, v in kwargs.items() if k in params}
                else:
                    filtered = kwargs
            except Exception:
                filtered = kwargs

            return provider_class(**filtered)

        except ModuleNotFoundError as e:
            # Differentiate between the provider module itself being missing
            # and the provider module raising ModuleNotFoundError for a nested import
            missing_mod = getattr(e, "name", None)
            if (
                missing_mod == module_path
                or (missing_mod and missing_mod.startswith(module_path + "."))
                or (missing_mod and module_path.startswith(missing_mod + "."))
            ):
                raise ValueError(
                    f"[Schema Error] Provider module not found for key_label='{key_label}', group='{resolved_group}'.\n"
                    f"  → Expected module at: {module_path}.py\n"
                    f"  → If this is a custom provider, make sure the file and class exist."
                ) from e
            # Otherwise the provider file exists but it imported a missing dependency.
            raise ValueError(
                f"[Schema Error] Provider '{module_path}' failed to import: missing dependency '{missing_mod}'.\n"
                f"  → This usually means a third-party package is not installed. Install the package or fix the provider's imports.\n"
                f"  → Original error: {e}"
            ) from e
        except AttributeError:
            raise ValueError(
                f"[Schema Error] Provider class '{class_name}' not found inside module '{module_path}'.\n"
                f"  → Check that the class is named exactly '{class_name}'."
            )
