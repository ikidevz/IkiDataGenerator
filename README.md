# 🎲 Iki Data Generator

> Generate realistic, diverse synthetic data with 700+ built-in fields across 22 categories. Perfect for testing, development, and prototyping — without the legal baggage of real data.

---

![image](assets/cover.png)

## What Is This?

**Iki Data Generator** is a Python library that creates synthetic datasets on demand. Instead of wrestling with dummy data or copy-pasting fake records, you define a _schema_ (which fields you want), call `.many(n)` to generate _n_ records, and export them to CSV, JSON, SQL, Excel, Parquet, or 10+ other formats. That's it.

It's built for developers who need:

- **Test data** for unit/integration tests
- **Demo data** for presentations or prototypes
- **Mock databases** for local development
- **Privacy-friendly datasets** with realistic properties but zero personal info
- **Performance testing** with large datasets

---

## Why Use Iki Data Generator?

### ✅ You Get

| Benefit                            | What It Means                                                                                   |
| ---------------------------------- | ----------------------------------------------------------------------------------------------- |
| **700+ Fields**                    | First name, email, credit card, medical codes, stock prices, cryptocurrencies, ML metrics, etc. |
| **22 Categories**                  | Personal, Finance, Commerce, Healthcare, Location, Education, Legal, AI/ML, and more            |
| **Easy Schema**                    | Simple string shortcuts or full control with dicts                                              |
| **Flexible Export**                | CSV, JSON, SQL, Parquet, DuckDB, Excel, XML, TSV, Firebase, more                                |
| **Zero Dependencies on Real Data** | No need to anonymize or worry about PII                                                         |
| **Blazing Fast**                   | Generates thousands of records instantly                                                        |
| **Extensible**                     | Add custom providers for domain-specific fields                                                 |

### ❌ You Don't Get

- No real person's data
- No need for data anonymization lawyers
- No internet calls to fake APIs
- No massive CSV files to download and commit

---

## Installation

### From PyPI (recommended)

```bash
pip install iki-data-generator
```

### From Source

```bash
git clone https://github.com/ikidevz/IkiDataGenerator.git
cd Iki-Data-Generator
pip install -e .
```

### Requirements

- **Python** ≥ 3.10
- **Dependencies**: duckdb, pandas, pyarrow, numpy, openpyxl, bcrypt, and a few others (installed automatically)

---

## Quick Start (60 Seconds)

### The Simplest Example

```python
from ikidatagen import IkiDataGenerator

# Define what fields you want
schema = ["first_name", "last_name", "email_address", "gender_binary"]

# Generate 100 records
data = IkiDataGenerator(schema).many(100).export("users")
```

**Result:** You now have `output/users.csv` and `output/users.json` with 100 realistic user records.

### A More Realistic Example

```python
from ikidatagen import IkiDataGenerator

schema = [
    {
        "label": "User ID",
        "key_label": "row_number",
        "options": {"blank_percentage": 0}  # No blanks for ID
    },
    "first_name",
    "last_name",
    "email_address",
    {
        "label": "Account Created",
        "key_label": "current_timestamp",
        "options": {"blank_percentage": 5}  # 5% will be blank
    },
    {
        "label": "IP Address",
        "key_label": "ip_address_v4",
        "options": {"blank_percentage": 25}  # 25% will be blank
    },
    {
        "label": "Full Profile",
        "key_label": "template",
        "options": {
            "template": "{{first_name}} {{last_name}} ({{email_address}})"
        }
    },
]

# Generate 500 records and save to both CSV and JSON
IkiDataGenerator(schema).many(500).export("users", formats=["csv", "json"])
```

**Result:** `output/users.csv` and `output/users.json` with 500 complete user records, ready to use.

---

## Common Use Cases

### 1. E-Commerce Platform Testing

Generate realistic customer orders, inventory, and transactions:

```python
from ikidatagen import IkiDataGenerator

ecommerce_schema = [
    "row_number",  # Order ID
    "current_timestamp",  # Order date
    "first_name",
    "email_address",
    {"key_label": "product_name", "label": "Product"},
    {"key_label": "product_price", "label": "Price", "options": {"min": 9.99, "max": 299.99}},
    {"key_label": "discount_percentage", "label": "Discount %", "options": {"blank_percentage": 70}},
    {"key_label": "order_status", "label": "Order Status"},
    {"key_label": "payment_method", "label": "Payment Method"},
    {"key_label": "shipping_method", "label": "Shipping"},
    {"key_label": "delivery_status", "label": "Status"},
]

generator = IkiDataGenerator(ecommerce_schema)
orders_data = generator.many(10000).export("ecommerce_orders")
```

### 2. Healthcare Records System

Generate HIPAA-safe test data for medical applications:

```python
healthcare_schema = [
    {"key_label": "row_number", "label": "Patient ID", "options": {"blank_percentage": 0}},
    "first_name",
    "last_name",
    "email_address",
    "phone_number",
    {"key_label": "date_of_birth", "label": "DOB", "options": {"from_date": "1950-01-01", "to_date": "2010-12-31"}},
    {"key_label": "blood_type", "label": "Blood Type"},
    {"key_label": "icd10_code", "label": "Diagnosis Code"},
    {"key_label": "medication_generic_name", "label": "Medication"},
    {"key_label": "vital_signs_blood_pressure", "label": "BP"},
    {"key_label": "lab_result_name", "label": "Lab Test"},
    {"key_label": "insurance_plan_name", "label": "Insurance"},
    {"key_label": "current_timestamp", "label": "Visit Date"},
]

generator = IkiDataGenerator(healthcare_schema)
patients = generator.many(5000).export("patient_records")
```

### 3. Financial Data for Testing

Generate bank accounts, transactions, and investment data:

```python
finance_schema = [
    "row_number",
    "first_name",
    "last_name",
    {"key_label": "account_number", "label": "Account #"},
    {"key_label": "iban", "label": "IBAN"},
    {"key_label": "credit_card_number", "label": "Card #"},
    {"key_label": "credit_card_type", "label": "Card Type"},
    {"key_label": "money", "label": "Balance", "options": {"min": 100, "max": 50000, "currency": "USD"}},
    {"key_label": "transaction_amount", "label": "Transaction", "options": {"min": 0.01, "max": 5000}},
    {"key_label": "transaction_type", "label": "Type"},
    {"key_label": "stock_symbol", "label": "Stock"},
    {"key_label": "cryptocurrency_name", "label": "Crypto"},
]

generator = IkiDataGenerator(finance_schema)
transactions = generator.many(50000).export("financial_data")
```

### 4. Educational Institution Data

Generate student and course enrollment data:

```python
education_schema = [
    {"key_label": "student_id", "label": "Student ID", "options": {"blank_percentage": 0}},
    "first_name",
    "last_name",
    "email_address",
    {"key_label": "major", "label": "Major"},
    {"key_label": "gpa", "label": "GPA", "options": {"min": 0.0, "max": 4.0}},
    {"key_label": "class_year", "label": "Year"},
    {"key_label": "enrollment_status", "label": "Status"},
    {"key_label": "course_name", "label": "Course"},
    {"key_label": "grade", "label": "Grade"},
    {"key_label": "date_of_birth", "label": "DOB"},
]

generator = IkiDataGenerator(education_schema)
students = generator.many(2000).export("student_data")
```

### 5. API Response Mocking

Generate realistic API response data:

```python
api_schema = [
    {"key_label": "uuid", "label": "id"},
    "first_name",
    "last_name",
    "email_address",
    {"key_label": "current_timestamp", "label": "created_at"},
    {"key_label": "current_timestamp", "label": "updated_at"},
    {"key_label": "json_web_token", "label": "auth_token"},
    {"key_label": "boolean", "label": "is_active"},
]

generator = IkiDataGenerator(api_schema)
api_data = generator.many(100).export("api_response", formats=["json"])
```

---

## Schema Definition

The schema is the heart of Iki Data Generator. It tells the library what fields to generate.

### Schema Entry Types

#### 1. **Simple String (Shorthand)**

```python
schema = ["first_name", "last_name", "email_address"]
# Generates fields with default settings, no options
```

#### 2. **Full Control (Dict)**

```python
schema = [
    {
        "key_label": "email_address",      # Required: which provider to use
        "label": "Email",                  # Optional: output column name (defaults to key_label)
        "group": "personal",               # Optional: provider category (auto-resolved if omitted)
        "options": {"blank_percentage": 10}  # Optional: provider-specific config
    }
]
```

### Key Parameters

| Parameter     | Required? | Description                                                         |
| ------------- | --------- | ------------------------------------------------------------------- |
| **key_label** | ✅ Yes    | The provider name (e.g., `first_name`, `credit_card_number`)        |
| **label**     | ❌ No     | How to name the output column (defaults to `key_label`)             |
| **group**     | ❌ No     | Provider category (auto-resolved from registry; override if needed) |
| **options**   | ❌ No     | Provider-specific settings (e.g., `blank_percentage`, `template`)   |

### Available Options (Common & Provider-Specific)

#### Universal Options (All Providers)

| Option               | Type      | Default | Range | Example | Effect                                     |
| -------------------- | --------- | ------- | ----- | ------- | ------------------------------------------ |
| **blank_percentage** | int/float | 0       | 0-100 | `10`    | Percentage of records where field is empty |

#### Numeric Provider Options

```python
# For: number, money, age, gpa, rating, price, quantity
schema = [
    {
        "key_label": "number",
        "options": {
            "blank_percentage": 5,      # Optional: % blanks
            "min": 0,                   # Optional: minimum value
            "max": 100,                 # Optional: maximum value
            "decimals": 2               # Optional: decimal places
        }
    }
]
```

| Option       | Type      | Default | Range | Effect                   |
| ------------ | --------- | ------- | ----- | ------------------------ |
| **min**      | int/float | 0       | Any   | Minimum value generated  |
| **max**      | int/float | 100     | Any   | Maximum value generated  |
| **decimals** | int       | 0       | 0-10  | Number of decimal places |

#### Date & Time Provider Options

```python
# For: date_time, date_of_birth, timestamp, current_timestamp
schema = [
    {
        "key_label": "date_time",
        "options": {
            "blank_percentage": 5,
            "from_date": "2020-01-01",     # Optional: start date
            "to_date": "2025-12-31",       # Optional: end date
            "date_format": "%Y-%m-%d",     # Optional: output format
            "minimum_age": 18,             # Optional: minimum age (instead of from_date)
            "maximum_age": 65              # Optional: maximum age (instead of to_date)
        }
    }
]
```

| Option          | Type | Example                      | Effect                  |
| --------------- | ---- | ---------------------------- | ----------------------- |
| **from_date**   | str  | `"2020-01-01"`               | Start date (YYYY-MM-DD) |
| **to_date**     | str  | `"2025-12-31"`               | End date (YYYY-MM-DD)   |
| **date_format** | str  | `"%Y-%m-%d"` or `"%m/%d/%Y"` | Python datetime format  |
| **minimum_age** | int  | `18`                         | Minimum age in years    |
| **maximum_age** | int  | `65`                         | Maximum age in years    |

**Common Date Format Codes:**

```
%Y  → 4-digit year (2024)
%y  → 2-digit year (24)
%m  → Month as number (01-12)
%d  → Day of month (01-31)
%H  → Hour (00-23)
%M  → Minute (00-59)
%S  → Second (00-59)
%A  → Full weekday (Monday)
%a  → Abbreviated weekday (Mon)
%B  → Full month (January)
%b  → Abbreviated month (Jan)
```

#### String Template Provider Options

```python
# For: template
schema = [
    {
        "key_label": "template",
        "options": {
            "blank_percentage": 5,
            "template": "{{first_name}} {{last_name}} ({{email_address}})"
        }
    }
]
```

| Option       | Type | Effect                                      |
| ------------ | ---- | ------------------------------------------- |
| **template** | str  | Template with `{{field_name}}` placeholders |

**Template Examples:**

```python
"{{first_name}} {{last_name}}"              # John Smith
"{{last_name}}, {{first_name}}"             # Smith, John
"{{email_address}} | {{phone_number}}"      # john@ex.com | 555-0123
"{{street_address}}, {{city}}, {{state}}"   # 123 Main St, Springfield, IL
"[{{job_title}}] at {{company_name}}"       # [Manager] at Acme Corp
```

#### Regular Expression Provider Options

```python
# For: regular_expression
schema = [
    {
        "key_label": "regular_expression",
        "options": {
            "blank_percentage": 5,
            "format": "[A-Z]{3}-\\d{5}"  # Regex pattern
        }
    }
]
```

| Option     | Type | Effect                     |
| ---------- | ---- | -------------------------- |
| **format** | str  | Regular expression pattern |

**Common Regex Patterns:**

```python
"[A-Z]{3}-\\d{4}"           # 3 letters, dash, 4 digits: ABC-1234
"\\(\\d{3}\\) \\d{3}-\\d{4}" # Phone: (123) 456-7890
"[A-Z]{2}\\d{6}"            # 2 letters + 6 digits: AB123456
"[A-Za-z0-9]{8}-[A-Za-z0-9]{4}" # ID-like: aBcD1234-xYz0
"[0-9]{3}-[0-9]{2}-[0-9]{4}" # SSN: 123-45-6789
```

#### Password Provider Options

```python
# For: password
schema = [
    {
        "key_label": "password",
        "options": {
            "blank_percentage": 0,
            "min_length": 12,       # Minimum length
            "upper_num": 2,         # Uppercase letters required
            "lower_num": 2,         # Lowercase letters required
            "numbers_num": 2,       # Digits required
            "symbols_num": 2        # Special chars required
        }
    }
]
```

| Option          | Type | Default | Effect                  |
| --------------- | ---- | ------- | ----------------------- |
| **min_length**  | int  | 8       | Minimum password length |
| **upper_num**   | int  | 0       | Uppercase letters       |
| **lower_num**   | int  | 0       | Lowercase letters       |
| **numbers_num** | int  | 0       | Digits                  |
| **symbols_num** | int  | 0       | Special symbols         |

#### Money Provider Options

```python
# For: money
schema = [
    {
        "key_label": "money",
        "options": {
            "blank_percentage": 5,
            "min": 10,              # Minimum amount
            "max": 10000,           # Maximum amount
            "currency": "USD"       # Currency code or name
        }
    }
]
```

| Option       | Type  | Example                            | Effect          |
| ------------ | ----- | ---------------------------------- | --------------- |
| **min**      | float | `10`                               | Minimum amount  |
| **max**      | float | `10000`                            | Maximum amount  |
| **currency** | str   | `"USD"`, `"EUR"`, `"GBP"`, `"JPY"` | Currency format |

**Supported Currencies:**

```
USD  → $1,234.56
EUR  → €1.234,56
GBP  → £1,234.56
JPY  → ¥123,456
CHF  → CHF 1,234.56
CAD  → C$1,234.56
AUD  → A$1,234.56
INR  → ₹1,23,456
```

#### Custom List Provider Options

```python
# For: custom_list
schema = [
    {
        "key_label": "custom_list",
        "options": {
            "blank_percentage": 5,
            "values": ["Option A", "Option B", "Option C"]
            # OR: "values": "Option A,Option B,Option C"
        }
    }
]
```

| Option     | Type      | Format                    | Effect          |
| ---------- | --------- | ------------------------- | --------------- |
| **values** | list\|str | `["a", "b"]` or `"a,b,c"` | List of choices |

**Examples:**

```python
# As list
"values": ["Low", "Medium", "High", "Urgent"]

# As comma-separated string
"values": "Draft,Review,Approved,Published"

# With special characters
"values": ["Yes ✓", "No ✗", "Maybe ?"]
```

#### Lambda Provider Options

```python
# For: lambda (custom functions)
import random

schema = [
    {
        "key_label": "lambda",
        "options": {
            "blank_percentage": 5,
            "function": lambda: f"ID-{random.randint(100000, 999999)}"
        }
    }
]
```

| Option       | Type     | Effect                               |
| ------------ | -------- | ------------------------------------ |
| **function** | callable | Python function that returns a value |

**Examples:**

```python
# Simple random choice
"function": lambda: random.choice(["A", "B", "C"])

# Random number with prefix
"function": lambda: f"ORD-{random.randint(1000, 9999)}"

# Timestamp-based
"function": lambda: datetime.now().isoformat()

# Complex logic
"function": lambda: "Active" if random.random() > 0.5 else "Inactive"
```

---

## 22 Data Categories

Iki Data Generator organizes 700+ fields into 22 categories. Here's a quick overview and **complete reference** of all providers with detailed parameters and options.

---

## Complete Provider Reference

This section documents **all 700+ fields** organized by category, with detailed parameter information for each provider.

### 🧑 **Personal Category** (65+ providers)

Generate names, identity documents, demographics, and personal information.

#### Core Identity Providers

| Provider            | Description                    | Parameters                 | Example                   |
| ------------------- | ------------------------------ | -------------------------- | ------------------------- |
| `first_name`        | Random male/female first names | `blank_percentage` (0-100) | `"John"`                  |
| `first_name_male`   | Male-specific first names      | `blank_percentage`         | `"Michael"`               |
| `first_name_female` | Female-specific first names    | `blank_percentage`         | `"Sarah"`                 |
| `last_name`         | Random surnames                | `blank_percentage`         | `"Smith"`                 |
| `full_name`         | Complete first + last name     | `blank_percentage`         | `"John Smith"`            |
| `middle_name`       | Middle name generation         | `blank_percentage`         | `"James"`                 |
| `title`             | Professional titles            | `blank_percentage`         | `"Dr."`, `"Mr."`, `"Ms."` |
| `suffix`            | Name suffixes                  | `blank_percentage`         | `"Jr."`, `"Sr."`, `"III"` |
| `gender_binary`     | Binary gender (M/F)            | `blank_percentage`         | `"M"` or `"F"`            |
| `gender_spectrum`   | Extended gender options        | `blank_percentage`         | `"Non-binary"`, `"Other"` |
| `gender_abbrev`     | Gender abbreviations           | `blank_percentage`         | `"M"`, `"F"`, `"O"`       |
| `gender_facebook`   | Facebook gender options        | `blank_percentage`         | Various gender identities |

