from pathlib import Path
from datetime import datetime as dt

# Current timestamp formatted
NOW = dt.now().strftime("%Y-%m-%d_%H-%M-%S")

# Base project path 
PROJECT_URL = Path(r'C:\Projetos\data-engineering\extract-data\01_selenium_scraping')

CSV_URL = PROJECT_URL / 'materials.csv'

SCRAPE_FOLDER = PROJECT_URL / 'scraping'
PIPELINE_FOLDER = PROJECT_URL / 'pipeline'
DATABASE_FOLDER = PROJECT_URL / 'database'
ANALYSIS_FOLDER = PROJECT_URL / 'analysis'
DATA_FOLDER = PROJECT_URL / 'data'
RAW_DATA_FOLDER = DATA_FOLDER / 'raw'
PROCESSED_DATA_FOLDER = DATA_FOLDER / 'processed'

SCRAPING_SOURCE = 'https://www.dentalcremer.com.br/'

# HTML elements
COOKIES_ID = 'onetrust-accept-btn-handler'
SEARCH_ID = 'search'

XPATH_PRODUCT = '//*[@id="linx-search"]/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div'
XPATH_PRODUCT_NAME = '/html/body/div[2]/main/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div/div[1]/h2/strong/a/span'
XPATH_PRODUCT_PRICE = '/html/body/div[2]/main/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div/div[1]/div[3]/div/span[2]/span/span/span'

# Output filename
PRODUCT_PRICE_FILENAME = RAW_DATA_FOLDER / f'{NOW}_product_prices.csv'
