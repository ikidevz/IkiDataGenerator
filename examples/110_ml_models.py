"""
110_ml_models.py - AI/ML Model Data

Machine learning models, frameworks, versions, and metadata.
"""

from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    {
        "key_label": "model_type",
        "label": "Model Type",
    },
    {
        "key_label": "model_framework",
        "label": "Framework",
    },
    {
        "key_label": "model_task",
        "label": "Task",
    },
    {
        "key_label": "model_version",
        "label": "Version",
    },
    {
        "key_label": "model_owner",
        "label": "Owner",
    },
    {
        "key_label": "model_input_format",
        "label": "Input Format",
    },
    {
        "key_label": "model_output_format",
        "label": "Output Format",
    },
    {
        "key_label": "model_deployment_env",
        "label": "Deployment Env",
    },
    {
        "key_label": "model_lifecycle_stage",
        "label": "Lifecycle Stage",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Development", "Testing", "Staging", "Production", "Deprecated"]}
    },
    {
        "key_label": "current_timestamp",
        "label": "Created",
    },
    {
        "key_label": "current_timestamp",
        "label": "Updated",
    },
]

IkiDataGenerator(schema).many(200).export("ml_models", formats=["csv", "json"])

print("[OK] Generated 200 ML models!")
