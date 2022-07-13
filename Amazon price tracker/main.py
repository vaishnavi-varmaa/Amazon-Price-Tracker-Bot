import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/dp/B09V48BYGP?th=1'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

def check_phone_price():
    page = requests.get(url, headers=headers)
    bs = BeautifulSoup(page.content,'html.parser')
    product_title=bs.find(id='productTitle').get_text()
    print(product_title.strip())

    price = bs.find(attrs='a-offscreen').get_text()
    price=price[1:-3]
    print(price)
    price_float=float(price.replace(",",""))
    print(price_float)
    return price_float


def send_email():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("gottumukkala.vaishnavi20@gmail.com","flluadhcevliqzju")
    subject = "AMAZON PRICE ALERT"
    body = "Hey the price fell Down.Do you wann buy? .Go order now before the deal gets over\n Link:'https://www.amazon.in/dp/B09V48BYGP?th=1"
    msg = f'Subject:{subject}\n\n\n{body}'

    server.sendmail("gottumukkala.vaishnavi20@gmail.com","gottumukkala.vaishnavi20@gmail.com",msg)
    print("email sent")
    server.quit()
price=check_phone_price()
if price < 12000000:
    send_email()