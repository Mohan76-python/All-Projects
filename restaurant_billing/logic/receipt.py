# logic/receipt.py

from datetime import datetime

def generate_receipt(item: str, quantity: int, price: int, total: int) -> str:
    """Generate a formatted receipt string."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"🧾 Receipt\n"
        f"----------------------\n"
        f"Item      : {item}\n"
        f"Quantity  : {quantity}\n"
        f"Unit Price: ₹{price}\n"
        f"Total     : ₹{total}\n"
        f"Time      : {timestamp}\n"
        f"----------------------\n"
        f"Thank you for your order!"
    )
