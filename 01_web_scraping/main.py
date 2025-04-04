import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime as dt
from analysis import executioner
data = pd.read_csv('01_web_scraping/data/data.csv')

options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=options)


browser.get('https://www.dentalcremer.com.br/')
wait = WebDriverWait(browser, 10)

try:
    cookie_button = wait.until(EC.element_to_be_clickable(
        (By.ID, 'onetrust-accept-btn-handler')))
    cookie_button.click()
    print("Cookies accepted.")
except:
    print("No cookie popup found.")

product_data = []
itens_amount = len(data['Itens'])
counter = 0

for item in data['Itens']:
    counter = counter + 1
    try:
        search_box = wait.until(
            EC.presence_of_element_located((By.ID, 'search')))
        search_box.clear()
        search_box.send_keys(item)
        search_box.send_keys(Keys.ENTER)

    except Exception as e:
        print(f'Item {item} not found.')

    time.sleep(2)

    try:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="linx-search"]/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div')))
        time.sleep(2)

        product_name = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/main/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div/div[1]/h2/strong/a/span'))).text

        product_price = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/main/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[3]/ol/li[1]/div/div[1]/div[3]/div/span[2]/span/span/span'))).text

        product_price = product_price.replace('R$', '')

        print(
            f"Retrieved {counter}/{itens_amount}: {product_name} - {product_price}")
        product_data.append({"Product": product_name, "Price": product_price})

    except Exception as e:
        print(
            f"Could not find item {item} ({counter}/{itens_amount}) due an error: {e}")
        product_data.append({"Product": item, "Price": "Not found"})

df = pd.DataFrame(product_data)
now = str(dt.now()).replace(' ', '_').replace(':', '_').split('.')[0]
df.to_csv(
    f'01_web_scraping/data/{now}_product_prices.csv', index=False)
print("Data saved to product_prices.csv")

browser.quit()

executioner()
