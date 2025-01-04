import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
from unidecode import unidecode

# AMAZON_URL = "https://appbrewery.github.io/instant_pot/" (PRACTICE)
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
SET_MIN_PRICE = 100

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

response = requests.get(url=AMAZON_URL, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# price = (int(soup.select_one(selector="span.a-price-whole").getText().split(".")[0]) +
#          (0.01*(int(soup.select_one(selector="span.a-price-fraction").getText()))))
price = float(soup.select_one(selector="span.aok-offscreen").getText().strip()[1:])
print(price)
title = unidecode(soup.select_one(selector="span#productTitle").getText().replace('\n', "").replace('\r', "").replace
                  ("                                        ", " ").strip())
link = AMAZON_URL

# email title, current price, link
load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASSWORD')
to_email = os.getenv('MY_EMAIL')
message = f"{title} is now $ {price}\n{link}".strip()
print(my_email, my_password)
print(message)

if price < SET_MIN_PRICE:
    connection = smtplib.SMTP(os.getenv('SMTP_ADDRESS'), 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Amazon Price Alert!\n\n{message}")
    connection.close()
    print("Email sent!")
