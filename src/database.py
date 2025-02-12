# database.py - Database connection for QuanthereumX
# Author: Przemek Buczek

import psycopg2
from psycopg2 import sql
from config import DATABASE

def connect_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=DATABASE["host"],
            port=DATABASE["port"],
            user=DATABASE["user"],
            password=DATABASE["password"],
            dbname=DATABASE["database"]
        )
        print("✅ Database connection established successfully!")
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None

def close_db(conn):
    """Close the database connection."""
    if conn:
        conn.close()
        print("✅ Database connection closed.")

# Example usage
if __name__ == "__main__":
    conn = connect_db()
    if conn:
        close_db(conn)
