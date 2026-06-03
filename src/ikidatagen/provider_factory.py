import importlib
import difflib

from .schema_registry import KEY_LABEL_REGISTRY


class ProviderFactory:
    _cache: dict = {}

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

        resolved = KEY_LABEL_REGISTRY.get(key_label)
        if resolved:
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
        resolved_group = ProviderFactory.resolve_group(key_label, group)

        module_path = f"synthetic_data_crafter.providers.{resolved_group}.{key_label.lower()}"
        class_name = "".join(word.capitalize()
                             for word in key_label.split("_")) + "Provider"
        cache_key = (resolved_group, key_label)

        try:
            if cache_key in ProviderFactory._cache:
                provider_class = ProviderFactory._cache[cache_key]
            else:
                module = importlib.import_module(module_path)
                provider_class = getattr(module, class_name)
                ProviderFactory._cache[cache_key] = provider_class

            return provider_class(**kwargs)

        except ModuleNotFoundError:
            raise ValueError(
                f"[Schema Error] Provider module not found for key_label='{key_label}', group='{resolved_group}'.\n"
                f"  → Expected module at: {module_path}.py\n"
                f"  → If this is a custom provider, make sure the file and class exist."
            )
        except AttributeError:
            raise ValueError(
                f"[Schema Error] Provider class '{class_name}' not found inside module '{module_path}'.\n"
                f"  → Check that the class is named exactly '{class_name}'."
            )
