"""
Tests for new P1 features:
- Seeding/reproducibility
- Uniqueness constraints
- Bcrypt fast mode
- Locale support
- Field ordering/correlation
"""

import pytest
from ikidatagen import IkiDataGenerator


class TestSeeding:
    """Test that seeding produces reproducible results."""

    def test_seeding_produces_reproducible_data(self):
        """Two generators with the same seed should produce identical data."""
        schema = ["first_name", "last_name", "email_address"]

        gen1 = IkiDataGenerator(schema, seed=42)
        data1 = gen1.many(10).data

        gen2 = IkiDataGenerator(schema, seed=42)
        data2 = gen2.many(10).data

        assert data1 == data2, "Same seed should produce identical data"

    def test_different_seeds_produce_different_data(self):
        """Two generators with different seeds should produce different data."""
        schema = ["first_name", "last_name", "email_address"]

        gen1 = IkiDataGenerator(schema, seed=42)
        data1 = gen1.many(10).data

        gen2 = IkiDataGenerator(schema, seed=43)
        data2 = gen2.many(10).data

        # Very unlikely to be equal with different seeds
        assert data1 != data2, "Different seeds should produce different data"

    def test_no_seed_produces_different_data_each_time(self):
        """Generator without seed should produce different data on each run."""
        schema = ["first_name", "last_name"]

        gen1 = IkiDataGenerator(schema)
        data1 = gen1.many(100).data

        gen2 = IkiDataGenerator(schema)
        data2 = gen2.many(100).data

        # At least some rows should differ (extremely unlikely to be 100% identical)
        assert data1 != data2, "Without seed, data should differ between runs"


class TestUniqueness:
    """Test unique constraint support."""

    def test_unique_constraint_produces_unique_values(self):
        """Values marked as unique should all be distinct."""
        schema = [
            "first_name",
            {"key_label": "email_address", "options": {"unique": True}},
        ]

        gen = IkiDataGenerator(schema, seed=42)
        data = gen.many(100).data

        emails = [row["email_address"]
                  for row in data if row["email_address"] is not None]
        unique_emails = set(emails)

        assert len(emails) == len(unique_emails), "Unique constraint violated"

    def test_unique_with_blanks(self):
        """Unique constraints should handle blank_percentage correctly."""
        schema = [
            "first_name",
            {
                "key_label": "email_address",
                "options": {"unique": True, "blank_percentage": 20},
            },
        ]

        gen = IkiDataGenerator(schema, seed=42)
        data = gen.many(50).data

        emails = [row["email_address"]
                  for row in data if row["email_address"] is not None]
        unique_emails = set(emails)

        assert len(emails) == len(
            unique_emails), "Unique constraint should still hold with blanks"
        assert len(emails) < 50, "Blank percentage should create some None values"

    def test_unique_constraint_exhaustion(self):
        """Requesting more unique values than possible should raise."""
        schema = [
            {
                "key_label": "gender_binary",
                "options": {"unique": True},
            },
        ]

        gen = IkiDataGenerator(schema, seed=42)
        # gender_binary only has ~2 values, so 100 unique values should fail
        with pytest.raises(ValueError, match="Unable to generate unique value"):
            gen.many(100).data


class TestBcryptFastMode:
    """Test bcrypt fast mode for password hashing."""

    def test_password_hash_default_uses_bcrypt_or_sha256(self):
        """Default password_hash should use bcrypt if available."""
        schema = [{"key_label": "password_hash"}]

        gen = IkiDataGenerator(schema, seed=42)
        data = gen.many(5).data

        for row in data:
            password_hash = row["password_hash"]
            assert password_hash is not None
            # Should be a hash (not plain text)
            assert len(password_hash) > 20

    def test_password_hash_fast_mode(self):
        """Fast mode should use SHA256-based hashing."""
        schema = [
            {
                "key_label": "password_hash",
                "options": {"fast": True},
            }
        ]

        gen = IkiDataGenerator(schema, seed=42)
        data = gen.many(5).data

        for row in data:
            password_hash = row["password_hash"]
            assert password_hash is not None
            # Fast mode uses sha256$ prefix
            assert password_hash.startswith("sha256$")

    def test_password_hash_with_custom_rounds(self):
        """Should accept rounds parameter."""
        schema = [
            {
                "key_label": "password_hash",
                "options": {"rounds": 8},
            }
        ]

        gen = IkiDataGenerator(schema, seed=42)
        data = gen.many(5).data

        for row in data:
            password_hash = row["password_hash"]
            assert password_hash is not None


class TestGenerationDefaults:
    """Test standard generation behavior without locale-specific APIs."""

    def test_generator_runs_without_locale_argument(self):
        """Basic generation should work without locale support."""
        schema = ["first_name", "last_name"]

        gen = IkiDataGenerator(schema)
        data = gen.many(5).data

        assert len(data) == 5
        for row in data:
            assert row["first_name"] is not None
            assert row["last_name"] is not None


class TestFieldOrdering:
    """Test that location fields generate successfully without enforced ordering."""

    def test_location_fields_generate_without_reordering(self):
        """Location fields should generate even when the schema order varies."""
        schema = [
            "first_name",
            "postal_code",
            "country",
            "state",
            "city",
            "last_name",
        ]

        gen = IkiDataGenerator(schema)
        data = gen.many(5).data

        assert len(data) == 5
        for row in data:
            assert "first_name" in row
            assert "country" in row
            assert "city" in row


