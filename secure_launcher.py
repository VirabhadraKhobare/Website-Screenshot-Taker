from tkinter import *
import subprocess
import sys

# === Configuration ===
APP_PASSWORD = "virbhadra123"  # Change this to your secure password

# === Login Function ===
def check_password():
    entered = password_entry.get()
    if entered == APP_PASSWORD:
        status_label.config(text="✅ Access granted!", fg="green")
        login_window.after(1000, lambda: [
            login_window.destroy(),
            subprocess.run([sys.executable, "app.py"])
        ])
    else:
        status_label.config(text="❌ Incorrect password", fg="red")

# === Window ===
login_window = Tk()
login_window.title("🔐 Secure Admin Access")
login_window.geometry("400x300")
login_window.configure(bg="#1e1e2f")
login_window.resizable(False, False)

# === Header ===
header = Label(
    login_window, text="🔒 Secure Screenshot App", 
    font=("Segoe UI", 16, "bold"), fg="#ffffff", bg="#1e1e2f"
)
header.pack(pady=(30, 10))

# === Instruction ===
Label(
    login_window, text="Please enter the admin password to continue", 
    font=("Segoe UI", 10), fg="#c0c0c0", bg="#1e1e2f"
).pack(pady=(0, 20))

# === Password Entry ===
password_entry = Entry(
    login_window, show="*", font=("Segoe UI", 12), justify="center", 
    width=25, bg="#2d2d44", fg="#ffffff", bd=0, insertbackground="white"
)
password_entry.pack(pady=10)
password_entry.focus()

# === Submit Button ===
def on_enter(e): submit_btn.config(bg="#03dac6")
def on_leave(e): submit_btn.config(bg="#1f1f33")

submit_btn = Button(
    login_window, text="Login", command=check_password,
    font=("Segoe UI", 11, "bold"), bg="#1f1f33", fg="white", 
    activebackground="#03dac6", activeforeground="black", padx=10, pady=5, bd=0
)
submit_btn.pack(pady=10)
submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

# === Status Message ===
status_label = Label(login_window, text="", fg="red", bg="#1e1e2f", font=("Segoe UI", 10))
status_label.pack(pady=10)

login_window.mainloop()
