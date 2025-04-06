import pandas as pd
import os

BASE_URL = r'01_selenium_scraping\data\raw'

dirs = os.listdir(BASE_URL)


def analysis(data):
    data = data.drop_duplicates().reset_index(drop=True)
    data = data.fillna('Not found')

    number_of_items = len(data)
    if 'Price' in data.columns:
        not_found = len(data.query('Price == "Not found"'))
        return (round((1 - (int(not_found)/int(number_of_items))) * 100, 2), number_of_items)

def executioner():
    counter = 0    
    for item in dirs:
        if 'data' in item:
            continue
        data = pd.read_csv(f'{BASE_URL}\{item}')
        result_tuple = analysis(data)
        result = result_tuple[0]
        len_data = result_tuple[1]
        counter = counter + 1
        print(f'{counter}/{len(dirs)}: Null values for file {item} ({len_data} rows): {result}%')

executioner()