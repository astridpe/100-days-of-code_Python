from InternetSpeedTwitterBot import InternetSpeedTwitterBot
from selenium.webdriver.chrome.service import Service

PROMISED_DOWN = 250
PROMISED_UP = 250
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

twitter_bot = InternetSpeedTwitterBot(driver_path=CHROME_DRIVER_PATH)
internet_speed = twitter_bot.get_internet_speed()

if twitter_bot.up < PROMISED_UP or twitter_bot.down < PROMISED_DOWN:
    twitter_bot.tweet_at_provider(PROMISED_UP, PROMISED_DOWN, TWITTER_EMAIL, TWITTER_PASSWORD)


