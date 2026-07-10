"""
Quick smoke test for IkiDataGenerator after `pip install iki-data-generator`.
Usage:
    pip install iki-data-generator
    python -m tests.quick_smoke_test
"""

from ikidatagen.core import IkiDataGenerator

SCHEMA = [
    "first_name",
    "last_name",
    {"key_label": "email_address", "label": "email"},
    {"key_label": "username", "options": {"blank_percentage": 0}},
]


def main():
    gen = IkiDataGenerator(SCHEMA)
    rows = gen.many(5)
    print("Generated rows:")
    for r in rows:
        print(r)


if __name__ == '__main__':
    main()
