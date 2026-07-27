"""Consolidated provider regression tests."""

import json
import warnings
from pathlib import Path

import pytest

from ikidatagen.provider_factory import ProviderFactory
from ikidatagen.schema_registry import (
    DEPRECATED_KEY_LABELS,
    KEY_LABEL_REGISTRY,
    resolve_key_label,
)


def _provider_keys_for_group(group):
    return sorted(
        key for key, label_group in KEY_LABEL_REGISTRY.items() if label_group == group
    )


def _assert_group_providers_generate(
    group,
    *,
    row_data=None,
    required_options=None,
    blank_allowed=None,
):
    failures = []
    blank_allowed = set(blank_allowed or ())
    required_options = required_options or {}

    for key_label in _provider_keys_for_group(group):
        options = required_options.get(key_label, {})
        try:
            provider = ProviderFactory.create(
                key_label=key_label, group=group, **options)
            value = provider.generate_non_blank(row_data=row_data or {})
            if key_label not in blank_allowed:
                assert value is not None
        except Exception as exc:  # pragma: no cover - exercised by the test harness
            failures.append(f"{key_label}: {exc.__class__.__name__}: {exc}")

    assert not failures, f"{group.title()} provider failures:\n" + \
        "\n".join(failures)


@pytest.mark.parametrize(
    ("group", "row_data", "required_options", "blank_allowed"),
    [
        ("advanced", {"value": "data"}, {
            "custom_list": {"values": ["alpha", "beta"]},
            "lambda": {"func": lambda row_data=None: "ok"},
            "template": {"template": "Test: {{value}}"},
        }, ()),
        ("ai", None, None, ()),
        ("basic", None, {
            "custom_list": {"values": ["option1", "option2"]},
            "number": {"values": [100, 200, 300]},
        }, {"blank"}),
        ("car", None, None, ()),
        ("commerce", None, None, ()),
        ("telecom", None, None, ()),
        ("infrastructure", None, None, ()),
        ("blockchain", None, None, ()),
        ("education", None, None, ()),
        ("finance", None, None, ()),
        ("gaming", None, None, ()),
        ("health", None, None, ()),
        ("developer_tools", None, None, ()),
        ("legal", None, None, ()),
        ("location", None, None, ()),
        ("marketing", None, None, ()),
        ("nature", None, None, ()),
        ("personal", None, None, ()),
        ("political", None, None, ()),
        ("entertainment", None, None, ()),
        ("gaming_sports", None, None, ()),
        ("travel", None, None, ()),
    ],
)
def test_provider_groups_can_generate(group, row_data, required_options, blank_allowed):
    """Each provider group should be constructible and able to emit a value."""
    _assert_group_providers_generate(
        group,
        row_data=row_data,
        required_options=required_options,
        blank_allowed=blank_allowed,
    )


def test_json_array_provider():
    """JSON array providers should generate valid JSON payloads."""
    provider = ProviderFactory.create(
        key_label="json_array",
        group="advanced",
        min_elements=1,
        max_elements=3,
    )
    value = provider.generate_non_blank(row_data={})
    parsed = json.loads(value)
    assert isinstance(parsed, list)


def test_template_provider():
    """Template providers should support placeholder expansion."""
    provider = ProviderFactory.create(
        key_label="template",
        group="advanced",
        template="User: {{first_name}}",
    )
    value = provider.generate_non_blank(row_data={"first_name": "John"})
    assert "User:" in value
    assert "John" in value


def test_commerce_credit_card_provider_with_card_type():
    """Commerce card providers should respect supplied card-type context."""
    provider = ProviderFactory.create(
        key_label="credit_card_number", group="commerce")
    value = provider.generate_non_blank(row_data={"credit_card_type": "Visa"})
    assert isinstance(value, str)
    assert len(value) > 0


def test_non_tezos_blockchain_providers_are_available():
    """The blockchain family should include broader non-Tezos primitives."""
    for key_label in ["solana_address", "tron_address", "blockchain_network", "transaction_hash"]:
        assert key_label in KEY_LABEL_REGISTRY
        assert KEY_LABEL_REGISTRY[key_label] == "blockchain"

        provider = ProviderFactory.create(
            key_label=key_label, group="blockchain")
        value = provider.generate_non_blank(row_data={})
        assert value is not None


