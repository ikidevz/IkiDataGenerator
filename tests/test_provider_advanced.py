import pytest
import json
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_advanced_providers_can_generate():
    """Test all advanced providers can generate values."""
    advanced_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "advanced"
    ]

    failures = []
    required_options = {
        "custom_list": {"values": ["alpha", "beta"]},
        "lambda": {"func": lambda row_data=None: "ok"},
        "template": {"template": "Test: {{value}}"},
    }

    for key_label in sorted(advanced_providers):
        options = required_options.get(key_label, {})
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="advanced", **options)
            value = provider.generate_non_blank(row_data={"value": "data"})
            assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Advanced provider failures:\n" + "\n".join(failures)


def test_json_array_provider():
    """Test JSON array provider generates valid JSON."""
    provider = ProviderFactory.create(
        key_label="json_array", group="advanced", min_elements=1, max_elements=3)
    value = provider.generate_non_blank(row_data={})
    parsed = json.loads(value)
    assert isinstance(parsed, list)


def test_template_provider():
    """Test template provider with placeholders."""
    provider = ProviderFactory.create(
        key_label="template", group="advanced", template="User: {{first_name}}")
    value = provider.generate_non_blank(row_data={"first_name": "John"})
    assert "User:" in value
    assert "John" in value
