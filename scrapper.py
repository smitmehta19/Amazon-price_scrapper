import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJXP4'
#URL = 'https://www.amazon.in/Sony-MDR-ZX110A-Stereo-Headphones-without/dp/B00KGZZ824/ref=sr_1_1?pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=2a03e8d4-0550-4cd8-8904-3d786229ed1c&pf_rd_r=TY6SK1MJZ8EW7ZW187ME&pf_rd_s=slot-3&pf_rd_t=701&qid=1562313716&s=gateway&smid=A14CZOWI0VEHLG&sr=8-1'

headers = {"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}


def check():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:9].replace(',', ''))

    if converted_price < 1.000:
        send_mail()

    print(title.strip())
    print(converted_price)

    if converted_price < 1.000:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('smitmehta1496@gmail.com', 'rscjkeogvjbytple')

    subject = "The Price for the Bluetooth earphones is down!"
    body = "Check the link now -----> https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJXP4"
    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'smitmehta1496@gmail.com',
        'smitm515@gmail.com',
        msg
    )

    print("Hey it Worked")
    server.quit()


while(True):
    check()
    time.sleep(60 * 180)
