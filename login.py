import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
load_dotenv("loginData.env")  # <--- Dateiname angeben!

# Pfad zu Brave-Exe (nicht Startmenü!)
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

options = Options()
options.binary_location = brave_path   # Brave statt Chrome benutzen

# ChromeDriver starten (Selenium benutzt den für Brave auch)
service = Service()  # wenn chromedriver im PATH ist
driver = webdriver.Chrome(service=service, options=options)

# Moodle Login-Seite
driver.get("https://bkb-ecampus.de/login/index.php")

# Benutzername und Passwort aus .env Datei laden
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

if not username or not password:
    print("❌ Fehler: Umgebungsvariablen USERNAME und/oder PASSWORD sind nicht gesetzt!")
    driver.quit()
    exit(1)
else:
    # Login ausfüllen
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
    # warten bis Dashboard lädt
    time.sleep(3)
    print("✅ Eingeloggt, aktuelle Seite:", driver.current_url)
    input("Drücke Enter zum Beenden und Schließen des Browsers...")  # Fenster bleibt offen

driver.quit()  # Schließt das Fenster erst nach Enter