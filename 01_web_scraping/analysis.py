import pandas as pd

data = pd.read_csv('01_web_scraping\data\product_prices1.csv')

# Removing duplicates
duplicates = data.value_counts()
data = data.drop_duplicates().reset_index(drop=True)

# Dataframe length
number_of_items = len(data['Product'])

# Number of "Not found" results
not_found = data.query('Price == "Not found"')['Price'].count()

# Perfomance result

result = (1 - (int(not_found)/int(number_of_items))) * 100

print(f'Current performance pct: {round(result, 2)}%')
