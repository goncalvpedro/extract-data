from .db import connect_to_db

def insert_scraped_products(products):
    conn = connect_to_db()
    if not conn:
        print("No DB connection.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS scraped_products (
                            id SERIAL PRIMARY KEY,
                            product_name TEXT,
                            price TEXT,
                            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        for item in products:
            cursor.execute(
                '''INSERT INTO scraped_products (product_name, price) VALUES (%s, %s)''',
                (item["Product"], item["Price"])
            )

        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted into database.")
    except Exception as e:
        print(f"Database insertion error: {e}")