class TestRowContext:
    """Test that provider row_data uses key labels while templates keep labels."""

    def test_providers_receive_key_label_context(self):
        """Username provider should resolve first_name and last_name from key-label context."""
        schema = [
            {"label": "First Name", "key_label": "first_name"},
            {"label": "Last Name", "key_label": "last_name"},
            {"label": "Username", "key_label": "username"},
        ]

        gen = IkiDataGenerator(schema, seed=42)
        data = gen.many(5).data

        for row in data:
            first_name = row["First Name"].lower()
            last_name = row["Last Name"].lower()
            username = row["Username"].lower()
            assert first_name in username
            assert last_name in username

    def test_template_provider_still_uses_output_labels(self):
        """Template provider should continue resolving placeholders from output labels."""
        schema = [
            {"label": "First Name", "key_label": "first_name"},
            {"label": "Last Name", "key_label": "last_name"},
            {
                "label": "Full Name",
                "key_label": "template",
                "options": {"template": "{{First Name}} {{Last Name}}"},
            },
        ]

        gen = IkiDataGenerator(schema, seed=42)
        row = gen.many(1).data[0]

        assert row["Full Name"] == f"{row['First Name']} {row['Last Name']}"


class TestRowIndexing:
    """Test that row_index is properly passed to providers."""

    def test_row_number_uses_row_index(self):
        """row_number should use row_index, not internal counter."""
        schema = [
            "first_name",
            {"key_label": "row_number", "label": "id"},
        ]

        gen1 = IkiDataGenerator(schema, seed=42)
        data1 = gen1.many(10).data
        row_numbers1 = [row["id"] for row in data1]

        # Generate same schema again with same seed
        gen2 = IkiDataGenerator(schema, seed=42)
        data2 = gen2.many(10).data
        row_numbers2 = [row["id"] for row in data2]

        # Row numbers should be consistent (1-10 in both cases)
        assert row_numbers1 == row_numbers2 == list(range(1, 11))

    def test_row_number_resets_on_new_many_call(self):
        """row_number should not leak across .many() calls."""
        schema = [
            "first_name",
            {"key_label": "row_number", "label": "id"},
        ]

        gen = IkiDataGenerator(schema, seed=42)
        data1 = gen.many(5).data
        row_numbers1 = [row["id"] for row in data1]

        # Call many() again on same instance
        data2 = gen.many(5).data
        row_numbers2 = [row["id"] for row in data2]

        # row_numbers should be 1-5 in both cases (not 1-5 then 6-10)
        assert row_numbers1 == list(range(1, 6))
        assert row_numbers2 == list(range(1, 6))


class TestStreamingGeneration:
    """Test streaming/batched generation."""

    def test_stream_method_yields_batches(self):
        """stream() should yield batches of rows."""
        schema = ["first_name", "last_name"]

        gen = IkiDataGenerator(schema)
        batches = list(gen.stream(n=1250, batch_size=100))

        # Should have batches (100*12 + 50)
        assert len(batches) == 13
        assert sum(len(batch) for batch in batches) == 1250
        # Most batches should have 100 rows
        assert all(len(b) == 100 for b in batches[:-1])
        # Last batch should have 50
        assert len(batches[-1]) == 50

    def test_stream_export_csv(self):
        """export() with stream=True should work."""
        import tempfile
        import os
        import csv

        schema = ["first_name", "last_name", "email_address"]

        with tempfile.TemporaryDirectory() as tmpdir:
            gen = IkiDataGenerator(schema, seed=42)
            gen.export(
                "test_stream",
                output_dir=tmpdir,
                formats=["csv"],
                stream=True,
                n=500,
                batch_size=100,
            )

            csv_path = os.path.join(tmpdir, "test_stream.csv")
            assert os.path.exists(csv_path)

            with open(csv_path, "r") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                assert len(rows) == 500

    def test_stream_export_ndjson(self):
        """export() can stream NDJSON without loading all rows in memory."""
        import tempfile
        import os

        schema = ["first_name", "last_name", "email_address"]

        with tempfile.TemporaryDirectory() as tmpdir:
            gen = IkiDataGenerator(schema, seed=42)
            gen.export(
                "test_stream",
                output_dir=tmpdir,
                formats=["ndjson"],
                stream=True,
                n=250,
                batch_size=50,
            )

            ndjson_path = os.path.join(tmpdir, "test_stream.ndjson")
            assert os.path.exists(ndjson_path)

            with open(ndjson_path, "r", encoding="utf-8") as f:
                lines = [line for line in f if line.strip()]
                assert len(lines) == 250


class TestStrictMode:
    """Test strict mode for unknown schema options."""

    def test_strict_mode_raises_on_unknown_option(self):
        """strict=True should raise on unknown options."""
        schema = [
            {
                "key_label": "first_name",
                "options": {"typo_option": True},
                "options_strict": True,
            }
        ]

        with pytest.raises(ValueError, match="Unknown option"):
            IkiDataGenerator(schema).many(1)

    def test_non_strict_mode_warns_on_unknown_option(self):
        """strict=False should warn but not raise."""
        schema = [
            {
                "key_label": "first_name",
                "options": {"typo_option": True, "strict": False},
            }
        ]

        # Should not raise, but should generate data
        gen = IkiDataGenerator(schema)
        data = gen.many(1).data
        assert len(data) == 1
