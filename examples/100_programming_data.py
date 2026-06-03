"""
100_programming_data.py - Programming & IT Data

Programming languages, frameworks, libraries, and tech stack data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "programming_language",
        "label": "Language",
    },
    {
        "key_label": "software_framework",
        "label": "Framework",
    },
    {
        "key_label": "version_number",
        "label": "Version",
    },
    {
        "key_label": "number",
        "label": "Stars",
        "options": {"min": 0, "max": 100000}
    },
    {
        "key_label": "number",
        "label": "Downloads (millions)",
        "options": {"min": 0, "max": 1000}
    },
    {
        "key_label": "custom_list",
        "label": "License",
        "options": {"values": ["MIT", "Apache 2.0", "GPL", "BSD", "ISC"]}
    },
    {
        "key_label": "current_timestamp",
        "label": "Release Date",
    },
    {
        "key_label": "url",
        "label": "Repository",
    },
]

IkiDataGenerator(schema).many(300).export(
    "programming_tech", formats=["csv", "json"])

print("[OK] Generated 300 programming/tech records!")