def test_location_providers_with_country_context():
    """Location providers should be able to use country-specific context."""
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


def test_personal_provider_with_context():
    """Personal providers should support row-level context."""
    provider = ProviderFactory.create(key_label="full_name", group="personal")
    value = provider.generate_non_blank(row_data={"gender": "Female"})
    assert isinstance(value, str)
    assert len(value) > 0


def test_no_duplicate_provider_filenames():
    """Provider filenames should be unique within the providers package."""
    root = Path("src/ikidatagen/providers")
    names = {}

    for path in root.rglob("*.py"):
        if path.name == "__init__.py":
            continue
        names.setdefault(path.name, []).append(str(path))

    dupes = {name: paths for name, paths in names.items() if len(paths) > 1}
    if dupes:
        msg_lines = [
            "Duplicate provider filenames detected (basename -> files):"]
        for name, paths in sorted(dupes.items()):
            msg_lines.append(f"  {name} ->")
            for path in paths:
                msg_lines.append(f"    - {path}")
        raise AssertionError("\n".join(msg_lines))


def test_provider_files_are_registered():
    """Each provider module should have a registry entry in the expected group."""
    root = Path("src/ikidatagen/providers")
    missing = []
    mismatched = []

    for path in root.rglob("*.py"):
        if path.name == "__init__.py":
            continue
        if path.parent == root:
            continue

        group = path.parent.name
        key_label = path.stem
        if key_label not in KEY_LABEL_REGISTRY:
            missing.append(str(path))
        elif KEY_LABEL_REGISTRY[key_label] != group:
            mismatched.append(
                (str(path), KEY_LABEL_REGISTRY[key_label], group))

    assert not missing, f"Provider files missing registry entries: {missing}"
    assert not mismatched, (
        "Provider files have registry group mismatches:\n"
        + "\n".join(
            f"{path} expected {expected}, found {actual}"
            for path, expected, actual in mismatched
        )
    )


def test_deprecated_key_labels_resolve_to_canonical_provider():
    """Deprecated aliases should still resolve to the canonical provider class."""
    with warnings.catch_warnings(record=True) as records:
        warnings.simplefilter("always", DeprecationWarning)
        provider = ProviderFactory.create("job")

    assert provider.__class__.__name__ == "JobTitleProvider"
    assert any(
        issubclass(w.category.__class__, type) if hasattr(
            w, "category") else True
        for w in records
    ) or records, "Expected a deprecation warning for alias key_label 'job'"


def test_deprecated_key_labels_resolve_to_registered_keys():
    """All deprecated aliases should map to a registered canonical key."""
    invalid = []
    for alias, canonical in DEPRECATED_KEY_LABELS.items():
        resolved = resolve_key_label(alias)
        if resolved != canonical or canonical not in KEY_LABEL_REGISTRY:
            invalid.append((alias, canonical, resolved))

    assert not invalid, (
        "All deprecated key labels must resolve to a registered canonical key label. "
        f"Invalid mappings: {invalid}"
    )


def test_contract_type_provider_uses_legal_group():
    """The contract_type provider should resolve to the legal provider module."""
    provider = ProviderFactory.create("contract_type")
    assert provider.__class__.__name__ == "ContractTypeProvider"
    assert provider.__class__.__module__.endswith("legal.contract_type")


def test_occupation_and_job_title_map_to_valid_personal_providers():
    """Occupation-related aliases should resolve to the expected personal providers."""
    job_title = ProviderFactory.create("job_title")
    occupation = ProviderFactory.create("occupation")

    assert job_title.__class__.__name__ == "JobTitleProvider"
    assert occupation.__class__.__name__ == "OccupationProvider"


def test_legacy_group_aliases_are_not_used_for_import_resolution():
    """Older group aliases should not be accepted for module resolution."""
    with pytest.raises(ValueError, match="Provider module not found"):
        ProviderFactory.create(key_label="apn_settings", group="communication")


def test_canonical_group_resolves_directly():
    """Canonical groups should resolve to their provider modules directly."""
    provider = ProviderFactory.create(
        key_label="apn_settings", group="telecom")
    assert provider is not None
