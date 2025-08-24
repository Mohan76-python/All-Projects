# logic/database.py

import sqlite3
import os

DB_PATH = os.path.join("..", "db", "orders.db")

def init_db():
    """Create orders table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            total INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_order(item: str, quantity: int, total: int):
    """Insert a new order into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO orders (item, quantity, total)
        VALUES (?, ?, ?)
    """, (item, quantity, total))
    conn.commit()
    conn.close()
from unittest.mock import patch

@patch('reporting.log_to_db')  # Replace with actual path
def test_generate_report_logs_to_db(self, mock_log):
    sample_data = [{'item': 'Juice', 'quantity': 1, 'price': 80}]
    generate_report(sample_data)
    mock_log.assert_called_once()
def setUp(self):
    self.sample_data = [
        {'item': 'Burger', 'quantity': 2, 'price': 100},
        {'item': 'Fries', 'quantity': 1, 'price': 50}
    ]
