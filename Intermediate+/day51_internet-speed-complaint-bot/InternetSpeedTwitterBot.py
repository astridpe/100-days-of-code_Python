from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_USERNAME = ""
INTERNET_PROVIDER = ""
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self, website_link):
        self.driver.get(website_link)
        go_button = self.driver.find_element(by=By.CLASS_NAME, value="js-start-test")
        go_button.click()

        time.sleep(45)
        self.up = float(self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text)
        self.down = float(self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text)
        self.driver.close()

    def complain(self, promised_up, promised_down, driver_path):
        text = f"Hey, {INTERNET_PROVIDER}, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up"

