from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = ""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.amazon.com/HOKA-ONE-Womens-Rincon-Running/dp/B099W3241F/ref=sr_1_1?keywords=hoka%2Bcarbon"
#            "%2Bx2%2Bwomens&qid=1651773006&sprefix=Hoka%2BCarbon%2BX%2B2%2Bw%2Caps%2C140&sr=8-1&th=1&psc=1")

# Classname:
# price = driver. find_element(by=By.CLASS_NAME, value="apexPriceToPay")
# print(price.text)

# Id:
# price = driver.find_element(by=By.ID, value="apexPriceToPay")

# Name:
# price = driver.find_element(by=By.NAME, value="q")

# CSS-selector:
# price = driver.find_element(by=By.CSS_SELECTOR, value=".apexPriceToPay span")

# xpath: price = driver.find_element(by=By.XPATH, value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[
# 1]/span[2]')


# driver.close() <--- Closes a tab in the browser

# PYTHON-EVENT CHALLENGE:
# -Get the upcoming event list from the Python webpage and print it as a dictionary in the format: {0: {time: event:}}

# driver.get("https://www.python.org/")
#
# events = {}
# event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
# event_name = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget  li a")
#
# for n in range(len(event_time)):
#     events[n] = {"time": event_time[n].text,
#                  "event": event_name[n].text,
#                  }
#
# print(events)

# WIKIPEDIA CHALLENGE:
# - 1. Get the article number from the Wikipedia main page and print it out:

driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
print(total_articles.text)

driver.quit()
