"""
90_gaming_players.py - Gaming Platform Players & Characters

RPG/MMORPG player data with characters, guilds, and progression.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "username",
    "email_address",
    {
        "key_label": "first_name",
        "label": "Character Name",
    },
    {
        "key_label": "dream_job",
        "label": "Class",
    },
    {
        "key_label": "guild_name",
        "label": "Guild",
        "options": {"blank_percentage": 30}
    },
    {
        "key_label": "number",
        "label": "Level",
        "options": {"min": 1, "max": 100}
    },
    {
        "key_label": "number",
        "label": "Experience Points",
        "options": {"min": 0, "max": 10000000}
    },
    {
        "key_label": "money",
        "label": "Gold",
    },
    {
        "key_label": "current_timestamp",
        "label": "Account Created",
    },
    {
        "key_label": "current_timestamp",
        "label": "Last Played",
    },
]

IkiDataGenerator(schema).many(500).export(
    "gaming_players", formats=["csv", "json"])

print("[OK] Generated 500 gaming players!")
