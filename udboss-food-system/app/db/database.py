import sqlite3

DATABASE_NAME = "udboss.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # returns dict-like rows
    return conn



def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Farmers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS farmers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT
    )
    """)

    # Crops table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_id INTEGER,
        crop TEXT,
        expected_harvest_date TEXT,
        quantity INTEGER,
        status TEXT,
        FOREIGN KEY(farmer_id) REFERENCES farmers(id)
    )
    """)

    # Market prices table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS market_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        market TEXT,
        crop TEXT,
        date TEXT,
        price INTEGER
    )
    """)
# Feedback table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        crop_id INTEGER,
        actual_price INTEGER,
        sold_date TEXT,
        FOREIGN KEY(crop_id) REFERENCES crops(id)
    )
    """)
    conn.commit()
    conn.close()