#### Identity & Document Providers

| Provider          | Description                  | Parameters         | Example                  |
| ----------------- | ---------------------------- | ------------------ | ------------------------ |
| `ssn`             | Social Security Numbers (US) | `blank_percentage` | `"123-45-6789"`          |
| `passport_number` | International passport IDs   | `blank_percentage` | `"123456789"`            |
| `nationality`     | Nationality/Country names    | `blank_percentage` | `"American"`, `"French"` |
| `language`        | Language names               | `blank_percentage` | `"English"`, `"Spanish"` |
| `language_code`   | ISO 639-1 language codes     | `blank_percentage` | `"en"`, `"es"`, `"fr"`   |

#### Demographics & Status Providers

| Provider            | Description             | Parameters         | Example                                    |
| ------------------- | ----------------------- | ------------------ | ------------------------------------------ |
| `age_group`         | Age ranges              | `blank_percentage` | `"18-25"`, `"35-45"`                       |
| `marital_status`    | Relationship status     | `blank_percentage` | `"Single"`, `"Married"`, `"Divorced"`      |
| `employment_status` | Job status              | `blank_percentage` | `"Employed"`, `"Unemployed"`, `"Retired"`  |
| `education_level`   | Educational attainment  | `blank_percentage` | `"High School"`, `"Bachelor's"`, `"PhD"`   |
| `military_rank`     | Military ranks          | `blank_percentage` | `"Private"`, `"Colonel"`                   |
| `life_stage`        | Life phases             | `blank_percentage` | `"Student"`, `"Professional"`, `"Retired"` |
| `relationship_type` | Relationship categories | `blank_percentage` | `"Spouse"`, `"Parent"`, `"Sibling"`        |

#### Appearance & Characteristics Providers

| Provider     | Description       | Parameters         | Example                          |
| ------------ | ----------------- | ------------------ | -------------------------------- |
| `hair_color` | Hair colors       | `blank_percentage` | `"Brown"`, `"Blonde"`, `"Black"` |
| `race`       | Ethnic background | `blank_percentage` | `"Caucasian"`, `"Asian"`         |
| `shirt_size` | Clothing sizes    | `blank_percentage` | `"S"`, `"M"`, `"L"`, `"XL"`      |
| `shoe_size`  | Shoe sizing       | `blank_percentage` | `"8"`, `"10.5"`                  |

#### Professional & Interest Providers

| Provider               | Description             | Parameters         | Example                            |
| ---------------------- | ----------------------- | ------------------ | ---------------------------------- |
| `job_title`            | Job positions           | `blank_percentage` | `"Software Engineer"`, `"Manager"` |
| `occupation`           | Occupational roles      | `blank_percentage` | `"Teacher"`, `"Nurse"`             |
| `role`                 | Generic role names      | `blank_percentage` | `"Admin"`, `"Viewer"`, `"Editor"`  |
| `industry`             | Business industries     | `blank_percentage` | `"Technology"`, `"Healthcare"`     |
| `department_corporate` | Corporate departments   | `blank_percentage` | `"Engineering"`, `"Sales"`         |
| `linkedin_skill`       | Professional skills     | `blank_percentage` | `"Python"`, `"Project Management"` |
| `company_name`         | Organization names      | `blank_percentage` | `"Acme Corp"`                      |
| `fake_company_name`    | Generated company names | `blank_percentage` | `"TechFlow Solutions"`             |
| `business_type`        | Business categories     | `blank_percentage` | `"SaaS"`, `"Manufacturing"`        |
| `organization_type`    | Organization structure  | `blank_percentage` | `"Startup"`, `"Enterprise"`        |
| `legal_entity`         | Legal entity types      | `blank_percentage` | `"LLC"`, `"Corporation"`           |
| `duns_number`          | D&B DUNS numbers        | `blank_percentage` | `"123456789"`                      |
| `ein`                  | Employer ID Numbers     | `blank_percentage` | `"12-3456789"`                     |
| `job_title`            | Job titles              | `blank_percentage` | `"Senior Manager"`                 |
| `salary_range`         | Salary bands            | `blank_percentage` | `"$50k-$75k"`                      |
| `income_level`         | Income categories       | `blank_percentage` | `"Middle"`, `"Upper"`              |
| `performance_rating`   | Performance scores      | `blank_percentage` | `"Excellent"`, `"Good"`            |
| `interview_stage`      | Hiring pipeline stages  | `blank_percentage` | `"Phone Screen"`, `"Offer"`        |

#### Lifestyle & Personal Info Providers

| Provider            | Description             | Parameters         | Example                         |
| ------------------- | ----------------------- | ------------------ | ------------------------------- |
| `hobby`             | Recreational activities | `blank_percentage` | `"Reading"`, `"Gaming"`         |
| `pet_type`          | Pet categories          | `blank_percentage` | `"Dog"`, `"Cat"`, `"Bird"`      |
| `pet_name`          | Pet names               | `blank_percentage` | `"Fluffy"`, `"Max"`             |
| `zodiac_sign`       | Zodiac signs            | `blank_percentage` | `"Aries"`, `"Taurus"`           |
| `religion`          | Religious affiliations  | `blank_percentage` | `"Christian"`, `"Muslim"`       |
| `mood`              | Emotional states        | `blank_percentage` | `"Happy"`, `"Anxious"`          |
| `personality_trait` | Character traits        | `blank_percentage` | `"Extroverted"`, `"Analytical"` |
| `daily_habit`       | Routine behaviors       | `blank_percentage` | `"Exercise"`, `"Reading"`       |
| `dream_job`         | Career aspirations      | `blank_percentage` | `"Travel Blogger"`              |
| `pronoun`           | Personal pronouns       | `blank_percentage` | `"he/him"`, `"she/her"`         |
| `quote`             | Motivational quotes     | `blank_percentage` | Random inspirational quotes     |
| `reaction`          | Emotional reactions     | `blank_percentage` | `"Excited"`, `"Surprised"`      |
| `project_status`    | Project statuses        | `blank_percentage` | `"Active"`, `"Completed"`       |

#### Event & Organization Providers

| Provider          | Description           | Parameters         | Example                     |
| ----------------- | --------------------- | ------------------ | --------------------------- |
| `conference_name` | Tech conference names | `blank_percentage` | `"TechConf 2024"`           |
| `event_type`      | Event categories      | `blank_percentage` | `"Conference"`, `"Webinar"` |
| `team_name`       | Team names            | `blank_percentage` | `"Team Alpha"`              |
| `buzzword`        | Corporate buzzwords   | `blank_percentage` | `"Synergy"`, `"Leverage"`   |
| `catch_praise`    | Compliments           | `blank_percentage` | `"Great job!"`              |
| `slogan`          | Marketing slogans     | `blank_percentage` | `"Think Different"`         |
| `hashtag`         | Social media tags     | `blank_percentage` | `"#ProductLaunch"`          |

---

### 💰 **Commerce Category** (65+ providers)

Generate e-commerce, retail, pricing, and product data.

#### Product & Catalog Providers

| Provider              | Description          | Parameters                       | Example                       |
| --------------------- | -------------------- | -------------------------------- | ----------------------------- |
| `product_name`        | Product titles       | `blank_percentage`               | `"Wireless Headphones"`       |
| `product_category`    | Product categories   | `blank_percentage`               | `"Electronics"`, `"Clothing"` |
| `product_subcategory` | Subcategories        | `blank_percentage`               | `"Audio"`, `"Footwear"`       |
| `product_description` | Product descriptions | `blank_percentage`               | Full product blurbs           |
| `product_price`       | Product prices       | `blank_percentage`, `min`, `max` | `"29.99"`                     |
| `sku`                 | Stock Keeping Units  | `blank_percentage`               | `"SKU-12345"`                 |

#### Payment & Financial Providers

| Provider             | Description               | Parameters                                   | Example                    |
| -------------------- | ------------------------- | -------------------------------------------- | -------------------------- |
| `credit_card_number` | CC numbers (valid format) | `blank_percentage`                           | `"4111-1111-1111-1111"`    |
| `credit_card_type`   | CC brand/type             | `blank_percentage`                           | `"Visa"`, `"MasterCard"`   |
| `money`              | Formatted currency        | `blank_percentage`, `min`, `max`, `currency` | `"$1,234.56"`              |
| `currency`           | Currency name             | `blank_percentage`                           | `"US Dollar"`, `"Euro"`    |
| `currency_code`      | ISO 4217 codes            | `blank_percentage`                           | `"USD"`, `"EUR"`           |
| `currency_symbol`    | Currency symbols          | `blank_percentage`                           | `"$"`, `"€"`, `"¥"`        |
| `iban`               | IBAN account numbers      | `blank_percentage`                           | `"DE89370400440532013000"` |
| `bban`               | BBAN numbers              | `blank_percentage`                           | `"0532013000"`             |

#### Order & Fulfillment Providers

| Provider               | Description           | Parameters         | Example                                        |
| ---------------------- | --------------------- | ------------------ | ---------------------------------------------- |
| `order_status`         | Order statuses        | `blank_percentage` | `"Pending"`, `"Shipped"`, `"Delivered"`        |
| `payment_status`       | Payment states        | `blank_percentage` | `"Paid"`, `"Pending"`, `"Failed"`              |
| `delivery_status`      | Delivery status       | `blank_percentage` | `"In Transit"`, `"Delivered"`                  |
| `shipment_status`      | Shipment states       | `blank_percentage` | `"Dispatched"`, `"Out for Delivery"`           |
| `payment_method`       | Payment types         | `blank_percentage` | `"Credit Card"`, `"PayPal"`, `"Bank Transfer"` |
| `shipping_method`      | Shipping options      | `blank_percentage` | `"Express"`, `"Standard"`                      |
| `postal_service`       | Postal services       | `blank_percentage` | `"USPS"`, `"FedEx"`, `"UPS"`                   |
| `delivery_time_window` | Delivery timeframes   | `blank_percentage` | `"9-12 AM"`, `"2-5 PM"`                        |
| `tracking_number`      | Shipment tracking     | `blank_percentage` | `"1234567890123"`                              |
| `return_reason`        | Return justifications | `blank_percentage` | `"Defective"`, `"Wrong Item"`                  |

#### Pricing & Promotion Providers

| Provider              | Description         | Parameters         | Example                            |
| --------------------- | ------------------- | ------------------ | ---------------------------------- |
| `discount_percentage` | Discount rates      | `blank_percentage` | `"10"`, `"25"`                     |
| `coupon_code`         | Promo codes         | `blank_percentage` | `"SAVE20"`                         |
| `promo_expiry_date`   | Promotion end dates | `blank_percentage` | `"12/31/2024"`                     |
| `subscription_plan`   | Subscription tiers  | `blank_percentage` | `"Basic"`, `"Pro"`, `"Enterprise"` |
| `loyalty_tier`        | Loyalty levels      | `blank_percentage` | `"Silver"`, `"Gold"`, `"Platinum"` |
| `membership_level`    | Membership grades   | `blank_percentage` | `"Standard"`, `"Premium"`          |
| `warranty_period`     | Warranty durations  | `blank_percentage` | `"1 Year"`, `"Lifetime"`           |

#### Inventory & Stock Providers

| Provider           | Description              | Parameters                       | Example                              |
| ------------------ | ------------------------ | -------------------------------- | ------------------------------------ |
| `inventory_status` | Stock statuses           | `blank_percentage`               | `"In Stock"`, `"Low Stock"`, `"Out"` |
| `stock_market`     | Market name              | `blank_percentage`               | `"NASDAQ"`, `"NYSE"`                 |
| `stock_name`       | Stock company names      | `blank_percentage`               | `"Apple Inc."`                       |
| `stock_symbol`     | Stock tickers            | `blank_percentage`               | `"AAPL"`, `"MSFT"`                   |
| `stock_sector`     | Market sectors           | `blank_percentage`               | `"Technology"`, `"Healthcare"`       |
| `stock_industry`   | Industry classifications | `blank_percentage`               | `"Computer Hardware"`                |
| `stock_market_cap` | Market cap ranges        | `blank_percentage`               | `"Large Cap"`, `"Small Cap"`         |
| `package_weight`   | Weight in shipments      | `blank_percentage`, `min`, `max` | `"2.5 lbs"`                          |
| `invoice_number`   | Invoice IDs              | `blank_percentage`               | `"INV-2024-001"`                     |

#### Retail & Merchandising Providers

| Provider            | Description           | Parameters         | Example                            |
| ------------------- | --------------------- | ------------------ | ---------------------------------- |
| `department_retail` | Retail departments    | `blank_percentage` | `"Men's Clothing"`, `"Home Goods"` |
| `restaurant_type`   | Restaurant categories | `blank_percentage` | `"Italian"`, `"Sushi"`             |
| `coffee_type`       | Coffee varieties      | `blank_percentage` | `"Espresso"`, `"Cappuccino"`       |
| `meal_type`         | Meal categories       | `blank_percentage` | `"Breakfast"`, `"Dinner"`          |
| `recipe_name`       | Recipe names          | `blank_percentage` | `"Spaghetti Carbonara"`            |
| `ingredient`        | Food ingredients      | `blank_percentage` | `"Tomato"`, `"Garlic"`             |
| `fabric_type`       | Material types        | `blank_percentage` | `"Cotton"`, `"Polyester"`          |
| `furniture_type`    | Furniture categories  | `blank_percentage` | `"Sofa"`, `"Dining Table"`         |
| `gem_stone`         | Precious stones       | `blank_percentage` | `"Diamond"`, `"Ruby"`              |
| `office_supply`     | Office items          | `blank_percentage` | `"Pen"`, `"Notebook"`              |
| `water_type`        | Water categories      | `blank_percentage` | `"Spring"`, `"Mineral"`            |

#### Customer & Review Providers

| Provider                       | Description           | Parameters         | Example                       |
| ------------------------------ | --------------------- | ------------------ | ----------------------------- |
| `review_text`                  | Customer reviews      | `blank_percentage` | Full review text              |
| `customer_feedback_score`      | Review ratings        | `blank_percentage` | `1-5` star ratings            |
| `recommendation_slot_position` | Rec positions         | `blank_percentage` | `"Top"`, `"Middle"`           |
| `price_sensitivity_level`      | Price sensitivity     | `blank_percentage` | `"High"`, `"Medium"`, `"Low"` |
| `click_depth`                  | User engagement depth | `blank_percentage` | `"Shallow"`, `"Deep"`         |

#### Analytics & Performance Providers

| Provider              | Description       | Parameters         | Example                             |
| --------------------- | ----------------- | ------------------ | ----------------------------------- |
| `sales_channel`       | Sales platforms   | `blank_percentage` | `"Amazon"`, `"Website"`, `"Retail"` |
| `bundle_type`         | Bundle categories | `blank_percentage` | `"Value Pack"`, `"Starter Kit"`     |
| `freight_mode`        | Shipping modes    | `blank_percentage` | `"Air"`, `"Sea"`, `"Rail"`          |
| `delivery_route_code` | Delivery routes   | `blank_percentage` | `"ROUTE-001"`                       |

---

### 💻 **IT/Technology Category** (100+ providers)

Generate programming, networking, software, and tech infrastructure data.

#### Programming & Development Providers

| Provider               | Description             | Parameters         | Example                            |
| ---------------------- | ----------------------- | ------------------ | ---------------------------------- |
| `programming_language` | Code languages          | `blank_percentage` | `"Python"`, `"JavaScript"`, `"Go"` |
| `software_framework`   | Development frameworks  | `blank_percentage` | `"Django"`, `"React"`, `"Spring"`  |
| `version_number`       | Software versions       | `blank_percentage` | `"1.2.3"`, `"3.0.0-beta"`          |
| `api_version`          | API versions            | `blank_percentage` | `"v1"`, `"v2.1"`                   |
| `api_endpoint_path`    | API paths               | `blank_percentage` | `"/api/users/profile"`             |
| `api_key`              | API authentication keys | `blank_percentage` | `"sk_test_123456..."`              |
| `http_method`          | HTTP verbs              | `blank_percentage` | `"GET"`, `"POST"`, `"PUT"`         |
| `http_status_code`     | HTTP response codes     | `blank_percentage` | `"200"`, `"404"`, `"500"`          |
| `git_commit_hash`      | Commit hashes           | `blank_percentage` | `"a1b2c3d4e5f6"`                   |

#### Networking & Infrastructure Providers

| Provider                | Description        | Parameters         | Example                    |
| ----------------------- | ------------------ | ------------------ | -------------------------- |
| `ip_address_v4`         | IPv4 addresses     | `blank_percentage` | `"192.168.1.1"`            |
| `ip_address_v6`         | IPv6 addresses     | `blank_percentage` | `"2001:0db8::1"`           |
| `ip_address_v4_cidr`    | IPv4 CIDR notation | `blank_percentage` | `"192.168.1.0/24"`         |
| `ip_address_v6_cidr`    | IPv6 CIDR notation | `blank_percentage` | `"2001:db8::/32"`          |
| `mac_address`           | MAC addresses      | `blank_percentage` | `"00:1A:2B:3C:4D:5E"`      |
| `port_number`           | Network ports      | `blank_percentage` | `"8080"`, `"5432"`         |
| `network_protocol`      | Network protocols  | `blank_percentage` | `"TCP"`, `"UDP"`, `"HTTP"` |
| `dns_record_type`       | DNS types          | `blank_percentage` | `"A"`, `"CNAME"`, `"MX"`   |
| `network_operator_code` | Carrier codes      | `blank_percentage` | Telecom operator IDs       |

