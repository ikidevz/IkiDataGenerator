from ikidatagen import IkiDataGenerator

schema = [
    {
        "label": "id",
        "key_label": "row_number",
        "options": {"blank_percentage": 0}
    },
    {
        "label": "First Name",
        "key_label": "first_name",
    },
    {
        "label": "Last Name",
        "key_label": "last_name",
    },
    {
        "label": "Username",
        "key_label": "username",
    },
    {
        "label": "Email Address",
        "key_label": "email_address",
    },
    {
        "label": "Gender",
        "key_label": "gender_binary",
    },
    {
        "label": "IP Address",
        "key_label": "ip_address_v4",
        "options": {"blank_percentage": 25}
    },
    {
        "label": "temp",
        "key_label": "template",
        "options": {"template": "{{First Name}} {{Last Name}} - {{Email Address}}"}
    },
    {
        "label": "created_at",
        "key_label": "current_timestamp",
        "options": {"blank_percentage": 10}
    },
]

IkiDataGenerator(schema).many(100).export("users", formats=["csv", "json"])
