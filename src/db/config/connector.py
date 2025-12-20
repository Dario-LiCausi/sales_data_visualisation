import os
from pathlib import Path
from mysql.connector import connect, Error
from dotenv import load_dotenv

# load the .env
PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")


# connect to mysql
class LoadDB:
    @staticmethod
    def login_db():
        try:
            db_name = os.getenv("MYSQL_DB") or os.getenv("MYSQL_DATABASE")
            conn = connect(
                host=os.getenv("MYSQL_HOST", "127.0.0.1"),
                port=int(os.getenv("MYSQL_PORT", 3307)),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=db_name,
            )
            print("Connection successful")
            return conn
        except Error as e:
            print(f"Connection error: {e}")
            return None
