"""
501_load_testing_data.py - Load Testing Data

Generate large datasets for load testing, performance testing, and benchmarking.
"""

from ikidatagen import IkiDataGenerator

print("⚡ Generating data for load testing...")

# High-volume event stream
event_schema = [
    "row_number",
    "username",
    {
        "key_label": "current_timestamp",
        "label": "event_time",
    },
    {
        "key_label": "custom_list",
        "label": "event_type",
        "options": {"values": ["click", "view", "purchase", "login", "error"]}
    },
    {
        "key_label": "url",
        "label": "page_url",
    },
    {
        "key_label": "country",
        "label": "country",
    },
]

# API request/response data
api_schema = [
    "row_number",
    "username",
    {
        "key_label": "current_timestamp",
        "label": "request_time",
    },
    {
        "key_label": "custom_list",
        "label": "method",
        "options": {"values": ["GET", "POST", "PUT", "DELETE"]}
    },
    {
        "key_label": "url",
        "label": "endpoint",
    },
    {
        "key_label": "number",
        "label": "status_code",
        "options": {"values": [200, 201, 400, 404, 500]}
    },
    {
        "key_label": "number",
        "label": "response_time_ms",
        "options": {"min": 10, "max": 5000}
    },
]

print("[OK] Generating 100,000 events (10 MB)...")
IkiDataGenerator(event_schema).many(100000).export(
    "load_test_events",
    formats=["csv", "parquet"]
)

print("[OK] Generating 50,000 API requests (5 MB)...")
IkiDataGenerator(api_schema).many(50000).export(
    "load_test_api",
    formats=["csv", "parquet"]
)

print("\n[OK] Load test data generated!")
print("   💡 Perfect for:")
print("      - JMeter load testing")
print("      - K6 performance testing")
print("      - Apache Bench (ab) testing")
print("      - Database load testing")
