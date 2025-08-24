# logic/exporter.py

import csv
import os
from datetime import datetime

def export_bill_to_csv(order_id, item, quantity, price, total, folder="bills"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/bill_{order_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Order ID", "Item", "Quantity", "Price", "Total"])
        writer.writerow([order_id, item, quantity, price, total])

    return filename
# logic/exporter.py (add this below export_bill_to_csv)

import json

def export_bill_to_json(order_id, item, quantity, price, total, folder="bills"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/bill_{order_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    bill_data = {
        "order_id": order_id,
        "item": item,
        "quantity": quantity,
        "price": price,
        "total": total,
        "timestamp": datetime.now().isoformat()
    }

    with open(filename, mode='w') as file:
        json.dump(bill_data, file, indent=4)

    return filename