#### Cloud & Infrastructure Providers

| Provider         | Description        | Parameters         | Example                      |
| ---------------- | ------------------ | ------------------ | ---------------------------- |
| `cloud_provider` | Cloud platforms    | `blank_percentage` | `"AWS"`, `"Azure"`, `"GCP"`  |
| `cloud_storage`  | Storage services   | `blank_percentage` | `"S3"`, `"Blob Storage"`     |
| `data_center`    | DC locations       | `blank_percentage` | `"us-east-1"`, `"eu-west-1"` |
| `server_name`    | Server identifiers | `blank_percentage` | `"server-prod-01"`           |
| `container_id`   | Container IDs      | `blank_percentage` | `"a1b2c3d4e5f6"`             |
| `docker_image`   | Docker images      | `blank_percentage` | `"python:3.11-slim"`         |
| `database_type`  | Database systems   | `blank_percentage` | `"PostgreSQL"`, `"MongoDB"`  |

#### Security & Authentication Providers

| Provider               | Description        | Parameters         | Example                              |
| ---------------------- | ------------------ | ------------------ | ------------------------------------ |
| `json_web_token`       | JWT tokens         | `blank_percentage` | Full JWT token                       |
| `md5`                  | MD5 hashes         | `blank_percentage` | `"5d41402abc4b2a76b9719d911017c592"` |
| `sha1`                 | SHA-1 hashes       | `blank_percentage` | SHA-1 hash strings                   |
| `sha256`               | SHA-256 hashes     | `blank_percentage` | SHA-256 hash strings                 |
| `encryption_algorithm` | Encryption methods | `blank_percentage` | `"AES-256"`, `"RSA-2048"`            |
| `permission_level`     | Access levels      | `blank_percentage` | `"Admin"`, `"User"`, `"Guest"`       |
| `password_strength`    | Password security  | `blank_percentage` | `"Weak"`, `"Medium"`, `"Strong"`     |
| `security_question`    | Security Q&A       | `blank_percentage` | `"What's your pet's name?"`          |
| `verification_code`    | 2FA/OTP codes      | `blank_percentage` | `"123456"`                           |

#### Devices & Hardware Providers

| Provider             | Description          | Parameters                       | Example                             |
| -------------------- | -------------------- | -------------------------------- | ----------------------------------- |
| `battery_level`      | Battery %            | `blank_percentage`, `min`, `max` | `"85"`                              |
| `storage_type`       | Storage media        | `blank_percentage`               | `"SSD"`, `"HDD"`                    |
| `memory_size`        | RAM/Memory           | `blank_percentage`               | `"16GB"`, `"512MB"`                 |
| `operating_system`   | OS names             | `blank_percentage`               | `"Windows"`, `"macOS"`, `"Linux"`   |
| `device_location`    | Device position      | `blank_percentage`               | `"Office"`, `"Home"`                |
| `firmware_version`   | Firmware versions    | `blank_percentage`               | `"1.2.3"`                           |
| `firmware_build`     | Firmware builds      | `blank_percentage`               | `"BUILD-12345"`                     |
| `power_state`        | Power status         | `blank_percentage`               | `"On"`, `"Sleeping"`, `"Off"`       |
| `power_source`       | Power input          | `blank_percentage`               | `"Battery"`, `"AC Adapter"`         |
| `resolution`         | Screen resolution    | `blank_percentage`               | `"1920x1080"`, `"2560x1600"`        |
| `screen_size`        | Display sizes        | `blank_percentage`               | `"15.6 inch"`, `"24 inch"`          |
| `browser`            | Web browsers         | `blank_percentage`               | `"Chrome"`, `"Firefox"`, `"Safari"` |
| `user_agent`         | User agent strings   | `blank_percentage`               | Full UA string                      |
| `laptop_brand`       | Laptop manufacturers | `blank_percentage`               | `"Dell"`, `"MacBook"`, `"HP"`       |
| `smart_device_brand` | IoT brands           | `blank_percentage`               | `"Amazon"`, `"Google"`, `"Apple"`   |
| `smart_device_type`  | IoT device types     | `blank_percentage`               | `"Smart Speaker"`, `"Thermostat"`   |
| `printer_type`       | Printer types        | `blank_percentage`               | `"Inkjet"`, `"Laser"`               |
| `form_factor`        | Device form          | `blank_percentage`               | `"Smartphone"`, `"Tablet"`          |

#### Web & Communication Providers

| Provider                | Description     | Parameters         | Example                               |
| ----------------------- | --------------- | ------------------ | ------------------------------------- |
| `email_address`         | Email addresses | `blank_percentage` | `"john.doe@example.com"`              |
| `username`              | User accounts   | `blank_percentage` | `"jdoe123"`, `"user_alpha"`           |
| `subject_line`          | Email subjects  | `blank_percentage` | `"Q4 Quarterly Review"`               |
| `slack_channel`         | Slack channels  | `blank_percentage` | `"#general"`, `"#dev-team"`           |
| `social_media_platform` | Social networks | `blank_percentage` | `"Twitter"`, `"LinkedIn"`, `"TikTok"` |
| `top_level_domain`      | Domain TLDs     | `blank_percentage` | `".com"`, `".org"`, `".io"`           |
| `wifi_ssid`             | WiFi networks   | `blank_percentage` | `"MyWiFi"`, `"CoffeeShop5G"`          |
| `wifi_standard`         | WiFi versions   | `blank_percentage` | `"WiFi 6"`, `"WiFi 5"`                |
| `wifi_band`             | WiFi bands      | `blank_percentage` | `"2.4GHz"`, `"5GHz"`                  |

#### Data & File Providers

| Provider         | Description         | Parameters         | Example                               |
| ---------------- | ------------------- | ------------------ | ------------------------------------- |
| `file_name`      | File names          | `blank_percentage` | `"document.pdf"`, `"image.jpg"`       |
| `file_extension` | File types          | `blank_percentage` | `".pdf"`, `".csv"`, `".json"`         |
| `file_size`      | File sizes          | `blank_percentage` | `"2.5 MB"`, `"1.2 GB"`                |
| `mime_type`      | MIME types          | `blank_percentage` | `"application/json"`, `"image/png"`   |
| `document_type`  | Document categories | `blank_percentage` | `"Report"`, `"Invoice"`, `"Contract"` |

#### Monitoring & Diagnostics Providers

| Provider            | Description          | Parameters                       | Example                        |
| ------------------- | -------------------- | -------------------------------- | ------------------------------ |
| `log_level`         | Log severity         | `blank_percentage`               | `"DEBUG"`, `"INFO"`, `"ERROR"` |
| `error_message`     | Error text           | `blank_percentage`               | `"Connection timeout"`         |
| `incident_type`     | Incident categories  | `blank_percentage`               | `"Outage"`, `"Degradation"`    |
| `uptime_percentage` | Service availability | `blank_percentage`               | `"99.9"`                       |
| `response_time`     | Latency              | `blank_percentage`, `min`, `max` | `"125ms"`, `"3.5s"`            |

#### Analytics & Engagement Providers

| Provider              | Description       | Parameters                       | Example                         |
| --------------------- | ----------------- | -------------------------------- | ------------------------------- |
| `feature_usage_event` | Usage tracking    | `blank_percentage`               | `"click_button"`, `"view_page"` |
| `engagement_level`    | User engagement   | `blank_percentage`               | `"High"`, `"Medium"`, `"Low"`   |
| `user_cohort`         | Cohort segments   | `blank_percentage`               | `"Early Adopter"`, `"Laggard"`  |
| `churn_risk_score`    | Churn probability | `blank_percentage`, `min`, `max` | `"0.75"`                        |
| `notification_type`   | Alert types       | `blank_percentage`               | `"Email"`, `"Push"`, `"SMS"`    |

---

### 🏥 **Healthcare Category** (60+ providers)

Generate medical, pharmaceutical, hospital, and health insurance data.

#### Patient & Diagnosis Providers

| Provider            | Description           | Parameters         | Example                         |
| ------------------- | --------------------- | ------------------ | ------------------------------- |
| `blood_type`        | Blood types           | `blank_percentage` | `"O+"`, `"AB-"`                 |
| `disease_name`      | Diseases              | `blank_percentage` | `"Type 2 Diabetes"`, `"Asthma"` |
| `symptom`           | Symptoms              | `blank_percentage` | `"Fever"`, `"Cough"`            |
| `disability_type`   | Disability categories | `blank_percentage` | `"Mobility"`, `"Hearing"`       |
| `medication_name`   | Drug names            | `blank_percentage` | `"Aspirin"`, `"Metformin"`      |
| `drug_name_generic` | Generic drug names    | `blank_percentage` | Chemical names                  |
| `drug_name_brand`   | Brand drug names      | `blank_percentage` | `"Advil"`, `"Tylenol"`          |
| `drug_company`      | Pharma companies      | `blank_percentage` | `"Pfizer"`, `"Merck"`           |
| `fda_ndc_code`      | FDA codes             | `blank_percentage` | `"0002-1234-01"`                |

#### Medical Coding Providers

| Provider               | Description          | Parameters         | Example                     |
| ---------------------- | -------------------- | ------------------ | --------------------------- |
| `icd10_diagnosis_code` | ICD-10 diagnosis     | `blank_percentage` | `"E11.9"` (Type 2 diabetes) |
| `icd10_dx_desc_short`  | ICD-10 short desc    | `blank_percentage` | `"Type 2 diabetes"`         |
| `icd10_dx_desc_long`   | ICD-10 long desc     | `blank_percentage` | Full description            |
| `icd10_procedure_code` | ICD-10 procedures    | `blank_percentage` | `"0DB68ZX"`                 |
| `icd9_diagnosis_code`  | ICD-9 diagnosis      | `blank_percentage` | `"250.00"`                  |
| `icd9_dx_desc_short`   | ICD-9 short desc     | `blank_percentage` | Short description           |
| `icd9_proc_desc_long`  | ICD-9 long proc desc | `blank_percentage` | Full description            |
| `hcpcs_code`           | HCPCS codes          | `blank_percentage` | `"E1390"`                   |
| `hcpcs_name`           | HCPCS descriptions   | `blank_percentage` | `"Ultrasonic cleaner"`      |

#### Hospital & Provider Providers

| Provider                  | Description            | Parameters         | Example                         |
| ------------------------- | ---------------------- | ------------------ | ------------------------------- |
| `hospital_name`           | Hospital names         | `blank_percentage` | `"General Medical Center"`      |
| `hospital_department`     | Hospital departments   | `blank_percentage` | `"Cardiology"`, `"Emergency"`   |
| `hospital_npi`            | NPI numbers            | `blank_percentage` | Provider ID numbers             |
| `hospital_city`           | Hospital location city | `blank_percentage` | City name                       |
| `hospital_state`          | Hospital state         | `blank_percentage` | State abbreviation              |
| `hospital_street_address` | Hospital address       | `blank_percentage` | Full street address             |
| `hospital_postal_code`    | Hospital ZIP           | `blank_percentage` | Postal code                     |
| `pharmacy_name`           | Pharmacy names         | `blank_percentage` | `"CVS Pharmacy"`, `"Walgreens"` |

#### Vital Signs & Lab Data Providers

| Provider                  | Description        | Parameters                       | Example                       |
| ------------------------- | ------------------ | -------------------------------- | ----------------------------- |
| `blood_pressure_reading`  | BP measurements    | `blank_percentage`, `min`, `max` | `"120/80"`                    |
| `blood_pressure_category` | BP classifications | `blank_percentage`               | `"Normal"`, `"Elevated"`      |
| `heart_rate`              | Heart rate (BPM)   | `blank_percentage`, `min`, `max` | `"72"`                        |
| `lab_test`                | Lab test names     | `blank_percentage`               | `"Complete Blood Count"`      |
| `lab_test_type`           | Lab test category  | `blank_percentage`               | `"Hematology"`, `"Chemistry"` |
| `lab_result_value`        | Test results       | `blank_percentage`, `min`, `max` | Numeric values                |
| `triage_level`            | ER priority        | `blank_percentage`               | `"Level 1"`, `"Level 5"`      |

#### Treatment & Care Providers

| Provider             | Description         | Parameters         | Example                      |
| -------------------- | ------------------- | ------------------ | ---------------------------- |
| `medication_dosage`  | Dosage amounts      | `blank_percentage` | `"500mg"`, `"10ml"`          |
| `appointment_status` | Appointment states  | `blank_percentage` | `"Scheduled"`, `"Completed"` |
| `medical_specialty`  | Medical specialties | `blank_percentage` | `"Oncology"`, `"Pediatrics"` |
| `medical_device_id`  | Device identifiers  | `blank_percentage` | Device serial numbers        |
| `prescription_id`    | Prescription IDs    | `blank_percentage` | `"RX-2024-001"`              |

#### Lifestyle & Wellness Providers

| Provider                  | Description             | Parameters         | Example                                |
| ------------------------- | ----------------------- | ------------------ | -------------------------------------- |
| `diet_type`               | Diet categories         | `blank_percentage` | `"Keto"`, `"Vegan"`                    |
| `dietary_restriction`     | Food restrictions       | `blank_percentage` | `"Gluten-Free"`, `"Nut Allergy"`       |
| `exercise_type`           | Exercise categories     | `blank_percentage` | `"Cardio"`, `"Weight Training"`        |
| `workout_duration`        | Exercise time           | `blank_percentage` | `"30 minutes"`, `"1 hour"`             |
| `mental_health_condition` | Mental health diagnoses | `blank_percentage` | `"Anxiety"`, `"Depression"`            |
| `vaccination_status`      | Vaccination states      | `blank_percentage` | `"Fully Vaccinated"`, `"Unvaccinated"` |
| `vaccination_type`        | Vaccine types           | `blank_percentage` | `"COVID-19"`, `"Flu"`                  |

#### Nutritional & Allergy Providers

| Provider         | Description       | Parameters                       | Example                    |
| ---------------- | ----------------- | -------------------------------- | -------------------------- |
| `allergy`        | Medical allergies | `blank_percentage`               | `"Peanuts"`, `"Latex"`     |
| `food_allergy`   | Food allergies    | `blank_percentage`               | `"Shellfish"`, `"Eggs"`    |
| `allergy_flag`   | Allergy status    | `blank_percentage`               | `"No Known Allergies"`     |
| `macro_nutrient` | Macronutrients    | `blank_percentage`               | `"Protein"`, `"Carbs"`     |
| `nutrient`       | Vitamins/minerals | `blank_percentage`               | `"Calcium"`, `"Vitamin D"` |
| `vitamin_name`   | Specific vitamins | `blank_percentage`               | `"B12"`, `"Folic Acid"`    |
| `calorie_count`  | Calorie amounts   | `blank_percentage`, `min`, `max` | `"2000"`                   |
| `serving_size`   | Portion sizes     | `blank_percentage`               | `"1 cup"`, `"100g"`        |
| `meal_rating`    | Food satisfaction | `blank_percentage`               | `1-5` ratings              |

#### Insurance & Administrative Providers

| Provider                  | Description          | Parameters         | Example                   |
| ------------------------- | -------------------- | ------------------ | ------------------------- |
| `health_insurance_plan`   | Insurance types      | `blank_percentage` | `"HMO"`, `"PPO"`          |
| `insurance_provider`      | Insurance companies  | `blank_percentage` | `"Aetna"`, `"Blue Cross"` |
| `medicare_beneficiary_id` | Medicare IDs         | `blank_percentage` | Medicare numbers          |
| `nhs_number`              | NHS patient IDs (UK) | `blank_percentage` | NHS numbers               |

#### Additional Providers

| Provider         | Description      | Parameters         | Example                   |
| ---------------- | ---------------- | ------------------ | ------------------------- |
| `body_part`      | Anatomical parts | `blank_percentage` | `"Heart"`, `"Liver"`      |
| `emergency_type` | Emergency types  | `blank_percentage` | `"Trauma"`, `"Cardiac"`   |
| `hormone`        | Hormones         | `blank_percentage` | `"Insulin"`, `"Cortisol"` |
| `organ`          | Organs           | `blank_percentage` | `"Kidney"`, `"Pancreas"`  |
| `pain_level`     | Pain intensity   | `blank_percentage` | `"1-10"` scale            |
| `chromosome`     | Chromosomes      | `blank_percentage` | `"X"`, `"Y"`, `"22"`      |

---

## 📊 **Advanced Category** (8 providers)

Advanced data generation with templates, regex, lambdas, and custom logic.

| Provider             | Description                     | Parameters                                | Example                                |
| -------------------- | ------------------------------- | ----------------------------------------- | -------------------------------------- |
| `template`           | Combine fields with `{{field}}` | `template`, `schema_labels`               | `"Hello {{first_name}} {{last_name}}"` |
| `regular_expression` | Generate from regex patterns    | `format`                                  | `"[A-Z]{3}-\\d{4}"` → `"ABC-1234"`     |
| `custom_list`        | Pick from a list                | `values` (list or comma-separated string) | `["Active", "Inactive", "Pending"]`    |
| `lambda`             | Custom Python function          | `function`                                | Custom generation logic                |
| `json_array`         | Generate JSON arrays            | `blank_percentage`                        | Array of objects                       |
| `url`                | Generate URLs                   | `blank_percentage`                        | Valid URL strings                      |
| `digit_sequence`     | Random digit strings            | `blank_percentage`, `length`              | `"1234567890"`                         |
| `character_sequence` | Random characters               | `blank_percentage`, `length`              | `"AbCdEfGhIj"`                         |
| `naughty_string`     | Special/edge case strings       | `blank_percentage`                        | SQL injection, Unicode, etc.           |

---

## 🤖 **AI/ML Category** (30+ providers)

Generate machine learning, model metrics, and AI infrastructure data.

| Provider                      | Description               | Parameters                       | Example                                       |
| ----------------------------- | ------------------------- | -------------------------------- | --------------------------------------------- |
| `model_type`                  | ML model types            | `blank_percentage`               | `"Regression"`, `"Classification"`            |
| `model_framework`             | ML frameworks             | `blank_percentage`               | `"TensorFlow"`, `"PyTorch"`, `"Scikit-learn"` |
| `model_task`                  | ML task types             | `blank_percentage`               | `"NLP"`, `"Computer Vision"`, `"Forecasting"` |
| `model_version`               | Model versions            | `blank_percentage`               | `"1.0.0"`, `"2.1.3-rc1"`                      |
| `model_owner`                 | Model creators            | `blank_percentage`               | Team/person names                             |
| `model_latency`               | Inference time            | `blank_percentage`, `min`, `max` | `"125ms"`, `"2.5s"`                           |
| `model_confidence`            | Prediction confidence     | `blank_percentage`, `min`, `max` | `"0.95"`, `"85%"`                             |
| `inference_result`            | Prediction outputs        | `blank_percentage`               | Class labels or values                        |
| `inference_endpoint`          | API endpoints             | `blank_percentage`               | `/api/v1/predict`                             |
| `model_input_format`          | Input data formats        | `blank_percentage`               | `"JSON"`, `"CSV"`, `"Binary"`                 |
| `model_output_format`         | Output formats            | `blank_percentage`               | `"JSON"`, `"Tensor"`                          |
| `model_training_dataset`      | Training data name        | `blank_percentage`               | Dataset identifiers                           |
| `model_lifecycle_stage`       | Model stages              | `blank_percentage`               | `"Development"`, `"Production"`               |
| `model_explainability_method` | Explainability techniques | `blank_percentage`               | `"SHAP"`, `"LIME"`, `"Attention"`             |
| `model_deployment_env`        | Deployment targets        | `blank_percentage`               | `"AWS"`, `"On-Premise"`, `"Edge"`             |
| `cpu_utilization`             | CPU %                     | `blank_percentage`, `min`, `max` | `"45.2"`                                      |
| `gpu_utilization`             | GPU %                     | `blank_percentage`, `min`, `max` | `"78.5"`                                      |
| `memory_footprint`            | Memory usage              | `blank_percentage`               | `"2.5GB"`, `"512MB"`                          |
| `data_drift_score`            | Data drift metric         | `blank_percentage`, `min`, `max` | `"0.12"` (0-1 scale)                          |
| `concept_drift_status`        | Concept drift state       | `blank_percentage`               | `"Stable"`, `"Drifting"`                      |
| `retraining_frequency`        | Update schedules          | `blank_percentage`               | `"Daily"`, `"Weekly"`                         |
| `compute_precision`           | Numeric precision         | `blank_percentage`               | `"float32"`, `"float64"`                      |

---

## 🌍 **Location Category** (35+ providers)

Generate geographic, address, and location data.

| Provider            | Description            | Parameters                       | Example                                     |
| ------------------- | ---------------------- | -------------------------------- | ------------------------------------------- |
| `country`           | Country names          | `blank_percentage`               | `"United States"`, `"France"`               |
| `country_code`      | ISO 3166 country codes | `blank_percentage`               | `"US"`, `"FR"`, `"JP"`                      |
| `state`             | State/Province names   | `blank_percentage`               | `"California"`, `"Texas"`                   |
| `state_abbrev`      | State abbreviations    | `blank_percentage`               | `"CA"`, `"TX"`, `"NY"`                      |
| `city`              | City names             | `blank_percentage`               | `"New York"`, `"Los Angeles"`               |
| `street_address`    | Full street addresses  | `blank_percentage`               | `"123 Main St, Apt 4B"`                     |
| `street_name`       | Street names           | `blank_percentage`               | `"Main Street"`, `"Park Avenue"`            |
| `street_number`     | House/Building numbers | `blank_percentage`, `min`, `max` | `"123"`, `"4567"`                           |
| `street_type`       | Street designators     | `blank_percentage`               | `"Street"`, `"Avenue"`, `"Boulevard"`       |
| `street_suffix`     | Address suffixes       | `blank_percentage`               | `"Apt"`, `"Suite"`, `"Floor"`               |
| `postal_code`       | ZIP/Postal codes       | `blank_percentage`               | `"10001"`, `"SW1A1AA"`                      |
| `latitude`          | Geographic latitude    | `blank_percentage`, `min`, `max` | `"40.7128"`                                 |
| `longitude`         | Geographic longitude   | `blank_percentage`, `min`, `max` | `"-74.0060"`                                |
| `time_zone`         | Time zone names        | `blank_percentage`               | `"America/New_York"`, `"Europe/London"`     |
| `timezone_abbrev`   | Timezone abbreviations | `blank_percentage`               | `"EST"`, `"PST"`, `"GMT"`                   |
| `timezone_offset`   | UTC offsets            | `blank_percentage`               | `"+5:30"`, `"-8:00"`                        |
| `continent`         | Continent names        | `blank_percentage`               | `"North America"`, `"Europe"`               |
| `subregion`         | Geographic subregions  | `blank_percentage`               | `"Northern Europe"`, `"Sub-Saharan Africa"` |
| `compass_direction` | Cardinal directions    | `blank_percentage`               | `"North"`, `"Northeast"`                    |
| `elevation`         | Altitude/elevation     | `blank_percentage`, `min`, `max` | `"1234m"`, `"5000ft"`                       |
| `phone`             | Phone numbers          | `blank_percentage`               | `"555-123-4567"`                            |

---

### 📚 **Education Category** (11 providers)

Generate academic and educational data.

| Provider           | Description                 | Parameters                       | Example                               |
| ------------------ | --------------------------- | -------------------------------- | ------------------------------------- |
| `university_name`  | University names            | `blank_percentage`               | `"MIT"`, `"Stanford"`                 |
| `degree`           | Degree types                | `blank_percentage`               | `"Bachelor's"`, `"Master's"`, `"PhD"` |
| `college_major`    | Academic majors             | `blank_percentage`               | `"Computer Science"`, `"Biology"`     |
| `academic_subject` | Subject areas               | `blank_percentage`               | `"Mathematics"`, `"Literature"`       |
| `school_type`      | School categories           | `blank_percentage`               | `"Public"`, `"Private"`, `"Charter"`  |
| `grade_level`      | Grade/Class levels          | `blank_percentage`               | `"Freshman"`, `"Junior"`, `"Senior"`  |
| `semester`         | Academic terms              | `blank_percentage`               | `"Spring 2024"`, `"Fall 2023"`        |
| `gpa`              | Grade point average         | `blank_percentage`, `min`, `max` | `"3.85"` (0-4.0 scale)                |
| `classroom_number` | Room numbers                | `blank_percentage`               | `"101"`, `"A-204"`                    |
| `certification`    | Professional certifications | `blank_percentage`               | `"AWS Certified"`, `"CPA"`            |
| `qualification`    | Job qualifications          | `blank_percentage`               | `"Bachelor's Required"`               |

---

### 🏗️ **Construction Category** (7 providers)

Generate construction, building, and trades data.

| Provider                            | Description         | Parameters         | Example                                         |
| ----------------------------------- | ------------------- | ------------------ | ----------------------------------------------- |
| `building_type`                     | Building categories | `blank_percentage` | `"Residential"`, `"Commercial"`, `"Industrial"` |
| `construction_material`             | Building materials  | `blank_percentage` | `"Steel"`, `"Concrete"`, `"Wood"`               |
| `construction_trade`                | Trade occupations   | `blank_percentage` | `"Electrician"`, `"Plumber"`, `"Carpenter"`     |
| `construction_role`                 | Construction roles  | `blank_percentage` | `"Foreman"`, `"Safety Officer"`                 |
| `tool_type`                         | Tool categories     | `blank_percentage` | `"Power Drill"`, `"Hammer"`                     |
| `construction_heavy_equipment`      | Large machinery     | `blank_percentage` | `"Excavator"`, `"Crane"`                        |
| `construction_subcontract_category` | Subcontractor types | `blank_percentage` | `"Concrete"`, `"Electrical"`                    |
| `construction_standard_cost_code`   | Cost codes          | `blank_percentage` | Standard construction codes                     |

---

### 🚗 **Automotive Category** (12 providers)

Generate vehicle and automotive data.

| Provider                | Description           | Parameters                       | Example                                |
| ----------------------- | --------------------- | -------------------------------- | -------------------------------------- |
| `car_make`              | Vehicle manufacturers | `blank_percentage`               | `"Toyota"`, `"Ford"`, `"BMW"`          |
| `car_model`             | Vehicle models        | `blank_percentage`               | `"Camry"`, `"Mustang"`, `"3 Series"`   |
| `car_base_model`        | Base model names      | `blank_percentage`               | `"SE"`, `"LX"`, `"Standard"`           |
| `car_model_year`        | Model years           | `blank_percentage`, `min`, `max` | `"2024"`, `"2020"`                     |
| `car_vin`               | Vehicle ID Numbers    | `blank_percentage`               | `"1HGBH41JXMN109186"`                  |
| `license_plate`         | License plate numbers | `blank_percentage`               | `"ABC-1234"`, `"XYZ-9876"`             |
| `vehicle_type`          | Vehicle categories    | `blank_percentage`               | `"Sedan"`, `"SUV"`, `"Truck"`          |
| `engine_type`           | Engine configurations | `blank_percentage`               | `"V6"`, `"Inline-4"`, `"Electric"`     |
| `fuel_type`             | Fuel types            | `blank_percentage`               | `"Gasoline"`, `"Diesel"`, `"Electric"` |
| `transmission_type`     | Transmission types    | `blank_percentage`               | `"Automatic"`, `"Manual"`, `"CVT"`     |
| `gas_type`              | Gas grades            | `blank_percentage`               | `"Regular"`, `"Premium"`, `"Diesel"`   |
| `driver_license_number` | License numbers       | `blank_percentage`               | Alphanumeric license IDs               |

---

### 🎮 **Gaming Category** (13 providers)

Generate gaming, entertainment, and player data.

| Provider                   | Description         | Parameters                       | Example                                  |
| -------------------------- | ------------------- | -------------------------------- | ---------------------------------------- |
| `game_genre`               | Game categories     | `blank_percentage`               | `"RPG"`, `"FPS"`, `"Strategy"`           |
| `console_platform`         | Gaming platforms    | `blank_percentage`               | `"PS5"`, `"Xbox Series X"`, `"PC"`       |
| `avatar_class`             | Character classes   | `blank_percentage`               | `"Warrior"`, `"Mage"`, `"Rogue"`         |
| `player_role`              | In-game roles       | `blank_percentage`               | `"Tank"`, `"DPS"`, `"Support"`           |
| `guild_name`               | Clan/Guild names    | `blank_percentage`               | `"Dragon Slayers"`, `"Shadow Syndicate"` |
| `quest_completion_rate`    | Quest progress %    | `blank_percentage`, `min`, `max` | `"85%"`                                  |
| `achievement_title`        | Achievement names   | `blank_percentage`               | `"Monster Slayer"`, `"Rich in Gold"`     |
| `badge`                    | Badge names         | `blank_percentage`               | Custom badge titles                      |
| `skill_level`              | Player skill tiers  | `blank_percentage`               | `"Novice"`, `"Expert"`, `"Legendary"`    |
| `leaderboard_rank`         | Ranking position    | `blank_percentage`, `min`, `max` | `"42"`, `"1"`                            |
| `in_game_currency_balance` | Virtual money       | `blank_percentage`, `min`, `max` | `"50000 Gold"`                           |
| `match_result`             | Game outcomes       | `blank_percentage`               | `"Win"`, `"Loss"`, `"Draw"`              |
| `session_outcome`          | Play session result | `blank_percentage`               | `"Victory"`, `"Defeat"`                  |

---

### 🎬 **Entertainment Category** (10+ providers)

Generate movie, book, music, and media data.

| Provider           | Description         | Parameters         | Example                                 |
| ------------------ | ------------------- | ------------------ | --------------------------------------- |
| `movie_title`      | Film titles         | `blank_percentage` | `"The Matrix"`, `"Inception"`           |
| `movie_genre`      | Film categories     | `blank_percentage` | `"Action"`, `"Drama"`, `"Comedy"`       |
| `book_title`       | Book names          | `blank_percentage` | `"1984"`, `"To Kill a Mockingbird"`     |
| `author_name`      | Author names        | `blank_percentage` | `"George Orwell"`, `"Jane Austen"`      |
| `song_title`       | Song names          | `blank_percentage` | `"Bohemian Rhapsody"`                   |
| `music_genre`      | Music categories    | `blank_percentage` | `"Rock"`, `"Hip-Hop"`, `"Jazz"`         |
| `artist_name`      | Artist/Band names   | `blank_percentage` | `"The Beatles"`, `"Beyoncé"`            |
| `album_name`       | Album titles        | `blank_percentage` | `"Abbey Road"`, `"Thriller"`            |
| `instrument_name`  | Musical instruments | `blank_percentage` | `"Guitar"`, `"Piano"`, `"Drums"`        |
| `video_game_title` | Video game names    | `blank_percentage` | `"The Legend of Zelda"`, `"Elden Ring"` |

---

### 💱 **Cryptocurrency Category** (7 providers)

Generate blockchain and cryptocurrency data.

| Provider                 | Description              | Parameters         | Example                                        |
| ------------------------ | ------------------------ | ------------------ | ---------------------------------------------- |
| `cryptocurrency_name`    | Crypto names             | `blank_percentage` | `"Bitcoin"`, `"Ethereum"`                      |
| `cryptocurrency_symbol`  | Ticker symbols           | `blank_percentage` | `"BTC"`, `"ETH"`, `"ADA"`                      |
| `bitcoin_address`        | Bitcoin wallets          | `blank_percentage` | `"1A1z..."`                                    |
| `ethereum_address`       | Ethereum wallets         | `blank_percentage` | `"0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"` |
| `cryptocurrency_address` | Generic crypto addresses | `blank_percentage` | Cryptocurrency wallet addresses                |
| `nft_token_id`           | NFT identifiers          | `blank_percentage` | Token IDs                                      |
| `tezos_*` (6 providers)  | Tezos blockchain data    | `blank_percentage` | Tezos-specific addresses/data                  |

---

### ⚖️ **Legal Category** (17 providers)

Generate legal and compliance data.

| Provider                  | Description         | Parameters         | Example                                        |
| ------------------------- | ------------------- | ------------------ | ---------------------------------------------- |
| `legal_jurisdiction`      | Legal territories   | `blank_percentage` | `"New York"`, `"California"`                   |
| `court_level`             | Court hierarchies   | `blank_percentage` | `"District Court"`, `"Supreme Court"`          |
| `contract_type`           | Contract categories | `blank_percentage` | `"NDA"`, `"Employment"`, `"Service"`           |
| `legal_filing_type`       | Filing categories   | `blank_percentage` | `"Lawsuit"`, `"Patent"`, `"Trademark"`         |
| `law_type`                | Area of law         | `blank_percentage` | `"Civil"`, `"Criminal"`, `"Corporate"`         |
| `crime_type`              | Crime categories    | `blank_percentage` | `"Theft"`, `"Fraud"`, `"Assault"`              |
| `verdict`                 | Trial outcomes      | `blank_percentage` | `"Guilty"`, `"Not Guilty"`, `"Acquitted"`      |
| `appeal_status`           | Appeal states       | `blank_percentage` | `"Pending"`, `"Upheld"`, `"Reversed"`          |
| `bail_status`             | Bail decisions      | `blank_percentage` | `"Released"`, `"Denied"`, `"Held"`             |
| `case_reference_number`   | Case IDs            | `blank_percentage` | `"CASE-2024-001"`                              |
| `evidence_type`           | Evidence categories | `blank_percentage` | `"Physical"`, `"Testimonial"`, `"Documentary"` |
| `penalty_type`            | Penalty categories  | `blank_percentage` | `"Fine"`, `"Imprisonment"`, `"Probation"`      |
| `regulatory_agency`       | Regulatory bodies   | `blank_percentage` | `"SEC"`, `"EPA"`, `"FDA"`                      |
| `legal_representation`    | Legal roles         | `blank_percentage` | `"Plaintiff Attorney"`, `"Defendant"`          |
| `legislation_status`      | Bill statuses       | `blank_percentage` | `"Proposed"`, `"Passed"`, `"Vetoed"`           |
| `legal_compliance_status` | Compliance states   | `blank_percentage` | `"Compliant"`, `"Non-Compliant"`               |
| `legal_fee_category`      | Fee structures      | `blank_percentage` | `"Hourly"`, `"Contingency"`                    |
| `notary_status`           | Notarization states | `blank_percentage` | `"Notarized"`, `"Pending"`                     |

---

### 🌿 **Nature Category** (10+ providers)

Generate natural world and environmental data.

| Provider            | Description        | Parameters                       | Example                                  |
| ------------------- | ------------------ | -------------------------------- | ---------------------------------------- |
| `animal_name`       | Animal names       | `blank_percentage`               | `"Lion"`, `"Elephant"`, `"Dolphin"`      |
| `plant_name`        | Plant names        | `blank_percentage`               | `"Rose"`, `"Oak"`, `"Bamboo"`            |
| `tree_name`         | Tree names         | `blank_percentage`               | `"Maple"`, `"Pine"`, `"Birch"`           |
| `flower_name`       | Flower names       | `blank_percentage`               | `"Sunflower"`, `"Tulip"`, `"Daisy"`      |
| `weather_condition` | Weather types      | `blank_percentage`               | `"Sunny"`, `"Rainy"`, `"Snowy"`          |
| `season`            | Seasons            | `blank_percentage`               | `"Spring"`, `"Summer"`, `"Fall"`         |
| `biome`             | Ecosystem types    | `blank_percentage`               | `"Rainforest"`, `"Desert"`, `"Tundra"`   |
| `temperature`       | Temperature values | `blank_percentage`, `min`, `max` | `"72°F"`, `"22°C"`                       |
| `noise_level`       | Sound levels       | `blank_percentage`               | `"45 dB"`, `"100 dB"`                    |
| `noise_category`    | Noise types        | `blank_percentage`               | `"Traffic"`, `"Industrial"`, `"Nature"`  |
| `noise_source`      | Sound sources      | `blank_percentage`               | `"Traffic"`, `"Construction"`, `"Music"` |

---

### 🔷 **Political Category** (5+ providers)

Generate political and government data.

| Provider               | Description          | Parameters         | Example                                       |
| ---------------------- | -------------------- | ------------------ | --------------------------------------------- |
| `political_party`      | Political parties    | `blank_percentage` | `"Democratic"`, `"Republican"`                |
| `political_ideology`   | Political viewpoints | `blank_percentage` | `"Liberal"`, `"Conservative"`, `"Moderate"`   |
| `government_structure` | Govt types           | `blank_percentage` | `"Democracy"`, `"Monarchy"`, `"Dictatorship"` |
| `election_type`        | Election categories  | `blank_percentage` | `"General"`, `"Primary"`, `"Recall"`          |
| `diplomatic_title`     | Diplomatic ranks     | `blank_percentage` | `"Ambassador"`, `"Envoy"`                     |

---

### 🎵 **Music Category** (5+ providers)

Generate music and audio data.

| Provider                                                                 | Description | Parameters         | Example                         |
| ------------------------------------------------------------------------ | ----------- | ------------------ | ------------------------------- |
| `music_production_software`                                              | DAW names   | `blank_percentage` | `"Ableton Live"`, `"Pro Tools"` |
| Multiple music providers from Entertainment category are also accessible |

---

### 🌐 **Marketing/Media Category** (7+ providers)

Generate marketing, analytics, and content data.

| Provider                | Description         | Parameters         | Example                                      |
| ----------------------- | ------------------- | ------------------ | -------------------------------------------- |
| `campaign_name`         | Marketing campaigns | `blank_percentage` | `"Summer Sale 2024"`                         |
| `marketing_channel`     | Marketing platforms | `blank_percentage` | `"Email"`, `"Social Media"`, `"Paid Search"` |
| `content_type`          | Content categories  | `blank_percentage` | `"Blog Post"`, `"Video"`, `"Infographic"`    |
| `target_audience`       | Audience segments   | `blank_percentage` | `"Tech Enthusiasts"`, `"Millennials"`        |
| `social_media_platform` | Social networks     | `blank_percentage` | `"Facebook"`, `"Instagram"`, `"TikTok"`      |
| `analytics_metric`      | Measurement types   | `blank_percentage` | `"CTR"`, `"CAC"`, `"LTV"`                    |

---

### 🏦 **Finance Category** (40+ providers)

Generate banking, investment, and financial data.

| Provider                 | Description            | Parameters                       | Example                                      |
| ------------------------ | ---------------------- | -------------------------------- | -------------------------------------------- |
| `bank_name`              | Bank names             | `blank_percentage`               | `"JPMorgan Chase"`, `"Bank of America"`      |
| `bank_routing_number`    | Bank routing codes     | `blank_percentage`               | `"021000021"`                                |
| `bank_swift_bic`         | SWIFT/BIC codes        | `blank_percentage`               | `"CHAUSUSXX"`                                |
| `bank_lei`               | Legal Entity IDs       | `blank_percentage`               | LEI numbers                                  |
| `bank_riad_code`         | RIAD codes             | `blank_percentage`               | Bank identification codes                    |
| `bank_street`            | Bank addresses         | `blank_percentage`               | Street address                               |
| `bank_city`              | Bank city              | `blank_percentage`               | City name                                    |
| `bank_state`             | Bank state             | `blank_percentage`               | State name                                   |
| `bank_branch_code`       | Branch codes           | `blank_percentage`               | `"001"`, `"025"`                             |
| `account_number`         | Account IDs            | `blank_percentage`               | `"123456789"`                                |
| `account_type`           | Account categories     | `blank_percentage`               | `"Checking"`, `"Savings"`, `"Money Market"`  |
| `credit_score`           | Credit rating          | `blank_percentage`, `min`, `max` | `"750"` (300-850)                            |
| `credit_score_band`      | Credit tiers           | `blank_percentage`               | `"Excellent"`, `"Good"`, `"Poor"`            |
| `credit_utilization`     | Credit usage %         | `blank_percentage`, `min`, `max` | `"35%"`                                      |
| `transaction_type`       | Transaction categories | `blank_percentage`               | `"Deposit"`, `"Withdrawal"`, `"Transfer"`    |
| `transaction_pattern`    | Transaction behaviors  | `blank_percentage`               | `"Regular"`, `"Sporadic"`, `"Unusual"`       |
| `investment_strategy`    | Investment approaches  | `blank_percentage`               | `"Growth"`, `"Value"`, `"Income"`            |
| `investment_persona`     | Investor types         | `blank_percentage`               | `"Conservative"`, `"Aggressive"`             |
| `investment_return_rate` | ROI percentages        | `blank_percentage`, `min`, `max` | `"7.5%"`                                     |
| `asset_type`             | Asset categories       | `blank_percentage`               | `"Stocks"`, `"Bonds"`, `"Real Estate"`       |
| `expense_category`       | Expense types          | `blank_percentage`               | `"Food"`, `"Utilities"`, `"Entertainment"`   |
| `expense_amount`         | Expense values         | `blank_percentage`, `min`, `max` | `"$150.00"`                                  |
| `tax_type`               | Tax categories         | `blank_percentage`               | `"Income"`, `"Property"`, `"Sales"`          |
| `tax_id`                 | Tax identification     | `blank_percentage`               | Tax ID numbers                               |
| `loan_type`              | Loan categories        | `blank_percentage`               | `"Auto"`, `"Mortgage"`, `"Personal"`         |
| `insurance_type`         | Insurance categories   | `blank_percentage`               | `"Auto"`, `"Home"`, `"Life"`                 |
| `insurance_provider`     | Insurance companies    | `blank_percentage`               | Insurance company names                      |
| `payment_term`           | Payment schedules      | `blank_percentage`               | `"Net 30"`, `"COD"`                          |
| `risk_level`             | Risk ratings           | `blank_percentage`               | `"Low"`, `"Medium"`, `"High"`                |
| `aml_risk_category`      | AML risk tiers         | `blank_percentage`               | `"Low Risk"`, `"Medium Risk"`                |
| `kyc_status`             | KYC states             | `blank_percentage`               | `"Verified"`, `"Pending"`, `"Failed"`        |
| `wealth_segment`         | Wealth tiers           | `blank_percentage`               | `"High Net Worth"`, `"Mass Affluent"`        |
| `spending_behavior`      | Spending patterns      | `blank_percentage`               | `"Conservative"`, `"Moderate"`, `"Splurger"` |
| `spending_category`      | Spending types         | `blank_percentage`               | `"Groceries"`, `"Entertainment"`             |
| `savings_goal`           | Savings targets        | `blank_percentage`               | `"Home Purchase"`, `"Retirement"`            |
| `grant_type`             | Grant categories       | `blank_percentage`               | `"Research"`, `"Community"`                  |
| `financial_goal`         | Financial targets      | `blank_percentage`               | `"Build Emergency Fund"`                     |
| `fraud_score`            | Fraud probability      | `blank_percentage`, `min`, `max` | `"0.23"` (0-1 scale)                         |
| `transfer_channel`       | Transfer methods       | `blank_percentage`               | `"Bank Transfer"`, `"Wire"`                  |

---

### 📱 **Communication Category** (22 providers)

Generate mobile, telecom, and network communication data.

| Provider               | Description          | Parameters                       | Example                             |
| ---------------------- | -------------------- | -------------------------------- | ----------------------------------- |
| `mobile_carrier`       | Telecom providers    | `blank_percentage`               | `"Verizon"`, `"AT&T"`, `"T-Mobile"` |
| `phone_number`         | Phone numbers        | `blank_percentage`               | `"555-123-4567"`                    |
| `imei_number`          | Device IDs           | `blank_percentage`               | IMEI numbers                        |
| `sim_card_type`        | SIM types            | `blank_percentage`               | `"Physical"`, `"eSIM"`              |
| `network_type`         | Network technologies | `blank_percentage`               | `"4G LTE"`, `"5G"`, `"WiFi"`        |
| `signal_strength`      | Signal quality       | `blank_percentage`               | `"-80 dBm"` (signal strength)       |
| `data_plan`            | Data packages        | `blank_percentage`               | `"Unlimited"`, `"5GB/month"`        |
| `download_speed`       | DL speeds            | `blank_percentage`, `min`, `max` | `"150 Mbps"`                        |
| `upload_speed`         | UL speeds            | `blank_percentage`, `min`, `max` | `"50 Mbps"`                         |
| `latency`              | Network latency      | `blank_percentage`, `min`, `max` | `"25ms"`, `"100ms"`                 |
| `wifi_standard`        | WiFi versions        | `blank_percentage`               | `"WiFi 6"`, `"WiFi 6E"`             |
| `roaming_status`       | Roaming states       | `blank_percentage`               | `"Active"`, `"Inactive"`            |
| `dual_sim_capability`  | Dual SIM support     | `blank_percentage`               | `"Yes"`, `"No"`                     |
| `esim_profiles_count`  | eSIM profile count   | `blank_percentage`, `min`, `max` | `"2"`, `"5"`                        |
| `hotspot_capability`   | Hotspot support      | `blank_percentage`               | `"Yes"`, `"No"`                     |
| `nfc_support`          | NFC enabled          | `blank_percentage`               | `"Yes"`, `"No"`                     |
| `volte_support`        | VoLTE enabled        | `blank_percentage`               | `"Yes"`, `"No"`                     |
| `wifi_calling_support` | WiFi calling         | `blank_percentage`               | `"Yes"`, `"No"`                     |
| `wifi_band`            | WiFi frequencies     | `blank_percentage`               | `"2.4GHz"`, `"5GHz"`, `"6GHz"`      |
| `apn_settings`         | APN configurations   | `blank_percentage`               | APN data                            |
| `bluetooth_version`    | Bluetooth versions   | `blank_percentage`               | `"5.3"`, `"5.2"`                    |
| `call_quality_rating`  | Call quality         | `blank_percentage`               | `1-5` ratings                       |
| `carrier_lock_status`  | Lock status          | `blank_percentage`               | `"Locked"`, `"Unlocked"`            |

---

### ✨ **Basic/Utility Category** (50+ providers)

Generate basic utilities, random data, and helper fields.

| Provider                                                                        | Description               | Parameters                                                                               | Example                                     |
| ------------------------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------- |
| `row_number`                                                                    | Auto-incrementing row ID  | `blank_percentage`                                                                       | `"1"`, `"2"`, `"3"`                         |
| `blank`                                                                         | Empty/null field          | `blank_percentage`                                                                       | Empty string or NULL                        |
| `boolean`                                                                       | True/False                | `blank_percentage`                                                                       | `True` or `False`                           |
| `number`                                                                        | Integer/float             | `blank_percentage`, `min`, `max`, `decimals`                                             | `"42"`, `"3.14"`                            |
| `color`                                                                         | Color names               | `blank_percentage`                                                                       | `"Red"`, `"Blue"`, `"Green"`                |
| `hex_color`                                                                     | Hex color codes           | `blank_percentage`                                                                       | `"#FF5733"`, `"#00AA00"`                    |
| `short_hex_color`                                                               | 3-char hex colors         | `blank_percentage`                                                                       | `"#F00"`, `"#0F0"`                          |
| `emoji`                                                                         | Emoji characters          | `blank_percentage`                                                                       | `"😀"`, `"🚀"`, `"❤️"`                      |
| `password`                                                                      | Secure passwords          | `blank_percentage`, `min_length`, `upper_num`, `lower_num`, `numbers_num`, `symbols_num` | `"A1!bC2@dE3"`                              |
| `password_hash`                                                                 | Hashed passwords          | `blank_percentage`                                                                       | Hash strings                                |
| `datetime`                                                                      | Date+time stamps          | `blank_percentage`, `from_date`, `to_date`, `date_format`, `minimum_age`, `maximum_age`  | `"06/24/2024 14:30:00"`                     |
| `time`                                                                          | Time only                 | `blank_percentage`                                                                       | `"14:30:00"`                                |
| `day_of_week`                                                                   | Day names                 | `blank_percentage`                                                                       | `"Monday"`, `"Friday"`                      |
| `month`                                                                         | Month names               | `blank_percentage`                                                                       | `"January"`, `"December"`                   |
| `season`                                                                        | Seasons                   | `blank_percentage`                                                                       | `"Winter"`, `"Summer"`                      |
| `date_range`                                                                    | Date ranges               | `blank_percentage`                                                                       | `"Jan 1 - Jan 31"`                          |
| `words`                                                                         | Random words              | `blank_percentage`                                                                       | `"apple"`, `"elephant"`, `"universe"`       |
| `sentences`                                                                     | Sentence text             | `blank_percentage`                                                                       | Multi-word sentences                        |
| `paragraphs`                                                                    | Paragraph text            | `blank_percentage`                                                                       | Full paragraphs                             |
| `punctuation`                                                                   | Special characters        | `blank_percentage`                                                                       | `"!"`, `"?"`, `"..."`                       |
| `rating`                                                                        | Ratings/scores            | `blank_percentage`                                                                       | `1-5` scale                                 |
| `sentiment`                                                                     | Sentiment classification  | `blank_percentage`                                                                       | `"Positive"`, `"Neutral"`, `"Negative"`     |
| `priority_level`                                                                | Priority ratings          | `blank_percentage`                                                                       | `"Low"`, `"Medium"`, `"High"`, `"Critical"` |
| `frequency`                                                                     | Frequency words           | `blank_percentage`                                                                       | `"Daily"`, `"Weekly"`, `"Monthly"`          |
| `duration`                                                                      | Time durations            | `blank_percentage`                                                                       | `"30 minutes"`, `"2 hours"`                 |
| `dimension`                                                                     | Size measurements         | `blank_percentage`                                                                       | `"Small"`, `"Large"`                        |
| `height`                                                                        | Height values             | `blank_percentage`, `min`, `max`                                                         | `"5'10\""`, `"180cm"`                       |
| `weight`                                                                        | Weight values             | `blank_percentage`, `min`, `max`                                                         | `"180 lbs"`, `"82kg"`                       |
| `temperature`                                                                   | Temperature values        | `blank_percentage`, `min`, `max`                                                         | `"72°F"`, `"22°C"`                          |
| `imperial_unit`                                                                 | Imperial measurements     | `blank_percentage`                                                                       | `"inches"`, `"pounds"`                      |
| `metric_prefix`                                                                 | Metric prefixes           | `blank_percentage`                                                                       | `"Kilo"`, `"Mega"`, `"Micro"`               |
| `dice_roll`                                                                     | D6 dice roll              | `blank_percentage`                                                                       | `1-6`                                       |
| `coin_flip`                                                                     | Heads/Tails               | `blank_percentage`                                                                       | `"Heads"` or `"Tails"`                      |
| `nato_phonetic`                                                                 | NATO phonetic             | `blank_percentage`                                                                       | `"Alpha"`, `"Bravo"`, `"Charlie"`           |
| `isbn`                                                                          | ISBN numbers              | `blank_percentage`                                                                       | `"978-3-16-148410-0"`                       |
| `ulid`                                                                          | ULID identifiers          | `blank_percentage`                                                                       | ULID format                                 |
| `paper_size`                                                                    | Paper sizes               | `blank_percentage`                                                                       | `"A4"`, `"Letter"`, `"Legal"`               |
| `current_timestamp`                                                             | Current time              | `blank_percentage`                                                                       | Current date/time                           |
| `sequence`                                                                      | Custom sequences          | `blank_percentage`, `start`, `step`                                                      | `"1"`, `"2"`, `"3"`                         |
| `address_line_2`                                                                | Address line 2            | `blank_percentage`                                                                       | `"Apt 4B"`, `"Suite 300"`                   |
| Plus distributions: `binomial`, `exponential`, `geometric`, `normal`, `poisson` | Statistical distributions | `blank_percentage`, parameters                                                           | Distribution samples                        |

---

### 🌐 **Basic Category - Distribution Providers**

Advanced statistical distributions for quantitative data generation:

