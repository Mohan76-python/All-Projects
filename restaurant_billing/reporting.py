def view_reports(db_connection):
    cursor = db_connection.cursor()
    
    # Total sales
    cursor.execute("SELECT SUM(total_amount) FROM bills")
    total_sales = cursor.fetchone()[0] or 0

    # Number of orders
    cursor.execute("SELECT COUNT(*) FROM bills")
    order_count = cursor.fetchone()[0]

    # Most popular items
    cursor.execute("""
        SELECT item_name, COUNT(*) as count 
        FROM bill_items 
        GROUP BY item_name 
        ORDER BY count DESC 
        LIMIT 5
    """)
    popular_items = cursor.fetchall()

    print(f"\n📋 Daily Report:")
    print(f"Total Sales: ₹{total_sales}")
    print(f"Number of Orders: {order_count}")
    print("Top 5 Items:")
    for item, count in popular_items:
        print(f" - {item}: {count} orders")
