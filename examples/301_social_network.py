"""
301_social_network.py - Social Media Platform Data

Complete social network dataset with users, posts, and interactions.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    "username",
    {
        "key_label": "email_address",
        "label": "Email",
    },
    {
        "key_label": "profile_picture_url",
        "label": "Profile Picture",
        "options": {"blank_percentage": 20}
    },
    {
        "key_label": "current_timestamp",
        "label": "Account Created",
    },
    {
        "key_label": "current_timestamp",
        "label": "Last Active",
    },
    {
        "key_label": "number",
        "label": "Followers",
        "options": {"min": 0, "max": 10000}
    },
    {
        "key_label": "number",
        "label": "Following",
        "options": {"min": 0, "max": 5000}
    },
    {
        "key_label": "words",
        "label": "Bio",
        "options": {"blank_percentage": 30}
    },
    {
        "key_label": "custom_list",
        "label": "Account Type",
        "options": {"values": ["Personal", "Business", "Creator", "Verified"]}
    },
    {
        "key_label": "boolean",
        "label": "Private Account",
    },
]

IkiDataGenerator(schema).many(2000).export(
    "social_users", formats=["csv", "json"])

print("[OK] Generated 2000 social network users!")
