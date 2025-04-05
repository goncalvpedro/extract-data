from database import conn
import pandas as pd

conn = conn

data = pd.read_csv(r'01_selenium_scraping\data\data.csv')
cursor = conn.cursor()

for item in data['Itens']:
    item = str(item)
    cursor.execute('''
        INSERT INTO materials (description) VALUES (%s)
    ''', (item,))

conn.commit()
cursor.close()
conn.close()
