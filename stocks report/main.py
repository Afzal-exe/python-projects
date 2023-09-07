import requests
import datetime
from twilio.rest import Client

# ----------------stocks--------------------

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_KEY = "9NBYH3SDCXUTTGIM"
URL = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": alpha_KEY
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [ value for (key, value) in data.items()]
day_before_yes_close = float(data_list[1]["4. close"])
yes_open = float(data_list[0]["1. open"])

change_perc = (day_before_yes_close - yes_open) / day_before_yes_close * 100


# -------------------NEWs------------------------

if change_perc >= 5:
    if yes_open - day_before_yes_close < 0:
        change_perc *= -1
    news_KEY = "977d57691c7742d397acc5654450c0e0"
    new_URL = "https://newsapi.org/v2/top-headlines"
    parameter = {
        "q": "Tesla",
        "apikey": news_KEY
    }
    new_response = requests.get(new_URL, params=parameter)
    new_response.raise_for_status()
    news = new_response.json()
    article = {
        "Headline": news["articles"][0]["title"],
        "Breif":news["articles"][1]["description"]
    }
    # print(article)

    message = f"{COMPANY_NAME}: {change_perc}\n{article}"
    print(message)

    account_sid = "AC3897f3470f270a0e6dd5b1993491b544"
    auth_token = "9033f5dca0fee7470a472ec1b3d32f85"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_="+12536428755",
        to="+919060791307"
        )


