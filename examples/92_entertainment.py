"""
92_entertainment.py - Movies, Books, Music, & Entertainment Data

Movie reviews, book catalog, music library data.
"""

from ikidatagen import IkiDataGenerator

print("[FILM] Generating entertainment data...")

# Movies
movie_schema = [
    "row_number",
    {
        "key_label": "movie_title",
        "label": "Title",
    },
    {
        "key_label": "movie_genre",
        "label": "Genre",
    },
    {
        "key_label": "number",
        "label": "Year",
        "options": {"min": 1980, "max": 2024}
    },
    {
        "key_label": "number",
        "label": "Runtime (min)",
        "options": {"min": 80, "max": 240}
    },
    {
        "key_label": "number",
        "label": "Rating",
        "options": {"min": 1, "max": 10}
    },
    {
        "key_label": "number",
        "label": "Votes",
        "options": {"min": 100, "max": 1000000}
    },
]

# Books
book_schema = [
    "row_number",
    {
        "key_label": "book_title",
        "label": "Title",
    },
    {
        "key_label": "author_name",
        "label": "Author",
    },
    {
        "key_label": "isbn",
        "label": "ISBN",
    },
    {
        "key_label": "number",
        "label": "Pages",
        "options": {"min": 50, "max": 1000}
    },
    {
        "key_label": "number",
        "label": "Year",
        "options": {"min": 1900, "max": 2024}
    },
    {
        "key_label": "number",
        "label": "Rating",
        "options": {"min": 1, "max": 5}
    },
]

# Music
music_schema = [
    "row_number",
    {
        "key_label": "song_title",
        "label": "Song",
    },
    {
        "key_label": "artist_name",
        "label": "Artist",
    },
    {
        "key_label": "album_name",
        "label": "Album",
    },
    {
        "key_label": "music_genre",
        "label": "Genre",
    },
    {
        "key_label": "number",
        "label": "Year",
        "options": {"min": 1960, "max": 2024}
    },
    {
        "key_label": "number",
        "label": "Duration (seconds)",
        "options": {"min": 120, "max": 600}
    },
]

print("[OK] Generating 500 movies...")
IkiDataGenerator(movie_schema).many(500).export(
    "entertainment_movies", formats=["csv", "json"])

print("[OK] Generating 1000 books...")
IkiDataGenerator(book_schema).many(1000).export(
    "entertainment_books", formats=["csv", "json"])

print("[OK] Generating 2000 songs...")
IkiDataGenerator(music_schema).many(2000).export(
    "entertainment_music", formats=["csv", "json"])

print("\n[OK] Entertainment data generated!")
