from db.reports_db import insert_report

insert_report(1200.00, 120.00, 60.00, 1260.00)
print("✅ Report inserted. Check logs/app.log for details.")
def main():
    db_connection = connect_to_database()  # your existing DB connection

    while True:
        print("\n=== Restaurant Billing System ===")
        print("1. Create New Bill")
        print("2. View Reports")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_new_bill(db_connection)
        elif choice == '2':
            view_reports(db_connection)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
