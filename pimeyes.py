# Import necessary libraries
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import chromedriver_autoinstaller
import os
import re
import random
import json
from os.path import isfile
import sys
from clear_screen import clear

# Function to load settings from a JSON file
def load_settings():
    # Check if proxy file exists
    if not isfile("proxy.txt"):
        # If not, create one with default settings
        with open("proxy.txt", 'w') as proxy_file:
            proxy_file.write("DEFAULT_PROXY")
        print("Proxy file created.")
    # Return the settings
    return

# Function to load proxies from a file
def load_proxies(file_path):
    with open(file_path, 'r') as proxy_file:
        proxies = proxy_file.readlines()
    return proxies

# Function to initialize the webdriver
def initialize_driver(proxy):
    chromedriver_autoinstaller.install()

    # Setup ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Add arguments to make headless browser appear as regular one
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Split the proxy string into components
    proxy_parts = proxy.split(':')
    formatted_proxy = f'{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}'

    # Proxy setup
    proxy_options = {
        'proxy': {
            'https': f'https://{formatted_proxy}',
        }
    }

    # Initialize driver
    driver = webdriver.Chrome(seleniumwire_options=proxy_options, options=options)
    clear()
    return driver

# Function to remove a proxy from the file
def remove_proxy(file_path, proxy):
    with open(file_path, 'r') as f:
        proxies = f.readlines()
    with open(file_path, 'w') as f:
        for p in proxies:
            if p.strip() != proxy:
                f.write(p)

# Initialize driver to None before the try block
driver = None

if __name__ == "__main__":
    try:
        # Check if a file path was provided as an argument
        if len(sys.argv) > 1:
            path = sys.argv[1]
        else:
            path = str(input("Please enter a filename: "))

        # Check if the file exists in the same directory
        if not os.path.isfile(os.path.join(os.path.dirname(__file__), path)):
            print("File not found in the current directory!")
            os._exit(1)

        # Load settings
        settings = load_settings()

       # Load proxies if use_proxy is True
        proxies = load_proxies("proxy.txt")
        proxy = random.choice(proxies).strip()

        if(proxy == "DEFAULT_PROXY"):
            print("No proxy found in proxy.txt! Please add a proxy.")
            os._exit(1)

        # Initialize driver
        driver = initialize_driver(proxy)
        wait = WebDriverWait(driver, 10)
        wait_Error = WebDriverWait(driver, 1)

        # Open the website
        driver.get("https://pimeyes.com/en")

        # Click on the first button
        try:
            button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hero-section"]/div/div[1]/div/div/div[1]/button[2]/span')))
            button1.click()
        except TimeoutException:
            print("Button not found!")
            driver.quit()
            os._exit(1)

        # Upload the file
        try:
            upload = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="file-input"]')))
            upload.send_keys(os.path.join(os.path.dirname(__file__), path))
        except TimeoutException:
            print("Upload button not found!")
            driver.quit()
            os._exit(1)

        # Click on the checkboxes
        try:
            checkbox1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/div/div/div[4]/div[1]/label/input')))
            checkbox2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/div/div/div[4]/div[2]/label/input')))
            checkbox3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/div/div/div[4]/div[3]/label/input')))

            checkbox1.click()
            checkbox2.click()
            checkbox3.click()
        except TimeoutException:
            print("Checkbox not found! Please check the file extension.")
            driver.quit()
            os._exit(1)

        # Click on the second button
        try:
            button2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/div/div/button')))
            button2.click()
        except TimeoutException:
            print("Button not found!")
            driver.quit()
            os._exit(1)

        # Check for unwanted elements
        try:
            unwanted_element = wait_Error.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div/div/div/p')))
            print("IP Limit. Stopping program and removing proxy if used.")
            if settings["use_proxy"]:
                remove_proxy(settings["proxy_file"], proxy)
            driver.quit()
            os._exit(1)
        except TimeoutException:
            pass

        # Get the results
        try:
            results = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="results"]/div/div/div[3]/div/div/div[1]/div/div[1]/button/div/span/span')))
            results_text = results.text

            # Use regular expression to extract the number of results
            num_results = re.search(r'\d+', results_text).group()
            print("Proxy: ", proxy)
            print("Results: ", num_results)
            print("Search url: ", driver.current_url)
        except TimeoutException:
            print("Results not found")
            driver.quit()

        # Delete the file
        try:
            os.remove(os.path.join(os.path.dirname(__file__), path))
        except:
            print("Error deleting file!")
            driver.quit()
            os._exit(1)
            
    except Exception as e:
        print(f"An error occurred: {e}!")
    finally:
        # Check if driver is not None before calling quit
        if driver is not None:
            driver.quit()
