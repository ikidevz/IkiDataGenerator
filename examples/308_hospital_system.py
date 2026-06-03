"""
308_hospital_system.py - Complete Hospital Management System

Full hospital network with patients, doctors, appointments, and billing.
"""

from ikidatagen import IkiDataGenerator

print("[HOSPITAL] Generating hospital management system data...")

# Patients
patient_schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "datetime",
        "label": "DOB",
    },
    "gender_binary",
    {
        "key_label": "blood_type",
        "label": "Blood Type",
    },
    "phone",
    "email_address",
    {
        "key_label": "street_address",
        "label": "Address",
    },
    {
        "key_label": "current_timestamp",
        "label": "Admission Date",
    },
]

# Doctors/Staff
doctor_schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "medical_specialty",
        "label": "Specialty",
    },
    {
        "key_label": "ssn",
        "label": "License",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Active", "On Leave", "Retired"]}
    },
]

# Appointments
appointment_schema = [
    "row_number",
    {
        "key_label": "current_timestamp",
        "label": "Date Time",
    },
    "first_name",
    "last_name",
    {
        "key_label": "first_name",
        "label": "Doctor First Name",
    },
    {
        "key_label": "last_name",
        "label": "Doctor Last Name",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Scheduled", "Completed", "Cancelled", "No Show"]}
    },
    {
        "key_label": "number",
        "label": "Duration (min)",
        "options": {"min": 15, "max": 120}
    },
]

# Medical Records
medical_schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "disease_name",
        "label": "Diagnosis",
    },
    {
        "key_label": "icd10_diagnosis_code",
        "label": "ICD-10",
    },
    {
        "key_label": "drug_name_generic",
        "label": "Medication",
    },
    {
        "key_label": "current_timestamp",
        "label": "Date",
    },
]

# Billing
billing_schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "money",
        "label": "Amount",
    },
    {
        "key_label": "insurance_type",
        "label": "Insurance",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Pending", "Paid", "Rejected"]}
    },
    {
        "key_label": "current_timestamp",
        "label": "Date",
    },
]

print("[OK] Generating 300 patients...")
IkiDataGenerator(patient_schema).many(300).export(
    "hospital_patients", formats=["csv"])

print("[OK] Generating 50 doctors...")
IkiDataGenerator(doctor_schema).many(50).export(
    "hospital_doctors", formats=["csv"])

print("[OK] Generating 1000 appointments...")
IkiDataGenerator(appointment_schema).many(1000).export(
    "hospital_appointments", formats=["csv"])

print("[OK] Generating 500 medical records...")
IkiDataGenerator(medical_schema).many(500).export(
    "hospital_medical_records", formats=["csv"])

print("[OK] Generating 800 billing records...")
IkiDataGenerator(billing_schema).many(800).export(
    "hospital_billing", formats=["csv"])

print("\n[OK] Hospital management system generated!")
