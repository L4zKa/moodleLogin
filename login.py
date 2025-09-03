import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import tkinter as tk # Für die GUI
from env_editor import edit_env

# Pfad zu Brave-Exe
brave_path = r"C:\Users\Ich\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"

options = Options()
options.binary_location = brave_path
options.add_argument("--start-maximized")  # Startet im Vollbild
options.add_argument("--disable-infobars") # Entfernt Info-Leiste
options.add_argument("--disable-extensions")
options.add_argument("--profile-directory=Default")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# ChromeDriver starten (Selenium benutzt den für Brave auch)
service = Service()  # wenn chromedriver im PATH ist
driver = webdriver.Chrome(service=service, options=options)

# Moodle Login-Seite
driver.get("https://bkb-ecampus.de/login/index.php")
driver.maximize_window()  # Fenster maximieren

# Pfad zur .env-Datei
env_file = ".env"

if os.path.exists(env_file):
    load_dotenv(env_file)
    username = os.getenv("MOODLE_USERNAME")
    password = os.getenv("MOODLE_PASSWORD")
    print("✅ .env Datei gefunden und geladen.")
else:
    username, password = edit_env(env_file)
    load_dotenv(env_file)

if not username or not password:
    print("❌ Fehler: Umgebungsvariablen MOODLE_USERNAME und/oder MOODLE_PASSWORD sind nicht gesetzt!")
    driver.quit()
    exit(1)
else:
    # Login ausfüllen
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
    # warten bis Dashboard lädt
    time.sleep(1)
    input("Drücke Enter zum Beenden und Schließen des Browsers...")  # Fenster bleibt offen

driver.quit()  # Schließt das Fenster erst nach Enter