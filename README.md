# Extract Data: A Web Scraping Tool with Selenium and Pandas

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-%23430098.svg?style=flat&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Docker](https://img.shields.io/badge/BeautifulSoup-4.x-green.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/goncalvpedro/extract-data)
![GitHub stars](https://img.shields.io/github/stars/goncalvpedro/extract-data?style=social)

## Overview

**Extract Data** is a Python-based web scraping tool designed to efficiently extract information from websites. It leverages the power of **Selenium** for dynamic content rendering, **PostgreSQL** to storage scraped information and **Pandas** for structured data manipulation, all of this inside **Docker Containers**.

## Key Features

* **Dynamic Content Handling:** Utilizes Selenium to interact with web pages that rely heavily on JavaScript, ensuring accurate data retrieval even for dynamically loaded content.
* **Structured Data Output:** 
* **CSS Selector Based Extraction:** Uses CSS selectors (and optionally XPath) for precise targeting of HTML elements, making the scraping process robust and adaptable.
* **Modular Design:** The codebase is structured to promote reusability and easy modification for different scraping tasks.
* **Clear and Concise Code:** Written with readability and maintainability in mind.

## Stacks Applied

This project utilizes the following technologies:

* **Python (>= 3.12):** The primary programming language used for the entire project.
* **Selenium:** A powerful browser automation library used to interact with web pages, handle JavaScript rendering, and navigate complex websites.
* **Pandas:** A data manipulation and analysis library providing efficient data structures (like DataFrames) for storing and working with extracted data.
* **Webdriver Manager:** A library that automatically manages browser drivers (e.g., ChromeDriver, GeckoDriver) required by Selenium, simplifying the setup process.
* **PostgreSQL**
* **Docker**

## Quick Note About Web Scraping with Selenium

When dealing with modern web applications, much of the content is loaded dynamically using JavaScript. Traditional scraping libraries that only parse the static HTML source often fail to capture this dynamically generated data. **Selenium** overcomes this limitation by actually *driving* a web browser. This allows the JavaScript on the page to execute fully, rendering all the content before the scraping logic is applied.

This approach provides significant advantages for scraping complex websites but also comes with considerations:

* **Resource Usage:** Running a full browser instance can be more resource-intensive (CPU and memory) compared to static HTML parsing.
* **Execution Speed:** Browser automation can be slower than simply downloading and parsing HTML.
* **Setup:** Requires the correct browser driver to be installed and configured (though libraries like `webdriver-manager` helps automate this).
* **Detection:** Websites may employ anti-scraping measures that can detect and block Selenium-driven scraping.  It's crucial to use Selenium responsibly and ethically, respecting the website's terms of service. Techniques like using appropriate waiting times, rotating user agents, and handling CAPTCHAs may be necessary.

Despite these considerations, Selenium is often the most effective solution for extracting data from websites with dynamic content.  It allows for interaction with the page in a way that mimics a real user, making it possible to scrape data that would otherwise be inaccessible.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/goncalvpedro/extract-data.git](https://github.com/goncalvpedro/extract-data.git)
    cd extract-data
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Provide clear and concise instructions on how to use the scripts in your repository. Include examples if possible. For instance:

1.  **Configure the scraping parameters:**
    * Open the main script (e.g., `scraper.py`).
    * Modify the target URL(s) and CSS selectors according to the website you want to scrape.  This often involves inspecting the website's HTML structure using your browser's developer tools. Add more fields as you need to extract more information.
    * Make sure you have Firefox installed locally.
    * Adjust any other relevant settings (e.g., headless mode, waiting times) within the script.  Headless mode (`options.headless = True`) allows Selenium to run without opening a visible browser window.

2.  **Run the scraper:**

    ```bash
    python scraper.py
    ```

3.  **Access the extracted data:**

    * The scraped data will typically be saved to a CSV file (e.g., `output.csv`) in the project directory.  The filename and format can usually be configured within the script.
    * You can then use Pandas or other tools to analyze the generated data.  For example, you could load the CSV file into a Pandas DataFrame for further manipulation:

        ```python
        import pandas as pd
        df = pd.read_csv('output.csv')
        print(df.head())
        ```
4.  **Adapt database tables for your application**

    * Go to **src/database/init.sql** and adapt table creation and initial data seeding. This file is responsible for populating tables before the scraper script tries to read its data. This is important if you are running with **Docker** or else you will receive an error "No materials found or failed to load materials." in line 39 of scraper.py. If you are running locally you can go directly into pgAdmin and create databases, tables and populates them with initial data before running int Python.


5.  **Rebuild Docker Compose**

    * After all changes were made and the script is running fine locally, apply changes in **docker-compose.yml** and compose it.

        ```bash
        docker compose up --build
        ```

## Best Practices

* **Use appropriate waiting times:** Avoid overloading the website's server by adding delays between requests.  Selenium provides methods like `time.sleep()` or explicit waits (`WebDriverWait`) to handle this.
* **Handle exceptions:** Implement error handling to gracefully manage unexpected situations, such as network errors, changes in the website's structure, or anti-scraping measures.
* **Be mindful of data usage:** Ensure that you are using the scraped data ethically and legally, and that you comply with the website's terms of service and any relevant privacy regulations.
* **User-Agent Rotation**:  Websites can identify and block scrapers by looking at the User-Agent header.  Rotating through a list of User-Agent strings can help to avoid detection.
* **Headless Mode**: Running the browser in headless mode (without a GUI) can sometimes help to avoid detection, and it also reduces resource consumption.  However, some sites specifically target headless browsers.


## Contributing

Contributions to this project are welcome! If you have suggestions, bug reports, or would like to add new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Make your modifications and commit them.
4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details.

## Acknowledgements

* The developers and contributors of the Selenium, Pandas, and Beautiful Soup libraries for creating such powerful and versatile tools.
* The `webdriver-manager` library for simplifying browser driver management.

