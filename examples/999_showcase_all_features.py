"""
999_showcase_all_features.py - Complete Feature Showcase

This example demonstrates ALL major features of Iki Data Generator in one script.
Run this to see what's possible!
"""

from ikidatagen import IkiDataGenerator

print("🎪 COMPLETE FEATURE SHOWCASE FOR IKI DATA GENERATOR")
print("=" * 60)

# Feature 1: Simple String Schema
print("\n1️⃣ Simple String Schema (Shorthand)")
print("-" * 60)
simple_schema = ["first_name", "last_name", "email_address", "country"]
print(f"Schema: {simple_schema}")
IkiDataGenerator(simple_schema).many(50).export(
    "showcase_simple", formats=["csv"])
print("[OK] Generated 50 records with simple schema")

# Feature 2: Full Dict Control
print("\n2️⃣ Full Control with Dicts")
print("-" * 60)
dict_schema = [
    {
        "key_label": "row_number",
        "label": "ID",
        "options": {"blank_percentage": 0}
    },
    {
        "key_label": "first_name",
        "label": "First Name"
    },
    {
        "key_label": "product_price",
        "label": "Price",
        "group": "commerce"
    }
]
IkiDataGenerator(dict_schema).many(50).export("showcase_dict", formats=["csv"])
print("[OK] Generated 50 records with full control")

# Feature 3: Custom Labels
print("\n3️⃣ Custom Column Labels")
print("-" * 60)
label_schema = [
    {"key_label": "first_name", "label": "Customer First Name"},
    {"key_label": "last_name", "label": "Customer Last Name"},
    {"key_label": "email_address", "label": "Email Contact"},
]
IkiDataGenerator(label_schema).many(50).export(
    "showcase_labels", formats=["csv"])
print("[OK] Custom labels in output columns")

# Feature 4: Templates
print("\n4️⃣ Templates - Combining Fields")
print("-" * 60)
template_schema = [
    "first_name",
    "last_name",
    "email_address",
    "city",
    "country",
    {
        "key_label": "template",
        "label": "Full Name",
        "options": {"template": "{{first_name}} {{last_name}}"}
    },
    {
        "key_label": "template",
        "label": "Address Line",
        "options": {"template": "{{city}}, {{country}}"}
    },
]
IkiDataGenerator(template_schema).many(50).export(
    "showcase_templates", formats=["csv"])
print("[OK] Generated combined fields with templates")

# Feature 5: Regex Patterns
print("\n5️⃣ Regular Expressions - Custom Patterns")
print("-" * 60)
regex_schema = [
    "first_name",
    "last_name",
    {
        "key_label": "regular_expression",
        "label": "Order ID",
        "options": {"pattern": "ORD-[A-Z]{3}-[0-9]{5}"}
    },
    {
        "key_label": "regular_expression",
        "label": "Product Code",
        "options": {"pattern": "P[0-9]{4}[A-Z]{2}"}
    },
]
IkiDataGenerator(regex_schema).many(50).export(
    "showcase_regex", formats=["csv"])
print("[OK] Generated custom pattern data with regex")

# Feature 6: Blank Percentages
print("\n6️⃣ Blank Percentages - Missing Data Simulation")
print("-" * 60)
blank_schema = [
    {"key_label": "row_number", "options": {"blank_percentage": 0}},
    {"key_label": "first_name", "options": {"blank_percentage": 5}},
    {"key_label": "phone", "options": {"blank_percentage": 40}},
    {"key_label": # "middle_name", "options": {"blank_percentage": 60}},
]
IkiDataGenerator(blank_schema).many(50).export(
    "showcase_blanks", formats=["csv"])
print("[OK] Generated data with realistic missing values")

# Feature 7: Numeric Ranges
print("\n7️⃣ Numeric Ranges - Min/Max Control")
print("-" * 60)
numeric_schema = [
    "product_name",
    {"key_label": "number", "label": "Quantity", "options": {"min": 1, "max": 100}},
    {"key_label": "number", "label": "Price", "options": {"min": 10, "max": 1000}},
    {"key_label": "number", "label": "Rating", "options": {"min": 1, "max": 5}},
]
IkiDataGenerator(numeric_schema).many(50).export(
    "showcase_numeric", formats=["csv"])
print("[OK] Generated numeric data with ranges")

# Feature 8: Custom Lists
print("\n8️⃣ Custom Lists - Specific Value Options")
print("-" * 60)
list_schema = [
    "first_name",
    "last_name",
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Active", "Inactive", "Pending", "Archived"]}
    },
    {
        "key_label": "custom_list",
        "label": "Priority",
        "options": {"values": ["High", "Medium", "Low"]}
    },
]
IkiDataGenerator(list_schema).many(50).export(
    "showcase_lists", formats=["csv"])
