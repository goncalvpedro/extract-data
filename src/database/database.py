import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def connect_to_db(name, username, password, host, port):
    try:
        conn = psycopg2.connect(
            database=name,
            user=username,
            password=password,
            host=host,
            port=port
        )

        return conn

    except Exception as e:
        return {'error': f'Unable to connect to the database due an error: {e}', 'status': 500}


def create_table(conn, table_name):
    try:
        cursor = conn.cursor()

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                description VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        cursor.close()
        conn.close()

        return {'message': f'Table {table_name} created successfully.'}

    except Exception as e:
        return {'error': f'Unable to create the table due an error: {e}'}


conn = connect_to_db(DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT)