| Provider                   | Description         | Parameters                            | Example                |
| -------------------------- | ------------------- | ------------------------------------- | ---------------------- |
| `binomial_distribution`    | Binomial outcomes   | `blank_percentage`, `n`, `p`          | `"45"` (from n trials) |
| `exponential_distribution` | Exponential decay   | `blank_percentage`, `lambda`          | `"2.3"`                |
| `geometric_distribution`   | Geometric sequences | `blank_percentage`, `p`               | `"5"`                  |
| `normal_distribution`      | Bell curve          | `blank_percentage`, `mean`, `std_dev` | `"102.5"`              |
| `poisson_distribution`     | Event counts        | `blank_percentage`, `lambda`          | `"3"`                  |

---

## Configuration & Advanced Options

### Global Options (All Providers)

Every provider accepts these core options:

| Option             | Type          | Default | Description                                  |
| ------------------ | ------------- | ------- | -------------------------------------------- |
| `blank_percentage` | float (0-100) | 0       | Percentage of records with NULL/empty values |

### Provider-Specific Parameters

Each provider may have additional parameters. Examples:

#### `number` Provider

```python
{
    "key_label": "age",
    "options": {
        "blank_percentage": 5,
        "min": 18,
        "max": 65,
        "decimals": 0
    }
}
```

#### `datetime` Provider

```python
{
    "key_label": "birth_date",
    "options": {
        "minimum_age": 18,
        "maximum_age": 65,
        "date_format": "mm/dd/yyyy"  # Format: yyyy/mm/dd, mm/dd/yyyy, dd/mm/yyyy, etc.
    }
}
```

#### `password` Provider

```python
{
    "key_label": "password",
    "options": {
        "min_length": 12,
        "upper_num": 2,
        "lower_num": 2,
        "numbers_num": 2,
        "symbols_num": 2
    }
}
```

#### `template` Provider

```python
{
    "key_label": "full_address",
    "options": {
        "template": "{{street_number}} {{street_name}}, {{city}}, {{state}} {{postal_code}}"
    }
}
```

#### `regular_expression` Provider

```python
{
    "key_label": "custom_id",
    "options": {
        "format": "[A-Z]{3}-[0-9]{4}-[A-Z]{2}"
    }
}
```

#### `custom_list` Provider

```python
{
    "key_label": "status",
    "options": {
        "values": ["Active", "Inactive", "Pending", "Archived"]
        # OR: "values": "Active,Inactive,Pending,Archived"
    }
}
```

#### `money` Provider

```python
{
    "key_label": "price",
    "options": {
        "min": 10,
        "max": 1000,
        "currency": "$"  # Can be: "$", "€", "¥", "£", etc.
    }
}
```

---

### 🧑 **Personal** (Name, Gender, Passport, etc.)

### 💰 **Finance** (Credit Cards, Banking, Currency)

`credit_card_number`, `credit_card_type`, `iban`, `bban`, `currency`, `currency_code`, `money`, `salary_range`, `stock_market`, etc.

### 🛍️ **Commerce** (Products, Orders, Pricing)

`product_name`, `product_category`, `product_price`, `barcode_ean13`, `order_status`, `payment_method`, `invoice_number`, `delivery_status`, `coupon_code`, etc.

### 📧 **Communication** (Email, Phone, Social)

`email_address`, `phone_number`, `username`, `social_media_handle`, `chat_message`, `contact_name`, etc.

### 🏗️ **Construction** (Building, Materials, Codes)

`construction_code`, `building_type`, `material_type`, `foundation_type`, `roof_type`, `door_type`, etc.

### 💻 **Tech/IT** (Programming, Frameworks, Version)

`programming_language`, `software_framework`, `version_number`, `log_level`, `http_status_code`, `file_extension`, `mime_type`, etc.

### 🏥 **Healthcare** (Diseases, Medications, Medical Codes)

`disease_name`, `symptom_name`, `medication_name`, `blood_type`, `vaccination_status`, `ICD10_diagnosis`, `ICD9_diagnosis`, `HCPCS_code`, etc.

### 🌍 **Location** (Countries, Cities, Addresses)

`country`, `state`, `city`, `street_address`, `postal_code`, `latitude`, `longitude`, `timezone`, `airport_code`, etc.

### 📚 **Education** (Schools, Courses, Subjects)

`university_name`, `degree`, `major`, `course_name`, `subject`, `educational_attainment`, etc.

### ⚖️ **Legal** (Laws, Contracts, Jurisdictions)

`legal_entity_type`, `contract_type`, `jurisdiction`, `court_type`, `legal_case_status`, `legal_term`, etc.

### 🎬 **Entertainment** (Movies, Books, Games)

`movie_title`, `movie_genre`, `book_title`, `author_name`, `video_game_title`, `music_genre`, `song_title`, etc.

### 🌿 **Nature** (Plants, Animals, Weather)

`plant_name`, `animal_name`, `tree_name`, `flower_name`, `weather_condition`, `season`, `biome`, etc.

### 🚗 **Automotive** (Cars, VINs, Fuel)

`car_make`, `car_model`, `car_vin`, `vehicle_type`, `license_plate`, `engine_type`, `fuel_type`, `transmission_type`, etc.

### 💱 **Cryptocurrency** (Coins, Blockchain, Wallets)

`crypto_currency`, `crypto_address`, `crypto_transaction_id`, `blockchain_type`, `smart_contract_language`, etc.

### 🎮 **Gaming** (Characters, Items, Guilds)

`character_class`, `character_race`, `game_genre`, `npc_name`, `item_type`, `quest_name`, `guild_name`, etc.

### 🎵 **Music** (Artists, Albums, Genres)

`artist_name`, `album_name`, `song_title`, `music_genre`, `instrument_name`, `music_production_software`, etc.

### 📱 **Marketing/Media** (Campaigns, Analytics, Content)

`campaign_name`, `social_media_platform`, `marketing_channel`, `content_type`, `target_audience`, `analytics_metric`, etc.

### 🌐 **Political** (Countries, Parties, Elections)

`political_party`, `political_ideology`, `election_type`, `government_structure`, `diplomatic_title`, etc.

### 📝 **Advanced** (Templates, Regex, Lambdas)

`template` (combine fields), `regular_expression` (match patterns), `lambda` (custom Python), `json_array`, `url`, `digit_sequence`, `character_sequence`, etc.

### 🤖 **AI/ML** (Models, Metrics, Training)

`model_type`, `model_framework`, `model_task`, `model_version`, `model_latency`, `model_confidence`, `cpu_utilization`, `gpu_utilization`, `data_drift_score`, `inference_result`, etc.

### ✨ **Basic** (Utilities, Random, Generators)

`row_number`, `blank`, `boolean`, `number`, `datetime`, `color`, `emoji`, `password`, `password_hash`, `isbn`, `ulid`, `sentiment`, `words`, `sentences`, `paragraphs`, etc.

### 🎲 **Miscellaneous** (Random & Fun)

`dice_roll`, `coin_flip`, `rating`, `frequency`, `priority_level`, `dimension`, `duration`, `height`, `weight`, `temperature`, etc.

---

## Export Formats

Generate data in your preferred format:

```python
# Export to multiple formats at once
IkiDataGenerator(schema).many(1000).export("dataset", formats=[
    "csv",      # Comma-separated values
    "json",     # JSON array of objects
    "sql",      # SQL INSERT statements
    "parquet",  # Apache Parquet (columnar)
    "excel",    # Excel workbook (.xlsx)
    "duckdb",   # DuckDB database
    # "tsv", "xml", "cql", "firebase", "dbunit" also supported
])
```

| Format        | File Extension | Best For                   | Notes                                  |
| ------------- | -------------- | -------------------------- | -------------------------------------- |
| **CSV**       | `.csv`         | Spreadsheets, import tools | Universal format                       |
| **JSON**      | `.json`        | APIs, JavaScript, NoSQL    | Pretty-printed with indent=2           |
| **SQL**       | `.sql`         | Databases                  | INSERT statements (specify table name) |
| **TSV**       | `.tsv`         | Tab-delimited data         | Alternative to CSV                     |
| **Excel**     | `.xlsx`        | Business reports           | Native Excel format                    |
| **Parquet**   | `.parquet`     | Big Data, Pandas, BI tools | Efficient columnar storage             |
| **DuckDB**    | `.duckdb`      | Analytics, SQL queries     | Embedded database                      |
| **XML**       | `.xml`         | Legacy systems, config     | Structured XML export                  |
| **Firestore** | `.json`        | Firebase/Firestore         | Firebase-ready format                  |
| **DBUnit**    | `.xml`         | Testing frameworks         | DBUnit test data format                |
| **CQL**       | `.cql`         | Cassandra databases        | CQL INSERT statements                  |

---

## API Reference

### `IkiDataGenerator(schema)`

Initialize the generator with a schema.

**Parameters:**

- `schema` (list): List of field names (strings) or field configs (dicts)

**Returns:** `IkiDataGenerator` instance

```python
gen = IkiDataGenerator(["first_name", "email_address"])
```

### `.many(n)`

Generate `n` records.

**Parameters:**

- `n` (int): Number of records to generate

**Returns:** `BaseGenerator` instance

```python
records = gen.many(100)
```

### `.export(name, formats=None)`

Export records to file(s).

**Parameters:**

- `name` (str): Output filename (without extension)
- `formats` (list, optional): File formats to export. Defaults to `["csv", "json"]`

**Returns:** None (files saved to `output/` folder)

```python
gen.many(100).export("users", formats=["csv", "json", "sql"])
# Creates: output/users.csv, output/users.json, output/users.sql
```

### `KEY_LABEL_REGISTRY`

Global dictionary mapping all 700+ field names to their categories.

```python
from ikidatagen import KEY_LABEL_REGISTRY

print(KEY_LABEL_REGISTRY["email_address"])  # → "personal"
print(KEY_LABEL_REGISTRY["credit_card_number"])  # → "commerce"
```

### `ProviderFactory`

Advanced: dynamically load providers.

```python
from ikidatagen import ProviderFactory

provider = ProviderFactory.create("email_address")
email = provider.generate()
```

---

## Advanced Examples

### Example 1: E-Commerce Dataset with Templates

```python
from ikidatagen import IkiDataGenerator

schema = [
    {"key_label": "row_number", "label": "Order ID"},
    {"key_label": "current_timestamp", "label": "Created At"},
    {"key_label": "customer_name", "label": "Customer"},
    {"key_label": "email_address", "label": "Email"},
    {"key_label": "product_name", "label": "Product"},
    {"key_label": "product_price", "label": "Price"},
    {
        "key_label": "template",
        "label": "Description",
        "options": {
            "template": "Order for {{product_name}} by {{customer_name}} ({{email_address}})"
        }
    },
    {"key_label": "order_status", "label": "Status"},
    {
        "key_label": "ip_address_v4",
        "label": "IP",
        "options": {"blank_percentage": 20}  # 20% missing
    }
]

IkiDataGenerator(schema).many(1000).export("orders", formats=["csv", "json"])
```

### Example 2: Healthcare Records

```python
from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "first_name",
    "last_name",
    "date_of_birth",
    "blood_type",
    "disease_name",
    "medication_name",
    "icd10_diagnosis",
    {
        "key_label": "current_timestamp",
        "label": "last_visit",
        "options": {"blank_percentage": 10}
    },
]

IkiDataGenerator(schema).many(500).export("patients", formats=["csv", "json", "sql"])
```

### Example 3: Test Data with Blanks and Validation

```python
from ikidatagen import IkiDataGenerator

schema = [
    {"key_label": "username", "options": {"blank_percentage": 0}},      # No blanks
    {"key_label": "email_address", "options": {"blank_percentage": 0}},  # No blanks
    {
        "key_label": "phone_number",
        "options": {"blank_percentage": 30}  # 30% missing phones
    },
    {
        "key_label": "address_line_1",
        "options": {"blank_percentage": 5}
    },
]

data = IkiDataGenerator(schema).many(10000).export("test_users", formats=["json"])
```

### Example 4: AI/ML Metrics Dataset

```python
from ikidatagen import IkiDataGenerator

schema = [
    "row_number",
    "model_type",
    "model_framework",
    "model_task",
    "model_version",
    "model_latency",
    "model_confidence",
    "cpu_utilization",
    "gpu_utilization",
    "memory_footprint",
    "inference_result",
    "inference_endpoint",
    "current_timestamp",
]

IkiDataGenerator(schema).many(5000).export("ml_metrics", formats=["parquet", "json"])
```

### Example 5: Custom Schema with Explicit Groups

```python
from ikidatagen import IkiDataGenerator

schema = [
    {"key_label": "username", "group": "personal"},
    {"key_label": "email_address", "group": "personal"},
    {"key_label": "product_name", "group": "commerce"},
    {"key_label": "currency", "group": "commerce"},
    {
        "key_label": "regular_expression",
        "group": "advanced",
        "label": "Custom Pattern",
        "options": {"pattern": "[A-Z]{2}[0-9]{4}"}
    }
]

IkiDataGenerator(schema).many(100).export("mixed_data")
```

---

## Configuration & Options

### Blank Percentage

Control how many records have empty values for a field:

```python
{
    "key_label": "phone_number",
    "options": {"blank_percentage": 25}  # 25% of records will have empty phone
}
```

### Templates

Combine fields with `{{field_name}}` syntax:

```python
{
    "key_label": "template",
    "options": {
        "template": "Full Name: {{first_name}} {{last_name}}, Email: {{email_address}}"
    }
}
```

### Regular Expressions

Generate data matching a pattern:

```python
{
    "key_label": "regular_expression",
    "options": {
        "pattern": "[A-Z]{3}-[0-9]{5}"  # Generates: ABC-12345
    }
}
```

### Custom List

Pick from a list of values:

```python
{
    "key_label": "custom_list",
    "options": {
        "values": ["Active", "Inactive", "Pending"]
    }
}
```

### Number Range

Generate numbers within a range:

```python
{
    "key_label": "number",
    "options": {
        "min": 0,
        "max": 100
    }
}
```

---

## 📚 Examples & Demonstrations

The `examples/` folder contains **45+ ready-to-run scripts** demonstrating all features and providers across 22 categories.

### Quick Start Examples

```bash
# Run the absolute simplest example
python examples/00_quick_start.py

# Explore basic fields
python examples/01_basic_fields.py

# Test all export formats
python examples/02_export_formats.py
```

### Run Examples by Category

#### Personal & Identity (3 examples)

```bash
python examples/10_personal_data.py          # Names, gender, dates
python examples/11_contact_info.py           # Email, phone, social
python examples/12_identity_documents.py     # Passports, SSN, IDs
```

#### E-Commerce & Shopping (4 examples)

```bash
python examples/20_ecommerce_shop.py         # Products with pricing
python examples/21_shopping_cart.py          # Complete orders
python examples/22_inventory_management.py   # Stock & inventory
python examples/23_payment_processing.py     # Payments & invoices
```

#### Finance & Banking (5 examples)

```bash
python examples/30_bank_accounts.py          # Bank accounts
python examples/31_credit_cards.py           # Credit card data
python examples/32_transactions.py           # Transfers & withdrawals
python examples/33_investment_portfolio.py   # Stocks & investments
python examples/34_crypto_blockchain.py      # Cryptocurrency wallets
```

#### Healthcare & Medical (3 examples)

```bash
python examples/40_patient_records.py        # Patient demographics
python examples/41_medical_diagnosis.py      # Diagnoses & ICD codes
python examples/42_medications.py            # Prescriptions & dosages
```

#### Location & Geography (2 examples)

```bash
python examples/50_addresses.py              # Addresses & coordinates
python examples/51_international_locations.py # Countries & cities
```

#### Education (1 example)

```bash
python examples/60_student_records.py        # Students & enrollment
```

#### Automotive (1 example)

```bash
python examples/70_car_inventory.py          # Cars, models, pricing
```

#### Entertainment & Gaming (2 examples)

```bash
python examples/90_gaming_players.py         # Gaming characters & guilds
python examples/92_entertainment.py          # Movies, books, music
```

#### Tech & Programming (2 examples)

```bash
python examples/100_programming_data.py      # Languages & frameworks
python examples/110_ml_models.py             # ML model metadata
python examples/111_ml_metrics.py            # Model performance metrics
```

#### Advanced Features (3 examples)

```bash
python examples/200_templates.py             # Combining fields with {{field}}
python examples/201_regex_patterns.py        # Custom regex patterns
python examples/203_blank_percentages.py     # Missing data simulation
```

#### Real-World Scenarios (7 complete systems)

```bash
python examples/300_saas_users.py            # SaaS with subscriptions
python examples/301_social_network.py        # Social media platform
python examples/302_analytics_events.py      # Event tracking (5000 events)
python examples/303_ecommerce_platform.py    # Complete e-commerce
python examples/304_travel_booking_system.py # Flights, hotels, bookings
python examples/308_hospital_system.py       # Hospital management
python examples/309_school_system.py         # University system
```

#### Batch & Large Datasets (3 examples)

```bash
python examples/400_mixed_categories.py      # Multiple categories mixed
python examples/401_batch_processing.py      # Batch generate 4 datasets
python examples/403_large_dataset.py         # Generate 1M+ records
```

#### Specialized Use Cases (4 examples)

```bash
python examples/500_test_data_unit_tests.py  # Unit test fixtures
python examples/501_load_testing_data.py     # Load testing (100K events)
python examples/502_demo_data.py             # Demo/presentation data
python examples/504_api_response_mocking.py  # Mock API responses
```

#### Complete Feature Showcase

```bash
python examples/999_showcase_all_features.py # All 12 features in one!
```

### Run All Examples at Once

