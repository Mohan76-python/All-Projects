import sqlite3
import pandas as pd

DB_PATH = "db/restaurant.db"

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def create_tables():
    """Create menu, orders, and order_items tables."""
    conn = connect_db()
    cursor = conn.cursor()

    # Menu table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT,
        category TEXT,
        price REAL
    )
    """)

    # Orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mode TEXT,
        payment_method TEXT,
        total REAL,
        gst REAL,
        discount REAL,
        timestamp TEXT
    )
    """)

    # Order items table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        item_id INTEGER,
        quantity INTEGER
    )
    """)

    conn.commit()
    conn.close()

def load_menu_from_csv(csv_path="data/menu.csv"):
    """Load menu items from CSV into the database."""
    df = pd.read_csv(csv_path)
    conn = connect_db()
    df.to_sql("menu", conn, if_exists="replace", index=False)
    conn.close()
