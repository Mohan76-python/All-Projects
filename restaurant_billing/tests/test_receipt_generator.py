import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.formatter import format_receipt
from datetime import datetime

def test_receipt_formatting():
    bill = {
    'bill_id': 1,
    'customer_name': 'Test User',
    'bill_date': datetime.strptime('2025-08-14', '%Y-%m-%d'),
    'payment_mode': 'Cash',
    'remarks': 'Test',
    'total_amount': 100.0
}
    items = [
        {'item_name': 'Test Item', 'quantity': 2, 'price_per_unit': 50.0, 'total_price': 100.0}
    ]
    receipt = format_receipt(bill, items)
    assert "Test Item" in receipt
    assert "₹100.00" in receipt
    

