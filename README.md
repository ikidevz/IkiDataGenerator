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

### Available Options (Common)

| Option               | Type      | Example                          | Effect                                            |
| -------------------- | --------- | -------------------------------- | ------------------------------------------------- |
| **blank_percentage** | int/float | `10`                             | Percentage of records where field is empty        |
| **template**         | str       | `"{{first_name}} {{last_name}}"` | Combine fields with template syntax               |
| **pattern**          | str       | `"[A-Z]{3}-\d{4}"`               | Regex pattern (for `regular_expression` provider) |
| **min**, **max**     | int/float | `min=0, max=100`                 | Range for numeric fields                          |

---

## 22 Data Categories

Iki Data Generator organizes 700+ fields into 22 categories. Here's a quick overview:

### 🧑 **Personal** (Name, Gender, Passport, etc.)

`first_name`, `last_name`, `middle_name`, `gender_binary`, `gender_spectrum`, `title`, `passport_number`, `ssn`, `nationality`, etc.

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

### Q: Can I use this data for production?

**A:** This is _synthetic_ data—perfect for development, testing, and demos. For production, consider anonymizing real data or using this as a base.

### Q: Can I extend it with custom fields?

**A:** Yes! Create a custom provider class in `providers/{your_category}/` and register it in `KEY_LABEL_REGISTRY`.

### Q: What's the difference between `blank_percentage` and `nullable`?

**A:** We use `blank_percentage` (0–100) to control how many records have empty values for a field.

### Q: How do I query generated data?

**A:** Export to DuckDB, then query with SQL:

```python
import duckdb
results = duckdb.sql("SELECT * FROM 'output/users.duckdb' WHERE age > 25").fetchall()
```

### Q: Can I regenerate the exact same data?

**A:** Not yet. Each run generates different data. (Seed support is planned for future releases.)

### Q: What if I need a field that doesn't exist?

**A:** Use the `lambda` provider for custom logic:

```python
{
    "key_label": "lambda",
    "options": {
        "function": lambda: f"CUSTOM_{random.randint(1000, 9999)}"
    }
}
```

---

## Roadmap

- 🔄 Seed support for reproducible datasets
- 🔗 Foreign key support for relational data
- 📊 Better performance for 100M+ records
- 🤖 AI-powered schema suggestions
- 🎨 GUI for schema builder
- 📈 Dataset profiling and statistics

---

## Thanks

Built with ❤️ for developers who hate dummy data.

Happy generating! 🎲

---

**Last updated:** June 2026
