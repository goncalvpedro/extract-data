from .db import connect_to_db


def verify_materials_table():
    conn = connect_to_db()
    if not conn:
        print("Failed to connect to DB.")
        return None

    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS materials (
                id SERIAL PRIMARY KEY,
                description VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP        
            )
        ''')
        
        conn.commit()
        cursor.close()
        return conn
    except Exception as e:
        print(f"Error ensuring table exists: {e}")
        return None


def read_materials():
    conn = verify_materials_table()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM materials;")
        materials = cursor.fetchall()
        cursor.close()
        conn.close()

        if materials:
            return materials

    except Exception as e:
        print(f"Unable to read materials: {e}")
        return []
