def format_receipt(bill, items):
    lines = []
    lines.append(f"\nBill ID: {bill['bill_id']}")
    lines.append(f"Customer: {bill['customer_name']}")
    lines.append(f"Date: {bill['bill_date'].strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Payment Mode: {bill['payment_mode']}")
    lines.append(f"Remarks: {bill['remarks']}\n")

    lines.append("Items:")
    lines.append("-" * 40)
    for i, item in enumerate(items, start=1):
        name = item['item_name']
        qty = item['quantity']
        unit_price = item['price_per_unit']
        total = item['total_price']
        lines.append(f"{i}. {name:<20} x{qty}  ₹{unit_price:.2f} → ₹{total:.2f}")
    lines.append("-" * 40)
    lines.append(f"Total Amount: ₹{bill['total_amount']:.2f}\n")
    lines.append(f"Raw Date: {bill['bill_date'].date()}")  # or any format you prefer
    return "\n".join(lines)
