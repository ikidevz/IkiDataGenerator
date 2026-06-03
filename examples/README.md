# 📚 Iki Data Generator Examples

This folder contains 50+ example scripts demonstrating all features and providers of Iki Data Generator. Run any example to generate sample datasets.

## Quick Navigation

### 🚀 Getting Started (Beginner)

- [00_quick_start.py](00_quick_start.py) – Simplest possible example (1 min)
- [01_basic_fields.py](01_basic_fields.py) – Common fields explained
- [02_simple_export.py](02_simple_export.py) – Export to different formats

### 👤 Personal & Identity Data

- [10_personal_data.py](10_personal_data.py) – Names, gender, dates of birth
- [11_contact_info.py](11_contact_info.py) – Email, phone, social media
- [12_identity_documents.py](12_identity_documents.py) – Passport, SSN, ID numbers

### 🛍️ Commerce & E-Commerce

- [20_ecommerce_shop.py](20_ecommerce_shop.py) – Products, orders, customers
- [21_shopping_cart.py](21_shopping_cart.py) – Shopping history with items
- [22_inventory_management.py](22_inventory_management.py) – Stock levels, SKU, barcodes
- [23_payment_processing.py](23_payment_processing.py) – Credit cards, invoices, payments

### 💰 Finance & Banking

- [30_bank_accounts.py](30_bank_accounts.py) – Savings, checking, accounts
- [31_credit_cards.py](31_credit_cards.py) – Card numbers, types, issuers
- [32_transactions.py](32_transactions.py) – Bank transfers, deposits, withdrawals
- [33_investment_portfolio.py](33_investment_portfolio.py) – Stocks, crypto, bonds
- [34_currency_exchange.py](34_currency_exchange.py) – Multi-currency data

### 🏥 Healthcare & Medical

- [40_patient_records.py](40_patient_records.py) – Patient demographics, medical history
- [41_medical_diagnosis.py](41_medical_diagnosis.py) – ICD codes, diagnoses, symptoms
- [42_medications.py](42_medications.py) – Prescriptions, dosages, side effects
- [43_hospital_visits.py](43_hospital_visits.py) – Appointments, procedures, billing

### 🌍 Location & Geography

- [50_addresses.py](50_addresses.py) – Street addresses, postal codes, coordinates
- [51_international_data.py](51_international_data.py) – Countries, cities, regions
- [52_travel_destinations.py](52_travel_destinations.py) – Airports, hotels, landmarks
- [53_weather_locations.py](53_weather_locations.py) – Weather conditions by location

### 📚 Education & Learning

- [60_student_records.py](60_student_records.py) – Student info, enrollment, grades
- [61_courses_curriculum.py](61_courses_curriculum.py) – Courses, subjects, degrees
- [62_university_data.py](62_university_data.py) – Universities, majors, graduation

### 🚗 Automotive & Vehicles

- [70_car_inventory.py](70_car_inventory.py) – Cars, models, years, prices
- [71_vehicle_registration.py](71_vehicle_registration.py) – VIN, license plates, owners
- [72_vehicle_maintenance.py](72_vehicle_maintenance.py) – Service records, repairs

### ⚖️ Legal & Compliance

- [80_legal_entities.py](80_legal_entities.py) – Companies, sole proprietors, partnerships
- [81_contracts.py](81_contracts.py) – Agreements, terms, jurisdictions
- [82_compliance_records.py](82_compliance_records.py) – Audit logs, certifications

### 🎮 Entertainment & Gaming

- [90_gaming_players.py](90_gaming_players.py) – Gamers, characters, guilds
- [91_game_inventory.py](91_game_inventory.py) – Items, equipment, quests
- [92_movies_books.py](92_movies_books.py) – Movies, books, authors, ratings
- [93_music_artists.py](93_music_artists.py) – Musicians, albums, genres

### 💻 Tech & IT

- [100_programming_data.py](100_programming_data.py) – Languages, frameworks, versions
- [101_software_bugs.py](101_software_bugs.py) – Bug reports, logs, stack traces
- [102_database_tables.py](102_database_tables.py) – Table structures, schemas

### 🤖 AI & Machine Learning

- [110_ml_models.py](110_ml_models.py) – Model types, frameworks, versions
- [111_ml_metrics.py](111_ml_metrics.py) – Accuracy, latency, confidence scores
- [112_training_data.py](112_training_data.py) – Datasets, features, labels

### ✨ Advanced Features

- [200_templates.py](200_templates.py) – Combining fields with templates
- [201_regex_patterns.py](201_regex_patterns.py) – Custom patterns with regex
- [202_lambda_functions.py](202_lambda_functions.py) – Custom Python logic
- [203_blank_percentages.py](203_blank_percentages.py) – Missing data and nulls

### 🌐 Real-World Scenarios

- [300_saas_users.py](300_saas_users.py) – SaaS platform users, subscriptions, usage
- [301_social_network.py](301_social_network.py) – Social media platform data
- [302_analytics_events.py](302_analytics_events.py) – Event tracking, analytics
- [303_ecommerce_platform.py](303_ecommerce_platform.py) – Full e-commerce system
- [304_ride_sharing.py](304_ride_sharing.py) – Ride-sharing app data
- [305_dating_app.py](305_dating_app.py) – Dating platform profiles
- [306_streaming_service.py](306_streaming_service.py) – Video streaming service
- [307_bank_system.py](307_bank_system.py) – Complete banking system
- [308_hospital_system.py](308_hospital_system.py) – Full hospital network
- [309_school_system.py](309_school_system.py) – Complete school/university

### 📊 Multi-Category Examples

- [400_mixed_categories.py](400_mixed_categories.py) – Combining 5+ categories
- [401_batch_processing.py](401_batch_processing.py) – Generate multiple datasets
- [402_export_all_formats.py](402_export_all_formats.py) – Export to all formats
- [403_large_dataset.py](403_large_dataset.py) – Generating 1M+ records

### 🔍 Specialized Use Cases

- [500_test_data_testing.py](500_test_data_testing.py) – Unit test fixtures
- [501_load_testing_data.py](501_load_testing_data.py) – Load testing datasets
- [502_demo_data.py](502_demo_data.py) – Demo/presentation data
- [503_data_migration.py](503_data_migration.py) – Data migration scenarios
- [504_api_response_mocking.py](504_api_response_mocking.py) – API response samples

## Running Examples

### Run a single example:

```bash
python examples/00_quick_start.py
```

### Run all examples:

```bash
python -m examples.*
```

### Run examples by category:

```bash
python examples/20_ecommerce_shop.py     # E-commerce
python examples/110_ml_metrics.py         # AI/ML
python examples/300_saas_users.py         # Real-world scenario
```

## Generated Output

All examples save data to `output/` folder:

```
output/
├── quick_start.csv
├── quick_start.json
├── personal_users.csv
├── ecommerce_orders.parquet
└── ... (more files)
```

## Tips

1. **Start Simple** – Begin with `00_quick_start.py` and work up
2. **Copy & Modify** – Use examples as templates for your own schemas
3. **Mix & Match** – Combine fields from different categories
4. **Check Output** – View generated files in `output/` folder
5. **Experiment** – Try different `blank_percentage` and export formats

## Learning Path

```
Beginner:   00 → 01 → 02 → 10 → 20 → 30
Intermediate: 40 → 50 → 60 → 200 → 201
Advanced:   300 → 301 → 400 → 401 → 403
```

---

**Have fun generating data!** 🎲
