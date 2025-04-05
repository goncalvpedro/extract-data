import pandas as pd
import os

BASE_URL = '01_web_scraping\data'

dirs = os.listdir(BASE_URL)


def analysis(data):
    data = data.drop_duplicates().reset_index(drop=True)

    # Dataframe length
    number_of_items = len(data)
    if 'Price' in data.columns:
        not_found = len(data.query('Price == "Not found"'))

        return round((1 - (int(not_found)/int(number_of_items))) * 100, 2)

def executioner():
    counter = 0    
    for item in dirs:
        if 'data' in item:
            continue
        data = pd.read_csv(f'{BASE_URL}\{item}')
        result = analysis(data)
        counter = counter + 1
        print(f'{counter}/{len(dirs)-1}: Null values for file {item} ({len(data)} rows): {result}%')

executioner()