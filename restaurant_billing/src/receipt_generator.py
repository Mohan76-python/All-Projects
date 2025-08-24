import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
from src.db.db_connector import get_connection
from src.utils.formatter import format_receipt
from src.utils.pdf_generator import generate_pdf_receipt  # ✅ Import here

def generate_receipt(bill_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Fetch bill
    cursor.execute("SELECT * FROM bills WHERE bill_id = %s", (bill_id,))
    bill = cursor.fetchone()
    if not bill:
        print(f"No bill found with ID {bill_id}")
        return

    # Fetch items
    cursor.execute("SELECT * FROM bill_items WHERE bill_id = %s", (bill_id,))
    items = cursor.fetchall()

    # Format and print
    receipt_text = format_receipt(bill, items)
    print(receipt_text)

    # ✅ Generate PDF
    pdf_path = generate_pdf_receipt(bill, items)
    print(f"\n✅ PDF receipt saved to: {pdf_path}")

    # ✅ Debug: Print item keys
    for item in items:
        print("Item keys:", item.keys())

    cursor.close()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate receipt for a given bill ID")
    parser.add_argument("--bill_id", type=int, required=True, help="Bill ID to generate receipt for")
    args = parser.parse_args()

    generate_receipt(args.bill_id)
