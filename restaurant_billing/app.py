from utils.db_utils import create_tables, load_menu_from_csv

def main():
    print("📦 Initializing Restaurant Billing Database...")
    create_tables()
    load_menu_from_csv()
    print("✅ Database setup complete!")

if __name__ == "__main__":
    main()
