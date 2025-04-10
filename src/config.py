from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from pathlib import Path
from datetime import datetime as dt

# Current timestamp formatted
NOW = dt.now().strftime("%Y-%m-%d_%H-%M-%S")

# Base project path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

CSV_URL = PROJECT_ROOT / 'materials.csv'

SCRAPE_FOLDER = PROJECT_ROOT / 'scraping'
ANALYSIS_FOLDER = PROJECT_ROOT / 'analysis'
DATA_FOLDER = PROJECT_ROOT / 'data'
RAW_DATA_FOLDER = DATA_FOLDER / 'raw'
PROCESSED_DATA_FOLDER = DATA_FOLDER / 'processed'

# SOURCE
SCRAPING_SOURCE = 'https://www.dentalcremer.com.br/'

# HTML elements
COOKIES_ID = 'onetrust-accept-btn-handler'
SEARCH_ID = 'search'

XPATH_PRODUCT_TILE = '//*[@id="linx-search"]/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div'
# XPATH_PRODUCT_NAME = '/html/body/div[2]/main/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div/div[1]/h2/strong/a/span'
# XPATH_PRODUCT_PRICE = '/html/body/div[2]/main/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div/div[1]/div[3]/div/span[2]/span/span/span'
XPATH_PRODUCT_NAME = "//strong[@class='name product-item-name']/a/span"
XPATH_PRODUCT_PRICE = "//span[@class='price-container price-final_price tax weee']//span[@class='price']"

# Output filename
PRODUCT_PRICE_FILENAME = RAW_DATA_FOLDER / f'{NOW}_product_prices.csv'

def get_browser():
    options = Options()
    options.add_argument("--headless")
    return Service(GeckoDriverManager().install()), options