print("[OK] Generated data from custom value lists")

# Feature 9: Multiple Export Formats
print("\n9️⃣ Multiple Export Formats")
print("-" * 60)
format_schema = ["first_name", "last_name", "email_address", "country"]
IkiDataGenerator(format_schema).many(100).export(
    "showcase_formats",
    formats=["csv", "json", "tsv", "parquet"]
)
print("[OK] Exported to: CSV, JSON, TSV, Parquet")

# Feature 10: All Major Categories
print("\n🔟 All 22 Data Categories")
print("-" * 60)
categories_schema = [
    # Personal
    "first_name", "last_name", "gender_binary", "date_of_birth",
    # Contact
    "email_address", "phone_number", "username",
    # Location
    "country", "city", "street_address",
    # Finance
    "credit_card_number", "money", "currency",
    # Commerce
    "product_name", "product_price", "sku",
    # Healthcare
    "blood_type", "disease_name",
    # IT
    "programming_language", "software_framework",
    # AI/ML
    "model_type", "model_framework",
    # And more...
]
IkiDataGenerator(categories_schema).many(50).export(
    "showcase_categories", formats=["json"])
print("[OK] Data from 10+ categories combined in one dataset")

# Feature 11: Large Datasets
print("\n1️⃣1️⃣ Large Dataset Generation")
print("-" * 60)
print("Generating 100,000 records with Parquet (efficient format)...")
large_schema = ["first_name", "last_name", "email_address", "country"]
IkiDataGenerator(large_schema).many(100000).export(
    "showcase_large", formats=["parquet"])
print("[OK] Generated 100,000 records efficiently")

# Feature 12: Real-World Scenario
print("\n1️⃣2️⃣ Real-World E-Commerce Scenario")
print("-" * 60)
ecommerce_schema = [
    "row_number",
    "first_name",
    "last_name",
    "email_address",
    "product_name",
    {"key_label": "product_price", "label": "price"},
    {"key_label": "number", "label": "quantity", "options": {"min": 1, "max": 10}},
    {
        "key_label": "custom_list",
        "label": "status",
        "options": {"values": ["Pending", "Shipped", "Delivered"]}
    },
    {"key_label": "current_timestamp", "label": "order_date"},
    {
        "key_label": "template",
        "label": "description",
        "options": {"template": "Order by {{first_name}} {{last_name}} - {{product_name}}"}
    },
]
IkiDataGenerator(ecommerce_schema).many(200).export(
    "showcase_ecommerce", formats=["csv", "json"])
print("[OK] Complete e-commerce order data")

print("\n" + "=" * 60)
print("[OK] SHOWCASE COMPLETE!")
print("=" * 60)
print("\n[FOLDER] Generated files in output/:")
print("   - showcase_simple.csv")
print("   - showcase_dict.csv")
print("   - showcase_labels.csv")
print("   - showcase_templates.csv")
print("   - showcase_regex.csv")
print("   - showcase_blanks.csv")
print("   - showcase_numeric.csv")
print("   - showcase_lists.csv")
print("   - showcase_formats.* (csv, json, tsv, parquet)")
print("   - showcase_categories.json")
print("   - showcase_large.parquet (100K records!)")
print("   - showcase_ecommerce.* (csv, json)")
print("\n💡 Next steps:")
print("   1. Review the output files")
print("   2. Try modifying the schemas above")
print("   3. Check examples/ folder for more use cases")
print("   4. Read README.md for full documentation")
