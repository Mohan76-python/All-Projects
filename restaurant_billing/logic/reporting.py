# logic/reporting.py

import os
import csv
import json
from datetime import datetime
from collections import defaultdict

def generate_daily_summary(folder="bills"):
    summary = defaultdict(lambda: {"orders": 0, "revenue": 0})

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        try:
            if filename.endswith(".csv"):
                with open(filepath, newline='') as file:
                    reader = csv.DictReader(file)
                    row = next(reader)
                    date = filename.split("_")[2]  # Extract YYYYMMDD
                    date = datetime.strptime(date, "%Y%m%d").date()
                    summary[date]["orders"] += 1
                    summary[date]["revenue"] += int(row["Total"])

            elif filename.endswith(".json"):
                with open(filepath) as file:
                    data = json.load(file)
                    date = datetime.fromisoformat(data["timestamp"]).date()
                    summary[date]["orders"] += 1
                    summary[date]["revenue"] += int(data["total"])

        except Exception as e:
            print(f"⚠️ Skipped {filename}: {e}")

    return summary
# logic/reporting.py

import sqlite3
from datetime import datetime

def generate_report(order_items, db_path='restaurant.db'):
    total = 0
    for item in order_items:
        qty = int(item['quantity'])
        price = int(item['price'])
        total += qty * price

    tax = round(total * 0.05, 2)
    discount = round(total * 0.10, 2) if total > 500 else 0
    final_total = round(total + tax - discount, 2)

    # Log to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reports (total, tax, discount, final_total, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (total, tax, discount, final_total, datetime.now().isoformat()))
    conn.commit()
    conn.close()

    return {
        'total': total,
        'tax': tax,
        'discount': discount,
        'final_total': final_total
    }

order = [
    {'item': 'Pizza', 'quantity': 2, 'price': 200},
    {'item': 'Fries', 'quantity': 1, 'price': 50}
]

summary = generate_report(order)
print(summary)
