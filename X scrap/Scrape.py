import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
import os
script_dir = Path(__file__).parent
ChromeDriver = script_dir /"chromedriver.exe"

print(f"ChromeDriver path: {ChromeDriver}")

service = Service(executable_path=str(ChromeDriver))

driver = webdriver.Chrome(service=service)

driver.get("https://x.com/home")

input()