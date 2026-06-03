"""
309_school_system.py - Complete School & University System

Full educational system with students, courses, grades, and staff.
"""

from ikidatagen import IkiDataGenerator

print("[GRADUATION] Generating school/university system data...")

# Students
student_schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "datetime",
        "label": "DOB",
    },
    "gender_binary",
    "email_address",
    {
        "key_label": "university",
        "label": "School/University",
    },
    {
        "key_label": "degree",
        "label": "Degree",
    },
    {
        "key_label": "academic_subject",
        "label": "Major",
    },
    {
        "key_label": "current_timestamp",
        "label": "Enrollment Date",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Active", "Graduated", "On Leave", "Dropped"]}
    },
]

# Faculty/Teachers
faculty_schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "job_title",
        "label": "Position",
    },
    {
        "key_label": "department_corporate",
        "label": "Department",
    },
    "email_address",
    {
        "key_label": "current_timestamp",
        "label": "Hired Date",
    },
]

# Courses
course_schema = [
    "row_number",
    {
        "key_label": "academic_subject",
        "label": "Course",
    },
    {
        "key_label": "academic_subject",
        "label": "Subject",
    },
    {
        "key_label": "number",
        "label": "Credits",
        "options": {"min": 1, "max": 4}
    },
    "first_name",
    "last_name",
    {
        "key_label": "number",
        "label": "Capacity",
        "options": {"min": 20, "max": 500}
    },
    {
        "key_label": "number",
        "label": "Enrolled",
        "options": {"min": 10, "max": 500}
    },
]

# Grades
grade_schema = [
    "row_number",
    "first_name",
    "last_name",
    {
        "key_label": "academic_subject",
        "label": "Course",
    },
    {
        "key_label": "number",
        "label": "Score",
        "options": {"min": 0, "max": 100}
    },
    {
        "key_label": "custom_list",
        "label": "Grade",
        "options": {"values": ["A", "B", "C", "D", "F"]}
    },
    {
        "key_label": "current_timestamp",
        "label": "Date",
    },
]

# Schedule
schedule_schema = [
    "row_number",
    {
        "key_label": "course_name",
        "label": "Course",
    },
    {
        "key_label": "day_of_week",
        "label": "Day",
    },
    {
        "key_label": "time",
        "label": "Time",
    },
    {
        "key_label": "custom_list",
        "label": "Room",
        "options": {"values": ["101", "102", "201", "202", "301", "Online"]}
    },
]

print("[OK] Generating 1000 students...")
IkiDataGenerator(student_schema).many(1000).export(
    "school_students", formats=["csv"])

print("[OK] Generating 100 faculty members...")
IkiDataGenerator(faculty_schema).many(
    100).export("school_faculty", formats=["csv"])

print("[OK] Generating 200 courses...")
IkiDataGenerator(course_schema).many(200).export(
    "school_courses", formats=["csv"])

print("[OK] Generating 5000 grades...")
IkiDataGenerator(grade_schema).many(5000).export(
    "school_grades", formats=["csv"])

print("[OK] Generating 500 class schedules...")
IkiDataGenerator(schedule_schema).many(
    500).export("school_schedule", formats=["csv"])

print("\n[OK] School/University system generated!")
