import pytest
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_commerce_providers_can_generate():
    """Test all commerce providers can generate values."""
    commerce_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "commerce"
    ]

    failures = []
    for key_label in sorted(commerce_providers):
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="commerce")
            value = provider.generate_non_blank(row_data={})
            assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Commerce provider failures:\n" + "\n".join(failures)


def test_commerce_credit_card_provider_with_card_type():
    """Test credit card provider with specific card type."""
    provider = ProviderFactory.create(
        key_label="credit_card_number", group="commerce")
    value = provider.generate_non_blank(row_data={"credit_card_type": "Visa"})
    assert isinstance(value, str)
    assert len(value) > 0
