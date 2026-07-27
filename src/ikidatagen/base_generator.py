from __future__ import annotations

import random
from typing import Any

from .provider_factory import ProviderFactory


def _normalize_entry(entry: str | dict[str, Any]) -> dict[str, Any]:
    """
    Accept the two supported schema entry shapes and return a canonical dict.

    Shape 1 — plain string shorthand:
        "first_name"
        → {"key_label": "first_name", "label": "first_name", "group": None, "options": {}}

    Shape 2 — full dict (all keys except key_label are optional):
        {
            "key_label": "salary_range",
            "label":     "Salary Range",   # optional — renames the output column
            "group":     "personal",        # optional — auto-resolved when omitted
            "options":   {"blank_percentage": 10},  # optional
        }
    """
    if isinstance(entry, str):
        return {
            "key_label": entry,
            "label":     entry,
            "group":     None,
            "options":   {},
        }

    if not isinstance(entry, dict):
        raise TypeError(
            f"[Schema Error] Each schema entry must be a string or dict, got {type(entry).__name__!r}."
        )

    key_label = entry.get("key_label")
    if not key_label:
        raise ValueError(
            f"[Schema Error] Every schema dict must include 'key_label'. Got: {entry}"
        )

    # label is optional — defaults to key_label when omitted
    label = entry.get("label") or key_label

    return {
        "key_label": key_label,
        "label":     label,
        "group":     entry.get("group"),
        "options":   entry.get("options", {}),
    }