To generate data from **all 45+ examples** in one command:

```bash
# Generate everything
for file in examples/[0-9]*.py; do
    echo "Running $file..."
    python "$file"
done
```

Or on Windows (PowerShell):

```powershell
Get-ChildItem examples\*.py -Filter "[0-9]*" | ForEach-Object {
    Write-Host "Running $($_.Name)..."
    python $_.FullName
}
```

### View Generated Output

All examples save data to the `output/` folder:

```
output/
├── quick_start.csv
├── quick_start.json
├── personal_data.csv
├── ecommerce_products.parquet
├── medical_diagnosis.json
├── ml_metrics.parquet
├── large_dataset.parquet
└── ... (40+ more files)
```

### Learning Path

**Beginner:** Start with simple examples and work up

```
00_quick_start → 01_basic_fields → 02_export_formats → 10_personal_data → 20_ecommerce_shop
```

**Intermediate:** Explore categories and features

```
30_bank_accounts → 40_patient_records → 50_addresses → 200_templates → 201_regex_patterns
```

**Advanced:** Complex real-world systems and large datasets

```
300_saas_users → 303_ecommerce_platform → 308_hospital_system → 400_mixed_categories → 403_large_dataset
```

### Examples Summary

| Category        | Examples | Records       | Topics                            |
| --------------- | -------- | ------------- | --------------------------------- |
| Getting Started | 3        | 50-100        | Basics, fields, formats           |
| Personal        | 3        | 50-300        | Names, IDs, documents             |
| Commerce        | 4        | 300-2000      | Products, orders, inventory       |
| Finance         | 5        | 200-1000      | Banking, cards, stocks, crypto    |
| Healthcare      | 3        | 300-500       | Patients, diagnoses, meds         |
| Location        | 2        | 500           | Addresses, coordinates, countries |
| Education       | 1        | 400           | Students, courses, degrees        |
| Automotive      | 1        | 600           | Cars, models, registration        |
| Entertainment   | 2        | 500-2000      | Gaming, movies, books, music      |
| Tech            | 2        | 200-5000      | Languages, frameworks, ML         |
| Advanced        | 3        | 50-500        | Templates, regex, blanks          |
| Real-World      | 7        | 300-5000      | Complete systems                  |
| Batch/Large     | 3        | 100K-1M       | Performance, scale                |
| Specialized     | 4        | 50-100K       | Testing, mocking, load tests      |
| **Total**       | **45+**  | **50 to 1M+** | **All features**                  |

### Modify Examples for Your Needs

All examples are templates—feel free to copy and modify:

```bash
# Copy an example as a starting point
cp examples/20_ecommerce_shop.py my_custom_dataset.py

# Edit and run your custom version
python my_custom_dataset.py
```

### Example Structure

Every example follows this simple pattern:

```python
from ikidatagen import IkiDataGenerator

# 1. Define schema
schema = [
    "first_name",
    "last_name",
    "email_address",
    # ... more fields
]

# 2. Generate data
IkiDataGenerator(schema).many(100).export("my_data", formats=["csv", "json"])

# 3. Check output/ folder
```

---

## Advanced Usage

### 1. Using Templates for Complex Fields

Combine multiple fields into a single output using template syntax:

```python
from ikidatagen import IkiDataGenerator

schema = [
    "first_name",
    "last_name",
    "email_address",
    {
        "label": "Full Profile",
        "key_label": "template",
        "options": {
            "template": "{{first_name}} {{last_name}} <{{email_address}}>"
        }
    },
    {
        "label": "Address",
        "key_label": "template",
        "options": {
            "template": "{{street_address}}, {{city}}, {{state}}, {{zipcode}}"
        }
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(100).export("profiles")
```

**Key features:**

- Use `{{field_name}}` syntax to reference any provider
- Combine unlimited fields in one template
- Useful for creating composite fields like full names or addresses

### 2. Custom Regex Patterns

Generate data matching custom patterns using regular expressions:

```python
schema = [
    {
        "label": "Order Number",
        "key_label": "regular_expression",
        "options": {"format": "ORD-[A-Z]{3}-\\d{5}"}  # ORD-ABC-12345
    },
    {
        "label": "Serial Number",
        "key_label": "regular_expression",
        "options": {"format": "[A-Z]{2}\\d{4}-[A-Z]{1}\\d{3}"}  # AB1234-X123
    },
    {
        "label": "License Plate",
        "key_label": "regular_expression",
        "options": {"format": "[A-Z]{3}-\\d{4}"}  # ABC-1234
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(500).export("orders")
```

### 3. Conditional Data with Blanks

Control data density by adding blank values strategically:

```python
schema = [
    {"key_label": "row_number", "label": "ID", "options": {"blank_percentage": 0}},  # Never blank
    {"key_label": "first_name", "label": "Name"},  # 0% blank (default)
    {
        "key_label": "phone_number",
        "label": "Phone",
        "options": {"blank_percentage": 20}  # 20% will be empty
    },
    {
        "key_label": "middle_name",
        "label": "Middle",
        "options": {"blank_percentage": 50}  # 50% will be empty
    },
    {
        "key_label": "nickname",
        "label": "Nickname",
        "options": {"blank_percentage": 80}  # 80% will be empty
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(1000).export("contacts")
```

### 4. Numeric Ranges and Precision

Generate numbers with specific ranges and decimal places:

```python
schema = [
    {
        "label": "Price",
        "key_label": "number",
        "options": {"min": 9.99, "max": 999.99, "decimals": 2}
    },
    {
        "label": "Quantity",
        "key_label": "number",
        "options": {"min": 1, "max": 1000, "decimals": 0}
    },
    {
        "label": "Rating",
        "key_label": "number",
        "options": {"min": 0, "max": 5, "decimals": 1}
    },
    {
        "label": "Percentage",
        "key_label": "number",
        "options": {"min": 0, "max": 100, "decimals": 2}
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(5000).export("products")
```

### 5. Date Ranges and Formats

Generate dates with custom ranges and formatting:

```python
from datetime import datetime, timedelta

schema = [
    {
        "label": "Born",
        "key_label": "date_time",
        "options": {
            "from_date": "1950-01-01",
            "to_date": "2010-12-31",
            "date_format": "%Y-%m-%d"
        }
    },
    {
        "label": "Order Date",
        "key_label": "date_time",
        "options": {
            "from_date": "2024-01-01",
            "to_date": "2024-12-31",
            "date_format": "%m/%d/%Y"  # MM/DD/YYYY format
        }
    },
    {
        "label": "Age Range",
        "key_label": "date_time",
        "options": {
            "minimum_age": 18,
            "maximum_age": 65
        }
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(1000).export("dates")
```

### 6. Custom Password Generation

Generate secure passwords with specific requirements:

```python
schema = [
    "username",
    {
        "label": "Basic Password",
        "key_label": "password",
        "options": {"min_length": 8}
    },
    {
        "label": "Strong Password",
        "key_label": "password",
        "options": {
            "min_length": 12,
            "upper_num": 2,       # 2+ uppercase
            "lower_num": 2,       # 2+ lowercase
            "numbers_num": 2,     # 2+ digits
            "symbols_num": 2      # 2+ symbols (!@#$, etc)
        }
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(100).export("credentials")
```

### 7. Currency-Formatted Money

Generate currency values in different formats:

```python
schema = [
    {
        "label": "USD Price",
        "key_label": "money",
        "options": {
            "min": 10,
            "max": 1000,
            "currency": "USD"  # Returns $1,234.56
        }
    },
    {
        "label": "EUR Price",
        "key_label": "money",
        "options": {
            "min": 10,
            "max": 1000,
            "currency": "EUR"  # Returns €1.234,56
        }
    },
    {
        "label": "JPY Price",
        "key_label": "money",
        "options": {
            "min": 1000,
            "max": 100000,
            "currency": "JPY"  # Returns ¥123,456
        }
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(1000).export("prices")
```

### 8. Custom Lists & Choices

Generate data from custom value lists:

```python
schema = [
    {
        "label": "Priority",
        "key_label": "custom_list",
        "options": {"values": ["Low", "Medium", "High", "Urgent"]}
    },
    {
        "label": "Status",
        "key_label": "custom_list",
        "options": {"values": "Draft,Review,Approved,Published"}  # Comma-separated also works
    },
    {
        "label": "Environment",
        "key_label": "custom_list",
        "options": {"values": ["Development", "Staging", "Production"]}
    },
]

generator = IkiDataGenerator(schema)
data = generator.many(500).export("tasks")
```

---

## Best Practices & Performance Tips

### 📊 Performance Optimization

#### For Large Datasets (1M+ records)

```python
from ikidatagen import IkiDataGenerator

# ✅ GOOD: Generate in batches
schema = ["first_name", "last_name", "email_address"]
generator = IkiDataGenerator(schema)

# Generate 1 million records in 100K batches
batches = 100000
total_records = 1000000

for i in range(0, total_records, batches):
    print(f"Generating {i} to {i+batches}...")
    generator.many(batches).export(f"users_batch_{i//batches:03d}")
```

#### Minimize Blank Percentages

```python
# ✅ GOOD: Only use blanks where needed
schema = [
    {"key_label": "id", "label": "ID", "options": {"blank_percentage": 0}},  # Never blank
    {"key_label": "email", "options": {"blank_percentage": 5}},  # Minimal blanks
]

# ❌ AVOID: Too many blanks = performance hit
schema = [
    {"key_label": "field", "options": {"blank_percentage": 95}},  # 95% blanks!
]
```

#### Use Simple Fields When Possible

```python
# ✅ GOOD: Simple field directly
schema = ["first_name", "last_name"]

# ❌ SLOWER: Dict with redundant options
schema = [
    {"key_label": "first_name", "label": "first_name", "options": {"blank_percentage": 0}},
    {"key_label": "last_name", "label": "last_name", "options": {"blank_percentage": 0}},
]
```

### 🎯 Schema Design Best Practices

#### 1. Always Include IDs

```python
schema = [
    {"key_label": "row_number", "label": "id", "options": {"blank_percentage": 0}},
    # ... other fields
]
```

#### 2. Use Meaningful Labels

```python
# ✅ GOOD: Clear, descriptive labels
schema = [
    {"key_label": "first_name", "label": "Given Name"},
    {"key_label": "last_name", "label": "Family Name"},
]

# ❌ AVOID: Cryptic labels
schema = [
    {"key_label": "first_name", "label": "fn"},
    {"key_label": "last_name", "label": "ln"},
]
```

#### 3. Organize Fields Logically

```python
# ✅ GOOD: Logical grouping
schema = [
    # Identity
    "first_name", "last_name", "date_of_birth",
    # Contact
    "email_address", "phone_number",
    # Location
    "street_address", "city", "state", "zipcode",
    # Professional
    "job_title", "company_name",
]
```

#### 4. Match Field Types to Context

```python
# ✅ GOOD: Use specialized fields
schema = [
    {"key_label": "money", "label": "Balance", "options": {"currency": "USD", "min": 0, "max": 50000}},
    {"key_label": "credit_card_number", "label": "Card"},
]

# ❌ AVOID: Generic numbers for specific data
schema = [
    {"key_label": "number", "label": "Balance"},
    {"key_label": "number", "label": "Card"},  # Not realistic!
]
```

### 📁 Export Format Selection

```python
# ✅ Use the right format for the job
schema = ["name", "email", "created_at"]

# For analytics: Parquet (compressed, fast)
generator.many(1000000).export("data", formats=["parquet"])

# For web apps: JSON
generator.many(100).export("data", formats=["json"])

# For databases: SQL
generator.many(5000).export("data", formats=["sql"])

# For spreadsheets: Excel or CSV
generator.many(100).export("data", formats=["excel", "csv"])
```

---

## Integration Examples

### 1. Database Integration

#### PostgreSQL with SQLAlchemy

```python
from sqlalchemy import create_engine
from ikidatagen import IkiDataGenerator
import json

# Generate data
schema = ["first_name", "last_name", "email_address", "phone_number"]
generator = IkiDataGenerator(schema)
data = generator.many(1000).export("users")

# Load into database
engine = create_engine("postgresql://user:password@localhost/mydb")

# Read CSV and insert
import pandas as pd
df = pd.read_csv("output/users.csv")
df.to_sql("users", engine, if_exists="append", index=False)
```

#### MongoDB

```python
from pymongo import MongoClient
from ikidatagen import IkiDataGenerator
import json

schema = [
    "first_name", "last_name", "email_address",
    {"key_label": "current_timestamp", "label": "created_at"}
]

generator = IkiDataGenerator(schema)
generator.many(5000).export("users", formats=["json"])

# Connect and insert
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["users"]

with open("output/users.json") as f:
    data = json.load(f)
    collection.insert_many(data)
```

### 2. REST API Population

```python
import requests
from ikidatagen import IkiDataGenerator

schema = ["first_name", "last_name", "email_address"]
generator = IkiDataGenerator(schema)

# Generate batch of records
records = generator.many(100)

# Simulate API posting
for record in records:
    response = requests.post(
        "https://api.example.com/users",
        json=record,
        headers={"Authorization": "Bearer YOUR_TOKEN"}
    )
    print(f"Created user {response.status_code}")
```

### 3. Testing with pytest

```python
import pytest
from ikidatagen import IkiDataGenerator

@pytest.fixture
def user_data():
    """Generate test user data"""
    schema = ["first_name", "last_name", "email_address"]
    generator = IkiDataGenerator(schema)
    return generator.many(100)

@pytest.fixture
def order_data():
    """Generate test order data"""
    schema = [
        "row_number",
        "first_name",
        {"key_label": "money", "options": {"min": 10, "max": 1000}},
        "order_status"
    ]
    generator = IkiDataGenerator(schema)
    return generator.many(50)

def test_user_creation(user_data):
    assert len(user_data) == 100
    assert "first_name" in user_data[0]
```

---

## Customization & Extension Guide

### Creating Custom Providers

Add domain-specific data generators:

```python
# In your project: custom_providers.py

from src.ikidatagen.base_generator import BaseProvider

class CustomDomainProvider(BaseProvider):
    """Generate domain-specific data"""

    def generate_non_blank(self):
        """Override this method with your logic"""
        domain_data = [
            "item_one",
            "item_two",
            "item_three",
        ]
        return random.choice(domain_data)

# Use in your schema
from custom_providers import CustomDomainProvider

schema = [
    "first_name",
    "last_name",
    {
        "label": "Custom Field",
        "key_label": "custom_domain",  # Your provider class
    }
]

generator = IkiDataGenerator(schema)
data = generator.many(100).export("custom_data")
```

---

## Error Handling & Troubleshooting

### Common Issues & Solutions

#### 1. "Provider not found" Error

```python
# ❌ WRONG: Typo in provider name
schema = [
    {"key_label": "first_nmae"}  # Typo: 'nmae' instead of 'name'
]

# ✅ CORRECT: Use exact provider name
schema = [
    {"key_label": "first_name"}
]
```

#### 2. Export Format Not Recognized

```python
# ❌ WRONG: Unsupported format
generator.many(100).export("data", formats=["txt"])

# ✅ CORRECT: Use supported formats
generator.many(100).export("data", formats=["csv", "json", "parquet"])
```

#### 3. Memory Issues with Large Datasets

```python
# ❌ PROBLEMATIC: Loading everything at once
for i in range(1000000):
    data = IkiDataGenerator(schema).many(1)  # Creates 1M objects!

# ✅ BETTER: Batch processing
for batch in range(0, 1000000, 10000):
    IkiDataGenerator(schema).many(10000).export(f"batch_{batch}")
```

#### 4. Incorrect Date Format

```python
# ❌ WRONG: Invalid date format code
options = {"date_format": "%Y%d%m"}  # YYYY-DD-MM (invalid!)

# ✅ CORRECT: Use valid Python date codes
options = {"date_format": "%Y-%m-%d"}  # YYYY-MM-DD
options = {"date_format": "%m/%d/%Y"}  # MM/DD/YYYY
options = {"date_format": "%d-%b-%Y"}  # DD-Mon-YYYY
```

### Debug Mode

```python
# Enable detailed logging
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("ikidatagen")
logger.setLevel(logging.DEBUG)

# Now generate data with detailed output
generator = IkiDataGenerator(schema)
data = generator.many(10)
```

---

## Expanded API Reference

### Core Classes

#### `IkiDataGenerator`

Main class for generating synthetic data.

**Constructor:**

```python
generator = IkiDataGenerator(
    schema: List[str | Dict],      # Field definitions
    output_dir: str = "output"     # Where to save exports
)
```

**Key Methods:**

| Method                   | Parameters                        | Returns            | Description                      |
| ------------------------ | --------------------------------- | ------------------ | -------------------------------- |
| `.many(n)`               | `n: int`                          | `GeneratorBuilder` | Generate n records               |
| `.export(name, formats)` | `name: str`, `formats: List[str]` | Path               | Export to multiple formats       |
| `.get_schema()`          | -                                 | `Dict`             | Get current schema configuration |
| `.validate_schema()`     | -                                 | `Bool`             | Check if schema is valid         |

**Example:**

```python
generator = IkiDataGenerator(schema)
result = generator.many(1000).export("mydata", formats=["csv", "json"])
```

#### Schema Entry Structure

Each schema entry can be:

**Simple string (shorthand):**

```python
"first_name"  # Uses all defaults
```

**Dictionary (full control):**

```python
{
    "key_label": "first_name",           # Required: provider name
    "label": "First Name",               # Optional: column name (defaults to key_label)
    "group": "personal",                 # Optional: category (auto-resolved)
    "options": {
        "blank_percentage": 10,          # Optional: % of blanks
        # ... provider-specific options
    }
}
```

