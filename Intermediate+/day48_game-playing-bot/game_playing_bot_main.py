from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_driver_path = ""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Create a bot using Selenium and Python to click on the cookie as fast as possible:
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

# loop for 5 seconds:
timeout = time.time() + 5

# 5 min:
five_min = time.time() + 60 * 5

game_playing = True

while game_playing:
    cookie.click()

    # Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive
    # one. You'll need to check how much money (cookies) you have against the price of each upgrade.
    if time.time() > timeout:
        # Check for best item, class '', i.e not 'grayed'
        items_to_buy = driver.find_elements(
            By.CSS_SELECTOR, 'div[class=""] b'
        )
        # Buy last item in list, aka most expensive
        items_to_buy[:][-1].click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". e.g. this is
    # mine:
    if time.time() > five_min:
        game_playing = False

cookies_second = driver.find_element(by=By.ID, value="cps")
print(cookies_second.text)

driver.quit()
