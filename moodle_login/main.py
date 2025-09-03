import os
from moodle_login.config import load_config, is_config_valid, ENV_FILE
from moodle_login.env_editor import edit_env
from moodle_login.browser import create_driver, login_moodle

def ensure_dependencies():
    import subprocess
    import sys
    required = ["selenium", "python-dotenv"]
    for package in required:
        try:
            __import__(package if package != "python-dotenv" else "dotenv")
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    ensure_dependencies()
    username, password, browser_path = load_config()
    if not is_config_valid(username, password, browser_path):
        username, password, browser_path = edit_env(ENV_FILE)
        if not is_config_valid(username, password, browser_path):
            print("❌ Error: Environment variables MOODLE_USERNAME, MOODLE_PASSWORD and/or BROWSER_PATH are not set!")
            return

    driver = create_driver(browser_path)
    try:
        login_moodle(driver, username, password)
        input("Press Enter to exit and close the browser...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()