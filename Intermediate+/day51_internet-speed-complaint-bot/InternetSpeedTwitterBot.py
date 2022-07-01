from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        time.sleep(3)
        go_button = self.driver.find_element(by=By.CLASS_NAME, value="js-start-test")
        go_button.click()

        time.sleep(45)
        self.up = float(self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text)
        self.down = float(self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text)
        self.driver.close()

    def tweet_at_provider(self, promised_up, promised_down, twitter_email, twitter_password):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div["
                                                            "1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                                            "2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email.send_keys(twitter_email)

        next_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div["
                                                                  "1]/div/div/div/div/div/div/div[2]/div["
                                                                  "2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_button.click()
        time.sleep(3)

        password = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div["
                                                               "1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                                               "2]/div[2]/div[1]/div/div/div[2]/div/label/div/div["
                                                               "2]/div[1]/input")
        password.send_keys(twitter_password)

        login_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div["
                                                                   "1]/div/div/div/div/div/div/div[2]/div["
                                                                   "2]/div/div/div[2]/div[2]/div[2]/div/div["
                                                                   "1]/div/div/div/div")
        login_button.click()

        time.sleep(5)
        tweet_compose = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div[1]/div/div/div[2]/header/div/div/div/div["
                                                       "1]/div[3]/a/div/span/div/div/span/span")

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up " \
                f"when I pay for {promised_down}down/{promised_up}up? "

        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div["
                                                                   "2]/div/div/div/div/div/div[2]/div["
                                                                   "2]/div/div/div/div[3]/div/div["
                                                                   "1]/div/div/div/div/div[2]/div[3]/div/div/div["
                                                                   "2]/div/div/span/span")
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()

