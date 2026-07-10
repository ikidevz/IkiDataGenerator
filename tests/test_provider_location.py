import pytest
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_location_providers_can_generate():
    """Test all location providers can generate values."""
    location_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "location"
    ]

    failures = []
    for key_label in sorted(location_providers):
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="location")
            value = provider.generate_non_blank(row_data={})
            assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Location provider failures:\n" + "\n".join(failures)


def test_location_providers_with_country_context():
    """Test location providers with country context."""
    providers_to_test = [
        ("state_abbrev", {"country": "United States"}),
        ("time_zone", {"country": "United Kingdom"}),
        ("phone", {"country": "Japan"}),
    ]

    for key_label, row_data in providers_to_test:
        provider = ProviderFactory.create(
            key_label=key_label, group="location")
        value = provider.generate_non_blank(row_data=row_data)
        assert value is not None
