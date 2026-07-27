from __future__ import annotations

from dataclasses import is_dataclass, fields
from typing import Any

import pandas as pd


class SchemaBuilder:
    """Convenience builder for creating schema definitions programmatically."""

    def __init__(self) -> None:
        self._fields: list[dict[str, Any]] = []

    def add_field(
        self,
        key_label: str,
        *,
        label: str | None = None,
        group: str | None = None,
        options: dict[str, Any] | None = None,
    ) -> "SchemaBuilder":
        self._fields.append(
            {
                "key_label": key_label,
                "label": label or key_label,
                "group": group,
                "options": options or {},
            }
        )
        return self

    def build(self) -> list[dict[str, Any]]:
        return list(self._fields)

    @classmethod
    def from_dataframe(cls, data: pd.DataFrame | Any) -> list[dict[str, Any]]:
        builder = cls()
        for column in data.columns:
            raw_name = str(column)
            if raw_name.lower() == "email":
                key_label = "email_address"
            elif raw_name.lower() == "age":
                key_label = "age"
            else:
                key_label = raw_name.replace(" ", "_").lower()
            builder.add_field(key_label, label=raw_name)
        return builder.build()

    @classmethod
    def from_dataclass(cls, model: type[Any]) -> list[dict[str, Any]]:
        if not is_dataclass(model):
            raise TypeError(
                "SchemaBuilder.from_dataclass expects a dataclass type")
        builder = cls()
        for field in fields(model):
            builder.add_field(field.name, label=field.name)
        return builder.build()
