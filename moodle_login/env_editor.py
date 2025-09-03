import tkinter as tk
from tkinter import filedialog

def edit_env(env_file):
    result = {}

    def browse_browser():
        path = filedialog.askopenfilename(title="Select browser executable")
        entry_browser.delete(0, tk.END)
        entry_browser.insert(0, path)

    def save_env():
        with open(env_file, "w") as f:
            f.write(f"MOODLE_USERNAME={entry_username.get()}\n")
            f.write(f"MOODLE_PASSWORD={entry_password.get()}\n")
            f.write(f"BROWSER_PATH={entry_browser.get()}\n")
        result['username'] = entry_username.get()
        result['password'] = entry_password.get()
        result['browser_path'] = entry_browser.get()
        root.destroy()

    root = tk.Tk()
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title(".env Editor")

    tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_username = tk.Entry(root, width=30)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_password = tk.Entry(root, width=30, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Browser exe:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_browser = tk.Entry(root, width=30)
    entry_browser.grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse...", command=browse_browser).grid(row=2, column=2, padx=5, pady=5)

    tk.Button(root, text="Save", command=save_env).grid(row=3, column=0, columnspan=3, pady=10)
    root.mainloop()

    return result.get('username'), result.get('password'), result.get('browser_path')