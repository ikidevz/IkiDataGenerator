# Iki Data Generator: Synthetic Data Made Ridiculously Simple

**Stop struggling with fake data. Start generating realistic datasets in 3 lines of code.**

---

## The Problem Nobody Talks About

You're building an e-commerce platform. You need test data.

You spin up your database. You manually create 10 users. You create 5 products. You hand-craft a few orders. It's tedious. It's incomplete. It's not real enough to catch edge cases.

Then you move to testing. You need 10,000 users. 50,000 transactions. Product reviews. Payment methods. Shipping addresses. Customer history. Marketing events. And suddenly your weekend is gone.

This is the invisible tax of software development. **Developers spend millions of hours creating fake data instead of building real features.**

What if there was a better way?

---

## Meet Iki Data Generator: Synthetic Data Superpowers

Iki Data Generator is a **Python library that generates 700+ realistic data fields across 22 categories**—with zero manual effort.

Three lines of code. That's all.

```python
from ikidatagen import IkiDataGenerator

schema = ["first_name", "last_name", "email_address", "credit_card_number"]
IkiDataGenerator(schema).many(10000).export("users", formats=["csv", "json", "parquet"])
```

Boom. 10,000 users. Ready to test. Multiple formats. Zero fuss.

---

## What Makes This Different?

### 1. **700+ Data Fields Ready to Go**

Not just names and emails. We're talking:

- **Personal Data**: First names, last names, usernames, birthdates, genders, SSN, passport numbers
- **Contact Info**: Email addresses (real patterns), phone numbers (valid formats), social media handles
- **Finance**: Bank accounts, credit cards (with valid Luhn checksums), transaction histories, investment portfolios, cryptocurrency wallets
- **Healthcare**: Patient IDs, diagnosis codes (ICD-9, ICD-10), medication names, dosage amounts, medical procedures
- **E-Commerce**: Product names, SKUs, prices, descriptions, inventory levels, shipping weights
- **Location Data**: Street addresses, cities, zip codes, GPS coordinates, countries, timezones
- **Education**: Student IDs, course names, grades, GPA, degrees, universities
- **Technology**: Programming languages, frameworks, algorithms, ML model names, performance metrics
- **And 14+ more categories**

Every field is generated with **realistic patterns, valid formats, and proper constraints**. Credit card numbers pass Luhn validation. Phone numbers match regional formats. Dates respect timezone rules.

### 2. **22 Data Categories—Mix and Match**

Don't want just personal data? Combine them:

```python
schema = [
    # Personal
    "first_name",
    "last_name",
    # Finance
    "credit_card_number",
    "bank_account_balance",
    # Commerce
    "product_name",
    "product_price",
    # Location
    "street_address",
    "country"
]

IkiDataGenerator(schema).many(1000).export("customers")
```

Build exactly the dataset structure you need.

### 3. **Advanced Features That Actually Work**

#### Templates with Field Substitution

```python
schema = [
    "first_name",
    "last_name",
    {"email_template": "{{first_name}}.{{last_name}}@company.com"}
]
# Generates: john.smith@company.com, emily.johnson@company.com, ...
```

#### Custom Regex Patterns

```python
schema = [
    "first_name",
    {"custom_id": r"USER-\d{4}-[A-Z]{2}"}
]
# Generates: USER-7392-QK, USER-1203-RS, ...
```

#### Simulating Real-World Missing Data

```python
schema = [
    "customer_name",
    {"middle_name": {"blank_percentage": 30}},  # 30% null
    "email_address"
]
# Realistic data with missing values
```

#### Numeric Ranges and Constraints

```python
schema = [
    "product_name",
    {"price": {"min": 9.99, "max": 299.99}},
    {"quantity": {"min": 1, "max": 1000}}
]
```

### 4. **Export to Any Format**

Generate once, use everywhere:

```python
IkiDataGenerator(schema).many(50000).export("dataset", formats=[
    "csv",
    "json",
    "parquet",
    "sql",
    "duckdb",
    "excel",
    "xml",
    "firebase",
    "dbunit"
])
```

Whether you're loading into PostgreSQL, uploading to BigQuery, testing with pandas, or seeding a NoSQL database—we got you.

### 5. **Handles Massive Datasets**

Need 1 million records? No problem.

```python
# Efficiently chunks 1M rows
IkiDataGenerator(schema).many(1000000).export("massive_dataset", formats=["parquet"])
```

Designed for performance. Uses streaming and chunking. Won't blow up your RAM.

---

## Real-World Use Cases

### SaaS Platform Testing

```python
# 1,000 users with subscriptions, plans, usage metrics
schema = ["user_id", "email_address", "subscription_tier", "monthly_spend",
          "signup_date", "last_login", "api_calls_used"]
IkiDataGenerator(schema).many(1000).export("saas_users")
```

### E-Commerce Testing

```python
# Complete dataset: customers, products, orders, reviews
users = IkiDataGenerator(user_schema).many(500)
products = IkiDataGenerator(product_schema).many(2000)
orders = IkiDataGenerator(order_schema).many(5000)
reviews = IkiDataGenerator(review_schema).many(10000)
```

### Healthcare Systems

