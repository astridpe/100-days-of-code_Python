import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_STOCK_API_KEY = ""
MY_NEWS_API_KEY = ""

ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
MY_PHONE_NUMBER = ""

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price:
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": MY_STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
date_list = [date_data for (date, date_data) in stock_data.items()]
yesterday_closing_price = date_list[0]["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price:
day_before_yesterday_closing_price = date_list[1]["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20:
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day
# before yesterday.
percentage_difference = round((difference / float(yesterday_closing_price)) * 100)

# If the percentage is greater than 5 then print("Get News").
if abs(percentage_difference) > 5:
    # print("Get News")

    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), use the News API to get the first 3 articles related to the COMPANY_NAME:
    news_parameters = {
        "apiKey": MY_NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    # Use Python slice operator to create a list that contains the first 3 articles:
    articles = news_response.json()["articles"][:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 article's headline and description using list comprehension.
    # for article in articles:
    #     title = article["title"]
    #     print(title)
    #     description = article["description"]
    #     print(f"{description}")
    #     url = article["url"]
    #     print(f"{url} \n")

    # you can use solution above, but list comprehension makes it easier to read.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\n"
                          f"Headline: {article['title']}. \n"
                          f"Brief: {article['description']}" for article in articles]

    # Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER,
        )
        print(message.status)

# Optional - Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
