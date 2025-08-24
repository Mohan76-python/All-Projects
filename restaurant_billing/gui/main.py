# main.py

from logic.billing import calculate_total
from logic.exporter import export_bill_to_csv, export_bill_to_json

menu = {
    "Idli": 30,
    "Dosa": 50,
    "Vada": 20
}

print("Welcome to Restaurant Billing System")
item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
order_id = input("Enter order ID: ")
format_choice = input("Export format (csv/json/both): ").lower()

try:
    total = calculate_total(menu, item, quantity)

    if format_choice == "csv":
        filename = export_bill_to_csv(order_id, item, quantity, menu[item], total)
    elif format_choice == "json":
        filename = export_bill_to_json(order_id, item, quantity, menu[item], total)
    elif format_choice == "both":
        csv_file = export_bill_to_csv(order_id, item, quantity, menu[item], total)
        json_file = export_bill_to_json(order_id, item, quantity, menu[item], total)
        filename = f"{csv_file} and {json_file}"
    else:
        raise ValueError("Invalid format choice")

    print(f"\n✅ Bill generated successfully!")
    print(f"🧾 Total: ₹{total}")
    print(f"📁 Saved to: {filename}")

except ValueError as e:
    print(f"❌ Error: {e}")
from logic.reporting import generate_daily_summary

summary = generate_daily_summary()
for date, data in summary.items():
    print(f"{date}: Orders={data['orders']}, Revenue=₹{data['revenue']}")
from db.reports_db import insert_report

# Sample call
insert_report(1000.00, 100.00, 50.00, 1050.00)
from db.reports_db import insert_report

# Sample call
insert_report(1200.00, 120.00, 60.00, 1260.00)
print("✅ Report inserted. Check logs/app.log for details.")
from db.reports_db import insert_report

# Sample call
insert_report(1200.00, 120.00, 60.00, 1260.00)
print("✅ Report inserted. Check logs/app.log for details.")
