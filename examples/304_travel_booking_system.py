"""
304_travel_booking_system.py - Travel & Hotel Booking Platform

Complete travel platform with flights, hotels, bookings, and reviews.
"""

from ikidatagen import IkiDataGenerator

print("✈️ Generating travel booking system data...")

# Airlines & Flights
flight_schema = [
    "row_number",
    {
        "key_label": "airline_name",
        "label": "Airline",
    },
    {
        "key_label": "airport_code",
        "label": "Departure Airport",
    },
    {
        "key_label": "airport_code",
        "label": "Arrival Airport",
    },
    {
        "key_label": "current_timestamp",
        "label": "Departure Time",
    },
    {
        "key_label": "current_timestamp",
        "label": "Arrival Time",
    },
    {
        "key_label": "number",
        "label": "Available Seats",
        "options": {"min": 0, "max": 500}
    },
    {
        "key_label": "money",
        "label": "Price",
    },
]

# Hotels
hotel_schema = [
    "row_number",
    {
        "key_label": "hotel_name",
        "label": "Hotel",
    },
    "city",
    "country",
    {
        "key_label": "number",
        "label": "Stars",
        "options": {"min": 1, "max": 5}
    },
    {
        "key_label": "number",
        "label": "Available Rooms",
        "options": {"min": 0, "max": 500}
    },
    {
        "key_label": "money",
        "label": "Price per Night",
    },
    {
        "key_label": "number",
        "label": "Rating",
        "options": {"min": 1, "max": 5}
    },
]

# Bookings
booking_schema = [
    "row_number",
    {
        "key_label": "current_timestamp",
        "label": "Booking Date",
    },
    "first_name",
    "last_name",
    "email_address",
    {
        "key_label": "hotel_name",
        "label": "Hotel",
    },
    {
        "key_label": "current_timestamp",
        "label": "Check-in",
    },
    {
        "key_label": "current_timestamp",
        "label": "Check-out",
    },
    {
        "key_label": "number",
        "label": "Rooms",
        "options": {"min": 1, "max": 10}
    },
    {
        "key_label": "money",
        "label": "Total Cost",
    },
    {
        "key_label": "custom_list",
        "label": "Status",
        "options": {"values": ["Confirmed", "Pending", "Cancelled"]}
    },
]

# Reviews
review_schema = [
    "row_number",
    {
        "key_label": "hotel_name",
        "label": "Hotel",
    },
    "username",
    {
        "key_label": "number",
        "label": "Rating",
        "options": {"min": 1, "max": 5}
    },
    {
        "key_label": "words",
        "label": "Title",
    },
    {
        "key_label": "paragraphs",
        "label": "Review",
    },
    {
        "key_label": "current_timestamp",
        "label": "Date",
    },
]

print("[OK] Generating 300 flights...")
IkiDataGenerator(flight_schema).many(300).export(
    "travel_flights", formats=["csv"])

print("[OK] Generating 200 hotels...")
IkiDataGenerator(hotel_schema).many(200).export(
    "travel_hotels", formats=["csv"])

print("[OK] Generating 1000 bookings...")
IkiDataGenerator(booking_schema).many(1000).export(
    "travel_bookings", formats=["csv"])

print("[OK] Generating 500 reviews...")
IkiDataGenerator(review_schema).many(500).export(
    "travel_reviews", formats=["csv", "json"])

print("\n[OK] Travel booking system generated!")