```python
# Patient records with HIPAA-realistic data
schema = ["patient_id", "first_name", "last_name", "dob",
          "icd10_diagnosis_code", "medication_name", "dosage"]
IkiDataGenerator(schema).many(5000).export("patients", formats=["csv"])
```

### Load Testing

```python
# 100K API requests for stress testing
schema = ["timestamp", "user_id", "endpoint", "response_time_ms", "status_code"]
IkiDataGenerator(schema).many(100000).export("load_test_events")
```

### Machine Learning Training Data

```python
# ML metrics for model performance tracking
schema = ["model_name", "accuracy", "precision", "recall", "f1_score",
          "training_time_seconds", "dataset_size"]
IkiDataGenerator(schema).many(50000).export("ml_metrics", formats=["parquet"])
```

---

## The Flex: 45+ Production-Ready Examples

We don't just give you a library. We give you a **learning playground**.

**45+ example scripts** covering:

- ✅ Getting started (3 examples)
- ✅ Personal & identity data (3 examples)
- ✅ E-commerce systems (4 examples)
- ✅ Financial data (5 examples)
- ✅ Healthcare records (3 examples)
- ✅ Real-world platforms (7 complete systems)
- ✅ Batch processing & large datasets (3 examples)
- ✅ Advanced techniques (3 examples)
- ✅ Specialized use cases like unit testing, load testing, API mocking (4 examples)
- ✅ Complete feature showcase (1 example with all 12 major features)

Each example is **runnable in one command**:

```bash
python examples/303_ecommerce_platform.py  # Full e-commerce dataset
python examples/308_hospital_system.py     # Healthcare with 300 patients, 1000 appointments
python examples/999_showcase_all_features.py  # Everything in one demo
```

Or run all 45 examples at once:

```bash
python run_all_examples.py
```

---

## Why Developers Are Switching

### ⚡ Speed

**Before**: 2 hours to set up test data  
**After**: 30 seconds with Iki Data Generator

### 🎯 Realism

**Before**: Hardcoded, obviously fake data  
**After**: Valid formats, realistic patterns, proper constraints

### 🔧 Flexibility

**Before**: Locked into one data structure  
**After**: 700+ fields, mix and match any combination

### 📊 Scalability

**Before**: Manual data creation hits a wall at ~1,000 records  
**After**: Generate millions efficiently

### 📦 Format Agnostic

**Before**: Generate CSV, manually convert to JSON, SQL, etc.  
**After**: One call, multiple formats

---

## Quick Start (Really Quick)

### Installation

```bash
pip install ikidatagen
```

### Your First Dataset

```python
from ikidatagen import IkiDataGenerator

# Define what you want
schema = [
    "first_name",
    "last_name",
    "email_address",
    "phone_number",
    "credit_card_number"
]

# Generate 100 records in 3 formats
IkiDataGenerator(schema).many(100).export("customers",
    formats=["csv", "json", "parquet"])
```

### Check Your Output

```
output/
├── customers.csv
├── customers.json
└── customers.parquet
```

Done. You have realistic test data ready to use.

---

## The Numbers

- **700+** data fields across 22 categories
- **22** data categories with specialized providers
- **45+** production-ready example scripts
- **9** export formats (CSV, JSON, Parquet, SQL, DuckDB, Excel, XML, Firebase, DBUnit)
- **1M+** records capability (tested and optimized)
- **0** manual data entry required
- **~5 seconds** to generate 100K realistic records
- **Zero** dependencies you don't need (lean stack: pandas, duckdb, pyarrow, etc.)

---

## Open Source & MIT Licensed

This isn't locked-in enterprise software. It's **MIT licensed, open source**, and built for developers.

- Fork it. Modify it. Use it commercially. No strings attached.
- Contribute new providers, formats, or features.
- Part of the growing ecosystem of data-focused Python tools.

---

## What's Next?

The roadmap includes:

- 🎯 Relationship generation (linked records across tables)
- 🌍 Locale-specific data generation
- 🎬 Streaming data generation for real-time scenarios
- 🔄 Deterministic generation (seed-based reproducibility)
- 📊 Interactive web UI for schema building
- 🚀 Performance optimizations for 100M+ records
- 🤖 AI-powered realistic value suggestion

---

## The Bottom Line

**Iki Data Generator solves a real problem that every software developer faces**: generating realistic test data without wasting hours on manual setup.

It's not just a tool. It's a **framework for thinking about synthetic data generation**. It's the dependency you'll add to every project. It's the library you'll recommend to your team.

Stop spending your weekend building fake data. Start building real features.

---

## Try It Today

```bash
# Install
pip install ikidatagen

# Run an example
python examples/00_quick_start.py

# Build your first dataset
python examples/run_all_examples.py
```

**45+ examples are waiting. Realistic data is just 3 lines away.**

---

## Share Your Thoughts

Built something cool with Iki Data Generator? Have a use case we should feature?

Drop a comment. Fork the repo. Contribute. Let's build the data generation tool the Python community deserves.

---

**Iki Data Generator** • MIT License • [GitHub](https://github.com) • [Docs](https://docs.example.com) • [Examples](https://github.com/examples)

_Generated realistic data in seconds. Because your time is worth more than manual spreadsheets._
