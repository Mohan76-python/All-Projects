# logic/billing.py

def calculate_total(menu: dict, item: str, quantity: int) -> int:
    """Calculate total price for given item and quantity."""
    if item not in menu:
        raise ValueError(f"Item '{item}' not found in menu.")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    return menu[item] * quantity
