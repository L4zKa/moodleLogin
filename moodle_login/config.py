import os
from dotenv import load_dotenv

ENV_FILE = ".env"

def load_config():
    load_dotenv(ENV_FILE)
    username = os.getenv("MOODLE_USERNAME")
    password = os.getenv("MOODLE_PASSWORD")
    browser_path = os.getenv("BROWSER_PATH")
    return username, password, browser_path

def is_config_valid(username, password, browser_path):
    return all([username, password, browser_path])