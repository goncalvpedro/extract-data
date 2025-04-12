import os
import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from database.materials import read_materials
from database.scraped_products import insert_scraped_products


class ProductScraper:
    def __init__(self, headless=True):
        self.browser = self.get_browser(headless)
        self.wait = WebDriverWait(self.browser, 10)
        self.product_data = []
        self.data = self.load_materials()

    def get_browser(self, headless):
        options = Options()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    def load_materials(self):
        materials = read_materials()
        print(materials)
        if materials:
            return pd.DataFrame([m[1] for m in materials], columns=["Itens"])
        else:
            raise Exception("No materials found or failed to load materials.")

    def open_browser(self):
        self.browser.get(config.SCRAPING_SOURCE)

    def accept_cookies(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, config.COOKIES_ID)))
            cookie_button.click()
            print("Cookies accepted.")
        except Exception:
            print("No cookie popup found.")

    def scrape_items(self):
        for index, item in enumerate(self.data["Itens"], 1):
            try:
                search_box = self.wait.until(EC.presence_of_element_located((By.ID, config.SEARCH_ID)))
                time.sleep(2)
                search_box.clear()
                search_box.send_keys(item)
                search_box.send_keys(Keys.ENTER)
                time.sleep(2)

                product_name = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, config.XPATH_PRODUCT_NAME))
                ).text
                product_price = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, config.XPATH_PRODUCT_PRICE))
                ).text

                print(f"Retrieved {index}/{len(self.data)}: {product_name} / {product_price}")
                self.product_data.append({"Product": product_name, "Price": product_price})
            except Exception as e:
                print(f"Error retrieving {item} ({index}/{len(self.data)}): {e}")
                self.product_data.append({"Product": item, "Price": "Not found"})

        return self.product_data

    def store_data(self):
        insert_scraped_products(self.product_data)

    def close(self):
        self.browser.quit()


if __name__ == "__main__":
    scraper = ProductScraper()
    scraper.open_browser()
    scraper.accept_cookies()
    scraper.scrape_items()
    scraper.store_data()
    scraper.close()
