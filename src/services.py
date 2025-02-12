# services.py - Core business logic for QuanthereumX
# Author: Przemek Buczek

from database import connect_db, close_db
from errors import DatabaseConnectionError
from logger import get_logger

logger = get_logger()

def fetch_data(query):
    """Fetch data from the database based on the given query."""
    conn = None
    try:
        conn = connect_db()
        if not conn:
            raise DatabaseConnectionError("Could not establish database connection.")
        
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        logger.info(f"✅ Successfully fetched data: {result}")
        return result

    except DatabaseConnectionError as e:
        logger.error(f"❌ {e}")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
    finally:
        if conn:
            close_db(conn)

def process_data(data):
    """Process data (example: simple transformation)."""
    try:
        processed = [str(item).upper() for item in data]
        logger.info(f"✅ Processed data: {processed}")
        return processed
    except Exception as e:
        logger.error(f"❌ Data processing error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    test_query = "SELECT * FROM users;"  # Example query
    raw_data = fetch_data(test_query)
    if raw_data:
        process_data(raw_data)
      
