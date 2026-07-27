from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .core import IkiDataGenerator


class Dataset:
    """High-level dataset wrapper for schema-driven generation."""

    def __init__(self, schema: list[str | dict[str, Any]], seed: int | None = None) -> None:
        self.schema = schema
        self.seed = seed
        self._generator = IkiDataGenerator(schema, seed=seed)

    @classmethod
    def from_schema(
        cls,
        schema: list[str | dict[str, Any]],
        seed: int | None = None,
    ) -> "Dataset":
        return cls(schema=schema, seed=seed)

    def generate(self, n: int) -> list[dict[str, Any]]:
        self._generator.many(n)
        return self._generator.data

    def export_recipe(self, output_path: str | Path) -> dict[str, Any]:
        recipe = {
            "schema": self.schema,
            "seed": self.seed,
        }
        path = Path(output_path)
        path.write_text(json.dumps(recipe, indent=2), encoding="utf-8")
        return recipe
