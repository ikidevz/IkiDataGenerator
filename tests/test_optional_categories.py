from importlib import import_module
from pathlib import Path


def test_optional_category_extras_are_declared():
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    content = pyproject.read_text(encoding="utf-8")

    for extra_name in ["telecom", "iot", "legal", "political", "construction", "sports"]:
        assert f"{extra_name} = [" in content

    module = import_module("ikidatagen.optional_categories")
    assert "telecom" in module.OPTIONAL_CATEGORY_EXTRAS
    assert module.OPTIONAL_CATEGORY_EXTRAS["legal"] == "legal"
