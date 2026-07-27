from __future__ import annotations

OPTIONAL_CATEGORY_EXTRAS = {
    "telecom": "telecom",
    "iot": "iot",
    "legal": "legal",
    "political": "political",
    "construction": "construction",
    "sports": "sports",
}


def get_optional_category_extras() -> dict[str, str]:
    return dict(OPTIONAL_CATEGORY_EXTRAS)
