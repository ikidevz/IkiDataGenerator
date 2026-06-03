"""
502_demo_data.py - Demo & Presentation Data

Create engaging demo datasets for presentations, prototypes, and showcases.
"""

from ikidatagen import IkiDataGenerator

print("[FILM] Generating presentation demo data...")

# SaaS metrics dashboard
dashboard_schema = [
    {
        "key_label": "row_number",
        "label": "Day",
    },
    {
        "key_label": "number",
        "label": "New Users",
        "options": {"min": 50, "max": 500}
    },
    {
        "key_label": "number",
        "label": "Active Users",
        "options": {"min": 1000, "max": 10000}
    },
    {
        "key_label": "money",
        "label": "Revenue",
        "options": {"min": 1000, "max": 50000}
    },
    {
        "key_label": "number",
        "label": "Conversion Rate %",
        "options": {"min": 0.5, "max": 5}
    },
    {
        "key_label": "number",
        "label": "Churn Rate %",
        "options": {"min": 0.1, "max": 2}
    },
]

# E-Commerce demo
ecommerce_schema = [
    "product_name",
    {
        "key_label": "number",
        "label": "Units Sold",
        "options": {"min": 10, "max": 1000}
    },
    {
        "key_label": "product_price",
        "label": "Price",
    },
    {
        "key_label": "number",
        "label": "Revenue",
        "options": {"min": 100, "max": 100000}
    },
    {
        "key_label": "rating",
        "label": "Rating",
    },
    {
        "key_label": "number",
        "label": "Reviews",
        "options": {"min": 0, "max": 1000}
    },
]

# Employee performance
performance_schema = [
    "first_name",
    "last_name",
    "department",
    {
        "key_label": "job_title",
        "label": "Position",
    },
    {
        "key_label": "number",
        "label": "Performance Score",
        "options": {"min": 1, "max": 10}
    },
    {
        "key_label": "money",
        "label": "Salary",
    },
    {
        "key_label": "number",
        "label": "Years",
        "options": {"min": 1, "max": 30}
    },
]

print("[OK] Generating dashboard metrics (30 records)...")
IkiDataGenerator(dashboard_schema).many(30).export(
    "demo_dashboard", formats=["csv", "json"])

print("[OK] Generating e-commerce demo (50 records)...")
IkiDataGenerator(ecommerce_schema).many(50).export(
    "demo_ecommerce", formats=["csv", "json"])

print("[OK] Generating employee performance (100 records)...")
IkiDataGenerator(performance_schema).many(100).export(
    "demo_performance", formats=["csv", "json"])

print("\n[OK] Demo data ready for presentations!")
