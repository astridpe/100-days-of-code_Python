import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfR4U3FmI2qbO-vtP7q76UmdG2iUuzX85ogJclMM_IhzSbzbA/viewform?usp" \
            "=sf_link "

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.5929740805664%2C%22east%22%3A-122.2736839194336%2C%22south%22%3A37.72154088653369%2C%22north%22%3A37.829002970360605%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

ACCEPT_LANGUAGE = ""
USER_AGENT = ""

# Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}
response = requests.get(url=ZILLOW_URL, headers=headers)
response.raise_for_status()
zillow_page = response.text
soup = BeautifulSoup(zillow_page, "html.parser")

# Create a list of links for all the listings you scraped:
all_links = soup.find_all(name="a", class_="list-card-link")
property_links = []
for i in all_links:
    link = f"https://www.zillow.com/b/argenta-san-francisco-ca-5Xj7m7/{i.get('href')}"
    property_links.append(link)

# Create a list of prices for all the listings you scraped:
all_prices = soup.find_all(name="div", class_="list-card-price")
property_prices = []
for i in all_prices:
    price_original = i.getText()
    price_without_plus = price_original.split("+")[0]
    price_without_slash = price_without_plus.split("/")[0]
    property_prices.append(price_without_slash)

# Create a list of addresses for all the listings you scraped:
all_addresses = soup.find_all(name="address", class_="list-card-addr")
property_addresses = []
for i in all_addresses:
    address_original = i.getText()
    address_without_area = address_original.split("| ")[-1]
    property_addresses.append(address_without_area)

# Use Selenium to fill in the google-form you created. Each listing should have its price/address/link
# added to the form. You will need to fill in a new form for each new listing.

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
index = len(property_addresses) - 1

while index > 0:
    driver.get(FORM_LINK)
    time.sleep(2)
    question_1 = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    question_2 = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    question_3 = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    send_button = driver.find_element(by=By.CLASS_NAME, value="NPEfkd")

    question_1.send_keys(property_addresses[index])
    question_2.send_keys(property_prices[index])
    question_3.send_keys(property_links[index])
    time.sleep(1)
    send_button.click()
    index -= 1

