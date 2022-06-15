from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

EMAIL = ""
PASSWORD = ""

chrome_driver_path = "/Users/astridpettersen/Documents/Python/chromedriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103819153&keywords=full%20stack%20developer"
           "&location=Norge")

time.sleep(1)

# 1. Figure out how to automatically log in to LinkedIn using Selenium
login_button = driver.find_element(by=By.CLASS_NAME, value="btn-secondary-emphasis")
login_button.click()
time.sleep(1)

email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(EMAIL)

password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)

submit_button = driver.find_element(by=By.CLASS_NAME, value="from__button--floating")
submit_button.click()
time.sleep(2)

# Save the first job application on the search-page
save_button = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
save_button.click()
time.sleep(3)




