import logging
import os
from datetime import datetime
from .db_config import get_connection

# Setup logging
log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def insert_report(total, gst, discount, final_amount):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO reports (total, gst, discount, final_amount, timestamp)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (total, gst, discount, final_amount, datetime.now())
        cursor.execute(query, values)
        conn.commit()
        logging.info("✅ Report inserted successfully.")

    except Exception as err:
        logging.error(f"❌ MySQL Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