class BaseGenerator:
    """
    Core data generator.  Accepts a mixed schema of strings and dicts.

    Examples
    --------
    Minimal (strings only):
        schema = ["first_name", "last_name", "email_address"]

    Mixed (string + dict for options or custom label):
        schema = [
            "first_name",
            "last_name",
            {"key_label": "salary_range", "label": "Salary", "options": {"blank_percentage": 10}},
            {"key_label": "template", "options": {"template": "{{first_name}} {{last_name}}"}},
        ]

    Full dict (old style, still works — group is now optional):
        schema = [
            {"label": "ID", "key_label": "row_number", "options": {"blank_percentage": 10}},
        ]
    """

    def __init__(
        self,
        schema: list[str | dict[str, Any]],
        seed: int | None = None,
    ):
        raw = [_normalize_entry(e) for e in schema]
        self.schema = raw
        import random as _random
        self._rng = _random.Random(seed)
        self.providers = self._initialize_providers()

    def _reorder_correlated_groups(self, entries: list[dict]) -> list[dict]:
        return entries

    def _call_provider(self, gen, row, idx):
        import inspect

        try:
            sig = inspect.signature(gen)
            params = sig.parameters
            kwargs_call = {}
            if 'row_data' in params:
                kwargs_call['row_data'] = row
            if 'row_index' in params:
                kwargs_call['row_index'] = idx
            return gen(**kwargs_call)
        except Exception:
            try:
                return gen(row, idx)
            except TypeError:
                try:
                    return gen(row)
                except TypeError:
                    return gen()

    def _apply_constraints(self, value, constraints):
        if not isinstance(constraints, dict):
            return value

        if "min_length" in constraints and isinstance(value, str) and len(value) < constraints["min_length"]:
            value = value + ("x" * (constraints["min_length"] - len(value)))
        if "max_length" in constraints and isinstance(value, str) and len(value) > constraints["max_length"]:
            value = value[:constraints["max_length"]]
        if "min_value" in constraints and isinstance(value, (int, float)) and value < constraints["min_value"]:
            value = constraints["min_value"]
        if "max_value" in constraints and isinstance(value, (int, float)) and value > constraints["max_value"]:
            value = constraints["max_value"]
        if "allowed_values" in constraints and value not in constraints["allowed_values"]:
            value = constraints["allowed_values"][0]
        return value

    def _apply_noise(self, value):
        if not isinstance(value, str) or not value:
            return value
        if len(value) <= 1:
            return value + "!"
        idx = self._rng.randrange(len(value))
        op = self._rng.choice(["swap", "repeat", "drop", "insert"])
        if op == "swap" and len(value) > 1:
            chars = list(value)
            j = (idx + 1) % len(chars)
            chars[idx], chars[j] = chars[j], chars[idx]
            return "".join(chars)
        if op == "repeat":
            return value[:idx] + value[idx] + value[idx:]
        if op == "drop":
            return value[:idx] + value[idx + 1:]
        return value[:idx] + self._rng.choice("abcdefghijklmnopqrstuvwxyz") + value[idx:]

    def _resolve_value(self, provider, row, idx, options):
        choices = options.get("choices")
        if choices:
            weights = options.get("weights")
            if weights is None:
                value = self._rng.choice(list(choices))
            else:
                if len(weights) != len(choices):
                    raise ValueError(
                        "[Schema Error] 'weights' must match the length of 'choices'.")
                value = self._rng.choices(
                    list(choices), weights=weights, k=1)[0]
        else:
            value = self._call_provider(provider.generate_non_blank, row, idx)

        if value is None:
            return None
        if options.get("mask"):
            return "[REDACTED]"
        if options.get("noise"):
            value = self._apply_noise(value)
        return self._apply_constraints(value, options.get("constraints", {}))

    def generate_many(self, n: int) -> list[dict]:
        """Generate n records.  Returns a list of dicts keyed by output label."""
        rows = [{} for _ in range(n)]

        for col_key, data in self.providers.items():
            label = data["label"]
            provider = data["provider"]
            options = data.get("options", {})

            pct = (getattr(provider, "blank_percentage", 0.0) or 0.0) / 100
            if not 0 <= pct <= 1:
                raise ValueError(
                    f"[Schema Error] Invalid blank_percentage for label '{label}': {pct*100}. "
                    "Must be between 0 and 100."
                )
            num_blanks = round(n * pct)
            blank_set = set(self._rng.sample(range(n), num_blanks)
                            ) if num_blanks > 0 else set()

            unique = bool(options.get("unique"))
            max_tries = int(options.get("max_unique_tries", 1000))
            seen = set() if unique else None

            for i in range(n):
                if i in blank_set:
                    rows[i][label] = None
                    continue

                if not unique:
                    value = self._resolve_value(provider, rows[i], i, options)
                    rows[i][label] = value
                    continue

                val = None
                for attempt in range(max_tries):
                    candidate = self._resolve_value(
                        provider, rows[i], i, options)
                    if candidate is None:
                        val = None
                        break
                    if candidate not in seen:
                        val = candidate
                        seen.add(candidate)
                        break
                if val is None:
                    raise ValueError(
                        f"[Schema Error] Unable to generate unique value for '{label}' after {max_tries} tries."
                    )
                rows[i][label] = val

        return rows

    def _initialize_providers(self) -> dict:
        providers: dict[str, dict] = {}
        schema_labels = [col["label"] for col in self.schema]

        for col in self.schema:
            label = col["label"]
            key_label = col["key_label"]
            group = col["group"]
            options = dict(col["options"])
            class_name = "".join(word.capitalize()
                                 for word in key_label.split("_")) + "Provider"
            if class_name == "TemplateProvider":
                options["schema_labels"] = schema_labels

            provider_options = dict(options)
            for key in ("unique", "max_unique_tries", "choices", "weights", "mask", "noise", "constraints"):
                provider_options.pop(key, None)

            provider_instance = ProviderFactory.create(
                key_label=key_label,
                group=group,
                rng=self._rng,
                **provider_options,
            )

            if label in providers:
                raise ValueError(
                    f"[Schema Error] Duplicate output label '{label}' in schema. "
                    "Each output column label must be unique."
                )

            providers[label] = {
                "provider":  provider_instance,
                "label":     label,
                "key_label": key_label,
                "options":   options,
            }

        # Collision detection: label must not equal another entry's key_label
        labels = set(providers.keys())
        key_labels = {v["key_label"] for v in providers.values()}
        for lab in labels:
            if lab in key_labels and providers[lab]["key_label"] != lab:
                raise ValueError(
                    f"[Schema Error] Output label '{lab}' collides with a provider key_label. "
                    "Rename the label or the key_label to avoid collisions."
                )

        return providers

    def stream(self, n: int, batch_size: int = 1000):
        """Generate rows as a stream yielding lists of dicts of at most batch_size."""
        import inspect

        def _call_provider(gen, row, idx):
            try:
                sig = inspect.signature(gen)
                params = sig.parameters
                kwargs_call = {}
                if 'row_data' in params:
                    kwargs_call['row_data'] = row
                if 'row_index' in params:
                    kwargs_call['row_index'] = idx
                return gen(**kwargs_call)
            except Exception:
                try:
                    return gen(row, idx)
                except TypeError:
                    try:
                        return gen(row)
                    except TypeError:
                        return gen()

        batch: list[dict] = []
        for i in range(n):
            row = {}
            for col_key, data in self.providers.items():
                label = data["label"]
                provider = data["provider"]
                options = data.get("options", {})
                pct = (getattr(provider, "blank_percentage", 0.0) or 0.0) / 100
                if self._rng.random() < pct:
                    row[label] = None
                    continue
                row[label] = self._resolve_value(provider, row, i, options)
            batch.append(row)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch
