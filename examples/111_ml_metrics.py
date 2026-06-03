"""
111_ml_metrics.py - Machine Learning Performance Metrics

Model performance tracking, accuracy, latency, and inference metrics.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "current_timestamp",
        "label": "Timestamp",
    },
    {
        "key_label": "model_version",
        "label": "Model Version",
    },
    {
        "key_label": "number",
        "label": "Accuracy",
        "options": {"min": 0.5, "max": 0.99}
    },
    {
        "key_label": "number",
        "label": "Precision",
        "options": {"min": 0.5, "max": 0.99}
    },
    {
        "key_label": "number",
        "label": "Recall",
        "options": {"min": 0.5, "max": 0.99}
    },
    {
        "key_label": "number",
        "label": "F1 Score",
        "options": {"min": 0.5, "max": 0.99}
    },
    {
        "key_label": "model_latency",
        "label": "Latency (ms)",
    },
    {
        "key_label": "model_confidence",
        "label": "Avg Confidence",
    },
    {
        "key_label": "cpu_utilization",
        "label": "CPU %",
    },
    {
        "key_label": "gpu_utilization",
        "label": "GPU %",
    },
    {
        "key_label": "memory_footprint",
        "label": "Memory (MB)",
    },
    {
        "key_label": "number",
        "label": "Inference Count",
        "options": {"min": 100, "max": 100000}
    },
    {
        "key_label": "data_drift_score",
        "label": "Data Drift Score",
    },
]

IkiDataGenerator(schema).many(5000).export(
    "ml_metrics", formats=["parquet", "json"])

print("[OK] Generated 5000 ML metrics records!")
