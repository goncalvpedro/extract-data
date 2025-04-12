import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    try:
        conn = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise e