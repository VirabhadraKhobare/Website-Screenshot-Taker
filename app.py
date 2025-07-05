import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os

class WebsiteScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌐 Full Website Screenshot Taker")
        self.root.geometry("600x300")
        self.root.config(bg="#f0f0f0")

        tk.Label(root, text="Enter Website URL:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        self.url_entry = tk.Entry(root, font=("Arial", 12), width=50)
        self.url_entry.pack(pady=5)

        self.capture_btn = tk.Button(root, text="📸 Capture Full Page", font=("Arial", 12), command=self.capture_website)
        self.capture_btn.pack(pady=20)

    def capture_website(self):
        url = self.url_entry.get().strip()
        if not url.startswith("http"):
            url = "https://" + url

        # Ask for save location
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Files", "*.png")],
                                                 title="Save Full Webpage Screenshot")
        if not save_path:
            return

        # Set Chrome Options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--hide-scrollbars")
        options.add_argument("--start-maximized")

        # Start Chrome
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # Set window size to full height of page
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, total_height)
        time.sleep(2)

        # Take screenshot
        driver.save_screenshot(save_path)
        driver.quit()

        messagebox.showinfo("Success", f"Screenshot saved at:\n{save_path}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteScreenshotApp(root)
    root.mainloop()
