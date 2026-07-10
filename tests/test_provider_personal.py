import pytest
from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import KEY_LABEL_REGISTRY


def test_all_personal_providers_can_generate():
    """Test all personal data providers can generate values."""
    personal_providers = [
        key for key, group in KEY_LABEL_REGISTRY.items() if group == "personal"
    ]

    failures = []
    for key_label in sorted(personal_providers):
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group="personal")
            value = provider.generate_non_blank(row_data={})
            assert value is not None
        except Exception as exc:
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, "Personal provider failures:\n" + "\n".join(failures)


def test_personal_provider_with_context():
    """Test personal providers with row context."""
    provider = ProviderFactory.create(key_label="full_name", group="personal")
    value = provider.generate_non_blank(row_data={"gender": "Female"})
    assert isinstance(value, str)
    assert len(value) > 0
