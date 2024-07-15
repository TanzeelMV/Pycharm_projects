import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alphavantage_api_key = "PWX2GLWIMW398KC1"
alphavantage_params = {
    "apikey": alphavantage_api_key,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact"
}
alph_response = requests.get(url="https://www.alphavantage.co/query", params=alphavantage_params)
alph_data = alph_response.json()

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_price_list = [value for (key, value) in alph_data["Time Series (Daily)"].items()]

today_stock_close = float(stock_price_list[0]["4. close"])
yest_stock_close = float(stock_price_list[1]["4. close"])


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_api_key = "131879695375411f9849939e3f14b821"
news_params = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_data = news_response.json()

# print(news_data["articles"][0]["description"])
# print(news_data["articles"][1]["description"])
# print(news_data["articles"][2]["description"])


def see_news(j: int) -> str:
    news_text = "Headline: " + news_data["articles"][j]["title"] + "\nBrief: " + news_data["articles"][j]["description"]
    return news_text


def percentage_change() -> str:
    percent = ((today_stock_close - yest_stock_close)*100)/today_stock_close
    if percent > 0:
        return f"🔺{round(percent, 3)}%\n"
    else:
        return f"🔻{round(percent, 3)}%\n"

# print(see_news(0))

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


acc_sid = "ACdc196b9763268402b443668fac625439"
auth_token = "87ca68a1effcab8d5c336c510039599c"

client = Client(acc_sid, auth_token)


def send_messages(k):
    message = client.messages.create(
        body=STOCK + ": " + percentage_change() + see_news(k),
        from_="+13613095450",
        to="+919324983039"
    )
    print(message.status)


if yest_stock_close > (today_stock_close*1.05) or yest_stock_close < (today_stock_close*0.95):
    # print("GET NEWS!")
    for i in range(3):
        send_messages(i)

# send_messages(4)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge 
funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st,
near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge 
funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, 
near the height of the coronavirus market crash.
"""
