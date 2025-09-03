from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def create_driver(browser_path):
    if "Edge" in browser_path or "msedge" in browser_path.lower():
        from selenium.webdriver.edge.service import Service as EdgeService
        from selenium.webdriver.edge.options import Options as EdgeOptions
        options = EdgeOptions()
        options.binary_location = browser_path
        options.add_argument("--start-maximized")
        service = EdgeService()  # EdgeDriver must be in PATH or specify path here
        return webdriver.Edge(service=service, options=options)
    else:
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        options = ChromeOptions()
        # Wrap path in quotes if it contains spaces or special characters
        if " " in browser_path or "(" in browser_path or ")" in browser_path:
            browser_path = f'"{browser_path}"'
        options.binary_location = browser_path
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        service = ChromeService()
        return webdriver.Chrome(service=service, options=options)

def login_moodle(driver, username, password):
    driver.get("https://bkb-ecampus.de/login/index.php")
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
    time.sleep(1)