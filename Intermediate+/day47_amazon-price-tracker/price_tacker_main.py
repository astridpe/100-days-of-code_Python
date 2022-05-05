import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "astridtesting282@gmail.com"
PASSWORD = "N$&Qm&9nBH%9Xr!"

# 1. Find a product on Amazon that you want to track and get the product URL:
URL = "https://www.amazon.com/HOKA-ONE-Womens-Rincon-Running/dp/B099W3241F/ref=sr_1_1?keywords=hoka%2Bcarbon%2Bx2" \
      "%2Bwomens&qid=1651773006&sprefix=Hoka%2BCarbon%2BX%2B2%2Bw%2Caps%2C140&sr=8-1&th=1&psc=1"

# 2. Use the requests library to request the HTML page of the Amazon product using the URL you got from 1:
ACCEPT_LANGUAGE = "nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5,sv;q=0.4"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)" \
             "Chrome/101.0.4951.54 Safari/537.36"

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
amazon_page = response.text

# 3. Use BeautifulSoup to make soup with the web page HTML you get back:
soup = BeautifulSoup(amazon_page, "lxml")

# 4. Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
price = soup.find("span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# 5. When the price is below 100 then use the smtp module to send an email to yourself.
# In the email, include the title of the product, the current price and a link to buy the product.
if price_as_float < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert\n\n HOKA ONE ONE Womens Rincon 3 Synthetic Textile "
                                f"Trainers is now ${price_as_float} \n {URL} "
                            )



