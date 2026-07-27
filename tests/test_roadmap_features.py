import asyncio
from dataclasses import dataclass

import pandas as pd
import pytest

from ikidatagen import Dataset, IkiDataGenerator, SchemaBuilder


def test_schema_builder_builds_schema_and_dataset():
    builder = SchemaBuilder()
    builder.add_field("first_name")
    builder.add_field("email_address", label="email", options={"mask": True})

    schema = builder.build()
    assert schema[0]["key_label"] == "first_name"
    assert schema[1]["label"] == "email"

    dataset = Dataset.from_schema(schema, seed=7)
    rows = dataset.generate(3)
    assert len(rows) == 3
    assert all("email" in row for row in rows)


def test_weighted_choices_option_supports_per_field_sampling():
    schema = [
        {
            "key_label": "custom_list",
            "options": {
                "choices": ["alpha", "beta", "gamma"],
                "weights": [1, 1, 20],
            },
        }
    ]

    gen = IkiDataGenerator(schema, seed=42)
    data = gen.many(50).data
    values = [row["custom_list"] for row in data]

    assert "gamma" in values
    assert values.count("gamma") > 20


def test_masking_option_redacts_generated_values():
    schema = [{"key_label": "first_name", "options": {"mask": True}}]

    gen = IkiDataGenerator(schema, seed=1)
    row = gen.one()

    assert row["first_name"] == "[REDACTED]"


def test_dirty_option_injects_noise_into_strings():
    schema = [{"key_label": "custom_list", "options": {
        "choices": ["hello"], "noise": True}}]

    gen = IkiDataGenerator(schema, seed=8)
    row = gen.one()

    assert isinstance(row["custom_list"], str)
    assert row["custom_list"] != "hello"


def test_generate_event_stream_adds_timestamps_and_sequences():
    schema = ["first_name"]
    gen = IkiDataGenerator(schema, seed=3)

    rows = gen.generate_event_stream(
        3,
        start_time="2024-01-01T00:00:00",
        step_seconds=60,
        timestamp_field="event_timestamp",
    )

    assert len(rows) == 3
    assert [row["event_sequence"] for row in rows] == [1, 2, 3]
    assert rows[0]["event_timestamp"].startswith("2024-01-01T00:00:00")


def test_async_generation_returns_rows():
    gen = IkiDataGenerator(["first_name"], seed=9)
    rows = asyncio.run(gen.many_async(3))

    assert len(rows) == 3
    assert all("first_name" in row for row in rows)


def test_schema_builder_infers_from_dataframe_and_dataclass():
    df = pd.DataFrame({"email": ["user@example.com"], "age": [30]})
    schema = SchemaBuilder.from_dataframe(df)
    assert schema[0]["key_label"] == "email_address"
    assert schema[1]["key_label"] == "age"

    @dataclass
    class User:
        name: str
        email: str

    schema_from_dc = SchemaBuilder.from_dataclass(User)
    assert schema_from_dc[0]["label"] == "name"
    assert schema_from_dc[1]["label"] == "email"


def test_dataset_recipe_export_writes_manifest(tmp_path):
    dataset = Dataset.from_schema([{"key_label": "first_name"}], seed=5)
    output_path = tmp_path / "recipe.json"

    recipe = dataset.export_recipe(output_path)

    assert recipe["schema"][0]["key_label"] == "first_name"
    assert output_path.exists()
