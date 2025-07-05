from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")
service = Service(executable_path=chromedriver_path)

options = Options()
# 👇 REMOVE headless to behave like a normal user
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://leetcode.com")
input("👁️ Check page manually, then press ENTER to screenshot...")

# Wait for user to complete verification manually
driver.set_window_size(1920, driver.execute_script("return document.body.scrollHeight"))
time.sleep(2)

driver.save_screenshot("leetcode_fullpage.png")
print("✅ Screenshot saved!")

driver.quit()
