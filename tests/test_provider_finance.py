import pytest
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_finance_providers_can_generate():
    """Test all finance/banking providers can generate values."""
    finance_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "finance"
    ]

    failures = []
    for key_label in sorted(finance_providers):
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="finance")
            value = provider.generate_non_blank(row_data={})
            assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Finance provider failures:\n" + "\n".join(failures)
