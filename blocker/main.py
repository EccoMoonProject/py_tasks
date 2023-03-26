import tkinter as tk
from tkinter import messagebox
import time
import os

# Ścieżka do pliku hosts w systemie
hosts_path = "/etc/hosts" if os.name == 'posix' else r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


def block_website():
    website = website_entry.get()
    duration = int(duration_entry.get()) * 60

    if website:
        with open(hosts_path, "a") as file:
            file.write(f"{redirect} {website}\n")

        messagebox.showinfo("Blokowanie strony",
                            f"Strona {website} została zablokowana.")

        root.after(duration * 1000, unblock_website, website)
        root.after((duration - 600) * 1000, warn_unblock_website, website)
    else:
        messagebox.showerror("Błąd", "Podaj prawidłowy adres strony.")


def unblock_website(website):
    with open(hosts_path, "r") as file:
        lines = file.readlines()

    with open(hosts_path, "w") as file:
        for line in lines:
            if website not in line:
                file.write(line)

    messagebox.showinfo("Odblokowanie strony",
                        f"Strona {website} została odblokowana.")


def warn_unblock_website(website):
    messagebox.showwarning(
        "Uwaga", f"Strona {website} zostanie odblokowana za 10 minut.")


def block_site():
    website = website_entry.get()
    duration = int(duration_entry.get()) * 60

    if website:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            file.write(redirect + ' ' + website + '\n')
            messagebox.showinfo(
                "Blokowanie strony", f'Strona {website} zostala zablokowana na {duration // 60} minut')
        time.sleep(duration - 600)
        messagebox.showwarning(
            "Uwaga", f"Strona {website} zostanie odblokowana za 10 minut.")
        time.sleep(600)
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in word for word in line):
                    file.write(line)
            file.truncate()
            messagebox.showinfo("Odblokowanie strony",
                                f'Strona {website} zostala odblokowana')


root = tk.Tk()
root.title("Bloker stron")
root.geometry("400x250")

label1 = tk.Label(root, text="Adres strony do zablokowania:")
label1.pack(pady=5)

website_entry = tk.Entry(root)
website_entry.pack(pady=5)

label2 = tk.Label(root, text="Czas blokowania w minutach:")
label2.pack(pady=5)

duration_entry = tk.Entry(root)
duration_entry.pack(pady=5)

block_button = tk.Button(root, text="Zablokuj stronę", command=block_site)
block_button.pack(pady=10)

root.mainloop()
