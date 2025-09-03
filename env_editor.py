import tkinter as tk

def edit_env(env_file):
    result = {}

    def save_env():
        with open(env_file, "w") as f:
            f.write(f"MOODLE_USERNAME={entry_username.get()}\n")
            f.write(f"MOODLE_PASSWORD={entry_password.get()}\n")
        result['username'] = entry_username.get()
        result['password'] = entry_password.get()
        root.destroy()

    root = tk.Tk()
    window_width = 350
    window_height = 150
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

    tk.Button(root, text="Speichern", command=save_env).grid(row=2, column=0, columnspan=2, pady=10)
    root.mainloop()

    return result.get('username'), result.get('password')