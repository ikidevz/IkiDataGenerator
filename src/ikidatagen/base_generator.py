from __future__ import annotations

import random
from typing import Any

from .provider_factory import ProviderFactory


_LABEL_KEYED_PROVIDERS = {"TemplateProvider", "LambdaProvider"}


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

    def __init__(self, schema: list[str | dict[str, Any]]):
        self.schema = [_normalize_entry(e) for e in schema]
        self.providers = self._initialize_providers()

    def generate_many(self, n: int) -> list[dict]:
        """Generate n records.  Returns a list of dicts keyed by output label."""
        rows = [{} for _ in range(n)]

        for col_key, data in self.providers.items():
            label = data["label"]
            provider = data["provider"]

            pct = (getattr(provider, "blank_percentage", 0.0) or 0.0) / 100
            num_blanks = round(n * pct)
            blank_set = set(random.sample(range(n), num_blanks)
                            ) if num_blanks > 0 else set()

            for i in range(n):
                if i in blank_set:
                    rows[i][label] = None
                    continue

                value = provider.generate_non_blank(row_data=rows[i])
                rows[i][label] = value

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
            if class_name in _LABEL_KEYED_PROVIDERS:
                options["schema_labels"] = schema_labels

            provider_instance = ProviderFactory.create(
                key_label=key_label,
                group=group,
                **options,
            )

            providers[label] = {
                "provider":  provider_instance,
                "label":     label,
                "key_label": key_label,
            }

        return providers