### Export Formats

| Format       | Extension  | Best For               | Speed     | Size     |
| ------------ | ---------- | ---------------------- | --------- | -------- |
| **CSV**      | `.csv`     | Spreadsheets, Excel    | Fast      | Medium   |
| **JSON**     | `.json`    | APIs, Web, NoSQL       | Medium    | Large    |
| **Parquet**  | `.parquet` | Analytics, Compression | Fastest   | Smallest |
| **Excel**    | `.xlsx`    | Business Reports       | Medium    | Medium   |
| **SQL**      | `.sql`     | Database Inserts       | Medium    | Medium   |
| **DuckDB**   | `.duckdb`  | Data Warehouse         | Very Fast | Small    |
| **TSV**      | `.tsv`     | Tab-separated          | Fast      | Medium   |
| **XML**      | `.xml`     | Legacy Systems         | Slow      | Large    |
| **Firebase** | `.json`    | Firebase DB            | Special   | Medium   |

---

## Project Structure

```
Iki-Data-Generator/
├── examples/                    # 45+ example scripts
│   ├── README.md                # Examples guide
│   ├── 00_quick_start.py        # Simplest example
│   ├── 01_basic_fields.py
│   ├── 20_ecommerce_shop.py
│   ├── 300_saas_users.py
│   ├── 403_large_dataset.py
│   └── 999_showcase_all_features.py  # All features!
├── src/ikidatagen/              # Main package
│   ├── __init__.py              # Public API
│   ├── core.py                  # Main IkiDataGenerator class
│   ├── base_generator.py        # Data generation logic
│   ├── exporters.py             # Export to CSV, JSON, SQL, etc.
│   ├── provider_factory.py      # Dynamic provider loading
│   ├── schema_registry.py       # Maps field names to categories
│   ├── payload.py               # Data payload handling
│   ├── dataset_manager.py       # Dataset management
│   ├── external_datasets/       # External data files
│   │   ├── csv/                 # 30+ CSV files (countries, airlines, etc.)
│   │   └── json/                # 25+ JSON files (advanced data)
│   └── providers/               # Data providers (700+ fields)
│       ├── advanced/            # Template, Regex, Lambda, etc.
│       ├── ai/                  # ML/AI metrics
│       ├── basic/               # Names, dates, colors, etc.
│       ├── car/                 # Vehicle data
│       ├── commerce/            # Products, orders, payments
│       ├── communication/       # Email, phone, social
│       ├── construction/        # Building codes, materials
│       ├── crypto/              # Cryptocurrency data
│       ├── education/           # Schools, degrees, subjects
│       ├── finance/             # Credit cards, banking
│       ├── gaming/              # Characters, items, guilds
│       ├── health/              # Medical codes, symptoms
│       ├── it/                  # Programming, frameworks
│       ├── legal/               # Laws, contracts
│       ├── location/            # Countries, cities, addresses
│       ├── marketing/           # Campaigns, channels
│       ├── misc/                # Miscellaneous data
│       ├── music/               # Artists, albums, genres
│       ├── nature/              # Plants, animals, weather
│       ├── personal/            # Names, gender, documents
│       ├── political/           # Parties, elections
│       ├── products/            # Product categories
│       ├── sports/              # Athletes, teams, leagues
│       └── travel/              # Airlines, hotels, destinations
├── output/                      # Generated data (CSV, JSON, etc.)
├── main.py                      # Example usage
├── pyproject.toml               # Package metadata
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

---

## How It Works (Behind the Scenes)

1. **Schema Parsing**: You provide a list of fields (strings or dicts)
2. **Provider Resolution**: Each field name is looked up in `KEY_LABEL_REGISTRY` to find its category
3. **Dynamic Loading**: The appropriate provider class is loaded from `providers/{category}/{field}.py`
4. **Generation**: Each provider generates realistic data for _n_ records
5. **Template Processing**: Template fields combine other fields using `{{field}}` syntax
6. **Blank Handling**: Records marked for blanks are cleared based on `blank_percentage`
7. **Export**: Data is serialized to your chosen format(s) and saved to `output/`

---

## Common Issues & Solutions

### ❌ "Unknown key_label 'xxx'"

**Problem:** You used a field name that doesn't exist.

**Solution:** Check `KEY_LABEL_REGISTRY` or review the 22 categories above. Did you spell it correctly? (Use underscores, lowercase.)

```python
# ❌ Wrong
schema = ["firstName"]  # camelCase? No!

# ✅ Correct
schema = ["first_name"]  # snake_case? Yes!
```

### ❌ "No data to export"

**Problem:** `.many(0)` or empty schema.

**Solution:** Generate at least 1 record.

```python
# ❌ Wrong
IkiDataGenerator(schema).many(0).export("data")

# ✅ Correct
IkiDataGenerator(schema).many(100).export("data")
```

### ❌ Export folder not found

**Problem:** `output/` directory doesn't exist.

**Solution:** The library creates it automatically. Make sure you have write permissions.

### ❌ Template field not rendering

**Problem:** `{{field_name}}` not being replaced.

**Solution:** Ensure the referenced field exists in your schema and the spelling matches exactly.

```python
# ❌ Wrong
{
    "key_label": "template",
    "options": {"template": "Name: {{first_name}} {{FirstName}}"}  # FirstName ≠ first_name
}

# ✅ Correct
{
    "key_label": "template",
    "options": {"template": "Name: {{first_name}} {{last_name}}"}
}
```

---

## Performance Tips

### Generating Large Datasets

- Use **Parquet** or **DuckDB** formats for large datasets (smaller file sizes, faster I/O)
- **DuckDB** is perfect for immediate querying: `import duckdb; duckdb.sql("SELECT * FROM 'data.duckdb'")`
- For 1M+ records, generate in batches to manage memory

```python
# ✅ Generate in chunks
for i in range(10):
    IkiDataGenerator(schema).many(100_000).export(f"chunk_{i}")
```

### Field Selection

- Only include fields you need (reduces generation time)
- Skip fields with expensive generation (e.g., `password_hash`)

### Export Efficiency

```python
# ✅ Smart exports
IkiDataGenerator(schema).many(1_000_000).export("big_data", formats=["parquet"])

# ❌ Avoid exporting to many formats at once
# IkiDataGenerator(schema).many(1_000_000).export("data", formats=["csv", "json", "sql", "excel"])
```

---

## Contributing

Have ideas? Want to add new providers or categories? Open a PR!

- **New Provider**: Add a file to `src/ikidatagen/providers/{category}/{field_name}.py`
- **New Category**: Create a folder in `providers/` and add your providers
- **Update Registry**: Edit `schema_registry.py` to register new fields
- **Tests**: Add tests for new providers

---

## License

MIT License — use it freely in personal and commercial projects.

---

## Links & Resources

- **GitHub**: [github.com/ikidevz/IkiDataGenerator](https://github.com/ikidevz/IkiDataGenerator)
- **Issues**: [Report bugs or request features](https://github.com/ikidevz/IkiDataGenerator/issues)
- **PyPI**: [pypi.org/project/iki-data-generator](https://pypi.org/project/iki-data-generator/)

---

## FAQ

### Getting Started

#### Q: Can I use this data for production?

**A:** This is _synthetic_ data—perfect for development, testing, and demos. For production, consider anonymizing real data or using this as a base.

#### Q: What Python versions are supported?

**A:** Python ≥ 3.10. The library uses modern Python features and is tested on:

- Python 3.10
- Python 3.11
- Python 3.12

#### Q: How do I install it on Windows/Mac/Linux?

**A:** Same for all platforms:

```bash
pip install iki-data-generator
```

Or from source:

```bash
git clone https://github.com/ikidevz/IkiDataGenerator.git
cd Iki-Data-Generator
pip install -e .
```

### Data Generation

#### Q: Can I regenerate the exact same data?

**A:** Not yet. Each run generates different data using random seed generation. Deterministic seed support is planned for future releases. For now:

```python
# Each run produces different output
data1 = generator.many(100).export("run1")
data2 = generator.many(100).export("run2")  # Different values
```

#### Q: How many records can I generate?

**A:** Theoretically unlimited, but practical limits depend on:

- **Available RAM**: 1M records typically use ~500MB
- **Export format**: CSV is lightweight; JSON uses more space
- **Fields per record**: More fields = larger dataset

**Recommended approach for 100M+ records:**

```python
# Generate in batches
batch_size = 100000
for i in range(0, 100000000, batch_size):
    generator.many(batch_size).export(f"batch_{i//batch_size}")
```

#### Q: How fast is the generation?

**A:** Performance depends on your system and schema:

- **Small schemas** (5-10 fields): 50K-100K records/second
- **Medium schemas** (20-50 fields): 20K-50K records/second
- **Complex schemas** (templates, regex, blanks): 5K-20K records/second

Typical performance on modern hardware:

```python
import time

schema = ["first_name", "last_name", "email_address"]
start = time.time()
generator.many(100000).export("users")
elapsed = time.time() - start
print(f"Generated 100K records in {elapsed:.2f} seconds")  # ~1-2 seconds
```

### Schema & Fields

#### Q: How do I know which providers are available?

**A:** The library includes 700+ built-in providers across 22 categories. Check the **Complete Provider Reference** section in this README, or list them in code:

```python
from src.ikidatagen.schema_registry import KEY_LABEL_REGISTRY

# Print all available providers
for key, value in sorted(KEY_LABEL_REGISTRY.items()):
    print(f"{key:40} -> {value}")
```

#### Q: Can I extend it with custom fields?

**A:** Yes! Create a custom provider class:

```python
# custom_providers.py
from src.ikidatagen.base_generator import BaseProvider
import random

class BeerBrandProvider(BaseProvider):
    def generate_non_blank(self):
        brands = ["Corona", "Heineken", "Guinness", "Stella", "Budweiser"]
        return random.choice(brands)

# Use it in your schema
schema = [
    "first_name",
    {
        "label": "Favorite Beer",
        "key_label": "beer_brand"  # Your custom provider
    }
]

generator = IkiDataGenerator(schema)
data = generator.many(100).export("drinkers")
```

#### Q: What's the difference between `blank_percentage` and NULL values?

**A:** We use `blank_percentage` (0–100) to control how many records have empty strings:

- `blank_percentage: 0` → All records have values
- `blank_percentage: 50` → 50% have empty strings
- `blank_percentage: 100` → All records are empty

```python
schema = [
    {"key_label": "phone_number", "options": {"blank_percentage": 30}}
    # 30% of phone_number fields will be ""
]
```

#### Q: How do I create composite fields (templates)?

**A:** Use the `template` provider with `{{field_name}}` syntax:

```python
schema = [
    "first_name",
    "last_name",
    {
        "label": "Display Name",
        "key_label": "template",
        "options": {"template": "{{last_name}}, {{first_name}}"}
    },
]
```

### Export & Formats

#### Q: What export formats are supported?

**A:** 11+ formats:

| Format            | Use Case               | Speed     | Size     |
| ----------------- | ---------------------- | --------- | -------- |
| **CSV**           | Spreadsheets           | Very Fast | Medium   |
| **JSON**          | APIs, Web              | Fast      | Large    |
| **Parquet**       | Analytics, Compression | Fastest   | Smallest |
| **Excel** (.xlsx) | Business Reports       | Medium    | Medium   |
| **SQL**           | Database Imports       | Medium    | Medium   |
| **DuckDB**        | Data Warehouse         | Very Fast | Small    |
| **TSV**           | Tab-separated          | Very Fast | Medium   |
| **XML**           | Legacy Systems         | Slow      | Large    |
| **Firebase**      | Firebase DB            | Special   | Medium   |
| **HTML**          | Web Display            | Medium    | Large    |
| **Markdown**      | Documentation          | Medium    | Medium   |

```python
# Export to multiple formats at once
generator.many(1000).export(
    "mydata",
    formats=["csv", "json", "parquet", "excel"]
)
# Creates: mydata.csv, mydata.json, mydata.parquet, mydata.xlsx
```

#### Q: How do I query generated data?

**A:** Export to DuckDB for SQL queries:

```python
import duckdb

# Generate and export
generator.many(10000).export("users", formats=["duckdb"])

# Query the DuckDB file
conn = duckdb.connect("output/users.duckdb")
results = conn.execute(
    "SELECT first_name, COUNT(*) FROM users GROUP BY first_name LIMIT 10"
).fetchall()
print(results)
```

#### Q: Can I import the data into Excel?

**A:** Yes! Export to Excel directly:

```python
generator.many(1000).export("users", formats=["excel"])
# Opens with: Excel, Google Sheets, LibreOffice, Numbers, etc.
```

Or export to CSV and open in Excel:

```python
generator.many(1000).export("users", formats=["csv"])
# Open output/users.csv with Excel
```

#### Q: How do I load data into a database?

**A:**

**PostgreSQL:**

```python
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("output/users.csv")
engine = create_engine("postgresql://user:pass@localhost/mydb")
df.to_sql("users", engine, if_exists="append", index=False)
```

**MongoDB:**

```python
import json
from pymongo import MongoClient

with open("output/users.json") as f:
    data = json.load(f)

client = MongoClient("mongodb://localhost:27017/")
client["mydb"]["users"].insert_many(data)
```

**MySQL:**

```python
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("output/users.csv")
engine = create_engine("mysql+pymysql://user:pass@localhost/mydb")
df.to_sql("users", engine, if_exists="append", index=False)
```

### Advanced Topics

#### Q: What if I need a field that doesn't exist?

**A:** Use the `lambda` provider for custom logic:

```python
import random

schema = [
    "first_name",
    {
        "label": "Custom ID",
        "key_label": "lambda",
        "options": {
            "function": lambda: f"USER_{random.randint(100000, 999999)}"
        }
    }
]
```

#### Q: How do I use regular expressions for custom patterns?

**A:** Use the `regular_expression` provider:

```python
schema = [
    {
        "label": "Order Number",
        "key_label": "regular_expression",
        "options": {"format": "ORD-\\d{6}"}  # ORD-123456
    },
    {
        "label": "Phone",
        "key_label": "regular_expression",
        "options": {"format": "\\(\\d{3}\\) \\d{3}-\\d{4}"}  # (123) 456-7890
    }
]
```

#### Q: Can I join related data (foreign keys)?

**A:** Foreign key support is planned! For now, use templates to relate data:

```python
# Generate master and detail records
schema = [
    {"key_label": "row_number", "label": "order_id"},
    {"key_label": "row_number", "label": "product_id"},
    "product_name",
]

# Or manually join in code
orders = generator.many(100)
for order in orders:
    order["product_id"] = random.randint(1, 50)
```

#### Q: How do I handle timezone-aware dates?

**A:** The date generator creates naive dates. Convert in code:

```python
from datetime import datetime
import pytz

schema = ["first_name", {"key_label": "date_of_birth", "label": "DOB"}]
data = generator.many(100)

# Add timezone
utc = pytz.UTC
for record in data:
    record["DOB"] = datetime.fromisoformat(record["DOB"]).replace(tzinfo=utc)
```

#### Q: How do I profile or analyze the generated data?

**A:** Export to Parquet and analyze with pandas:

```python
import pandas as pd

generator.many(50000).export("data", formats=["parquet"])
df = pd.read_parquet("output/data.parquet")

# Basic profiling
print(df.describe())
print(df.dtypes)
print(df.isnull().sum())
```

#### Q: Can I use this with Docker?

**A:** Yes! Create a Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "my_script.py"]
```

Then run:

```bash
docker build -t datagen .
docker run -v $(pwd)/output:/app/output datagen
```

### Troubleshooting

#### Q: I get "Provider not found" error

**A:** Check the provider name spelling:

```python
# ❌ Wrong: Typo
schema = [{"key_label": "first_nmae"}]

# ✅ Correct
schema = [{"key_label": "first_name"}]
```

#### Q: Memory usage is too high

**A:** Generate in smaller batches:

```python
# ❌ Bad: Generates 10M records in memory
data = generator.many(10000000)

# ✅ Good: Process in batches
for i in range(0, 10000000, 100000):
    generator.many(100000).export(f"batch_{i//100000}")
```

#### Q: Export is slow

**A:** Some formats are slower than others. Optimize:

```python
# Fastest
generator.many(100000).export("data", formats=["parquet"])

# Fast
generator.many(100000).export("data", formats=["csv"])

# Slower but readable
generator.many(100000).export("data", formats=["json"])
```

#### Q: Data looks unrealistic

**A:** Check your schema for issues:

```python
# ❌ May look unrealistic: Generic number
schema = [{"key_label": "number", "label": "credit_card"}]

# ✅ Better: Use realistic provider
schema = [{"key_label": "credit_card_number", "label": "credit_card"}]
```

---

## Roadmap

- 🔄 **Seed support** for reproducible datasets
- 🔗 **Foreign key relationships** for relational data generation
- 📊 **Better performance** for 100M+ records with streaming
- 🤖 **AI-powered schema suggestions** based on use case
- 🎨 **Web GUI** for schema builder and visualization
- 📈 **Data profiling & statistics** to validate generation
- 🔐 **PII detection** to ensure privacy-safe data
- 🌐 **API service** for cloud-based generation
- 📚 **Dataset templates** for common domains (SaaS, E-commerce, Healthcare)

---

## Contribution

Found a bug? Want to add providers? Contributions welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes and test
4. Submit a pull request

---

## Thanks

Built with ❤️ for developers who hate dummy data.

Happy generating! 🎲

---

**Last updated:** June 2026 | **Version:** 1.0.0 | **License:** MIT
