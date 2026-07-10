import pytest
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_basic_providers_can_generate():
    """Test all basic data providers can generate values."""
    basic_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "basic"
    ]

    failures = []
    required_options = {
        "custom_list": {"values": ["option1", "option2"]},
    }
    # Providers that can return None or blank values are expected
    blank_allowed = {"blank"}

    for key_label in sorted(basic_providers):
        options = required_options.get(key_label, {})
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="basic", **options)
            value = provider.generate_non_blank(row_data={})
            # Some providers like 'blank' intentionally return empty/None
            if key_label not in blank_allowed:
                assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Basic provider failures:\n" + "\n".join(failures)
