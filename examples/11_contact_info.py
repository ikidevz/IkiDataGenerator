"""
11_contact_info.py - Contact Information

Email, phone, social media, and messaging data.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "username",
    "email_address",
    "phone",
    {
        "key_label": "social_media_platform",
        "label": "Social Media",
    },
    {
        "key_label": "phone",
        "label": "Secondary Phone",
        "options": {"blank_percentage": 40}  # 40% missing
    },
    {
        "key_label": "sentences",
        "label": "Last Message",
    },
    {
        "key_label": "first_name",
        "label": "Contact First Name",
    },
    {
        "key_label": "last_name",
        "label": "Contact Last Name",
    },
]

IkiDataGenerator(schema).many(200).export(
    "contact_info", formats=["csv", "json"])

print("[OK] Generated 200 contact records!")
