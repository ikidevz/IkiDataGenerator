import pytest
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_health_providers_can_generate():
    """Test all health/medical providers can generate values."""
    health_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "health"
    ]

    failures = []
    for key_label in sorted(health_providers):
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="health")
            value = provider.generate_non_blank(row_data={})
            assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Health provider failures:\n" + "\n".join(failures)
