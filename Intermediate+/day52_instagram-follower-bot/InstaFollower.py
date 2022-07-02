from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class InstaFollower:

    # In the init() method, create the Selenium driver:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Create three methods - login() and find_followers() and follow():
    def login(self, username, password):

        # Use Selenium and Python to login to Instagram automatically using your email and password. Write your code in
        # the login() method:
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(1)
        cookies_btn = self.driver.find_element(by=By.CLASS_NAME, value="aOOlW")
        cookies_btn.click()

        time.sleep(2)
        login_username = self.driver.find_element(by=By.CLASS_NAME, value="f0n8F ")
        login_username.send_keys(username)

        login_password = self.driver.find_element(by=By.XPATH,
                                                  value="/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
        login_password.send_keys(password)

        login_btn = self.driver.find_element(by=By.XPATH,
                                             value="/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]")
        login_btn.click()

        time.sleep(2)
        not_saving_info = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div[1]/section/main/div/div/div/div/button")
        not_saving_info.click()

        time.sleep(2)
        no_notification = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
        no_notification.click()

    def find_followers(self, similar_account):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}/")

        time.sleep(2)
        followers = self.driver.find_element(by=By.XPATH,
                                             value="/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div")
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(by=By.XPATH,
                                         value="/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div")

        # scroll 10 times:
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH,
                                                         value="/html/body/div[5]/div/div/div/div[3]/button[2]")
                cancel_button.click()
