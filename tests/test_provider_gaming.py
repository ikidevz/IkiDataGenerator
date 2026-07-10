import pytest
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_gaming_providers_can_generate():
    """Test all gaming/entertainment providers can generate values."""
    gaming_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "gaming"
    ]

    failures = []
    for key_label in sorted(gaming_providers):
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="gaming")
            value = provider.generate_non_blank(row_data={})
            assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Gaming provider failures:\n" + "\n".join(failures)
