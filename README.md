# Moodle Login Automation

Automate login to your Moodle instance using Selenium and Python.

## Features

- GUI for entering credentials and selecting your browser executable
- Stores credentials and browser path in a `.env` file
- Automatically installs required Python packages
- Uses Selenium to automate browser login

## Setup

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd moodleLogin
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the program:**

   ```sh
   python -m moodle_login.main
   ```

   The first run will prompt you for your Moodle username, password, and browser executable (e.g., Brave, Chrome, etc.).

## Usage

- The script will open your selected browser and log in to Moodle automatically.
- Credentials and browser path are stored in `.env` for future runs.
- To change credentials or browser, delete `.env` and rerun the script.

## Requirements

- Python 3.8+
- ChromeDriver (must be in your PATH)
- Supported browsers: Brave, Chrome, Chromium (provide the path to the executable)

## File Structure

```
moodleLogin/
│
├── moodle_login/
│   ├── __init__.py
│   ├── config.py
│   ├── env_editor.py
│   ├── browser.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

## License

MIT License
