import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import os
script_dir = Path(__file__).parent
ChromeDriver = script_dir /"chromedriver.exe"

print(f"ChromeDriver path: {ChromeDriver}")

service = Service(executable_path=str(ChromeDriver))

driver = webdriver.Chrome(service=service)

driver.get("https://x.com/home")
wait = WebDriverWait(driver, 10)

signup = driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a")
signup.click()

input() 

driver.quit()