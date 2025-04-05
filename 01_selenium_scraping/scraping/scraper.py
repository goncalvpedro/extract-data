from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config


data = pd.read_csv(config.CSV_URL)


def get_browser():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(service=Service(
        GeckoDriverManager().install()), options=options)


browser = get_browser()

browser.get(config.SCRAPING_SOURCE)
wait = WebDriverWait(browser, 10)


def accept_cookies():

    try:
        cookie_button = wait.until(EC.element_to_be_clickable(
            (By.ID, config.COOKIES_ID)))
        cookie_button.click()
        print("Cookies accepted.")
    except:
        print("No cookie popup found.")


product_data = []
itens_amount = len(data)


def scrape_item(data):
    counter = 0

    for item in data.iloc[:,0]:
        item = item[1]
        counter = counter + 1

        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, config.SEARCH_ID)))
            search_box.clear()
            search_box.send_keys(item)
            search_box.send_keys(Keys.ENTER)

            time.sleep(2)

            wait.until(EC.presence_of_element_located(
                (By.XPATH, config.XPATH_PRODUCT)))

            time.sleep(2)

            product_name = wait.until(EC.presence_of_element_located(
                (By.XPATH, config.XPATH_PRODUCT_NAME))).text

            product_price = wait.until(EC.presence_of_element_located(
                (By.XPATH, config.XPATH_PRODUCT_PRICE))).text

            product_price = product_price.replace('R$', '').strip()

            print(
                f"Retrieved {counter}/{itens_amount}: {product_name} - {product_price}")
            product_data.append(
                {"Product": product_name, "Price": product_price})

        except Exception as e:
            print(
                f"Could not find item {item} ({counter}/{itens_amount}) due an error: {e}")
            product_data.append(
                {"Product": item, "Price": "Not found"})

    return product_data


product_data = scrape_item(data)

df = pd.DataFrame(product_data)

now = config.NOW

df.to_csv(
    config.PRODUCT_PRICE_FILENAME, index=False)

browser.quit()
