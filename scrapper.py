from bs4 import BeautifulSoup
import requests
import smtplib

url="https://www.flipkart.com/asus-zenfone-3-laser-silver-32-gb/p/itmehctfzhfjwc6v?pid=MOBEHCTFPH8UTTGH&lid=LSTMOBEHCTFPH8UTTGHBCJLZQ&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Asus&fm=neo%2Fmerchandising&iid=d7ef05fb-f739-4a76-87e6-59be827e8bf6.MOBEHCTFPH8UTTGH.SEARCH&ppt=browse&ppn=browse&ssid=d2hw0itygg0000001598101488089"

r=requests.get(url)

soup=BeautifulSoup(r.content, "html.parser")
#print(soup.prettify())
title=soup.find("span",{"class":"_35KyD6"}).get_text()
#print(title)

title_price=soup.find("div", {"class":"_1vC4OE _3qQ9m1"}).text
title_price= (title_price[1:]).replace(",", "")
print(float(title_price))

your_price=int(input("price:"))
if float(title_price) < your_price:
    
    From=input("Email:")
    psw=input("Password:")
    to_send=input("Email whr u want to send:")
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(From,psw)

    sub = "Price got lower check out"
    body = f"PRODUCT:{title}\n{url}"
    msg = f"Subject: {sub}\n{body}"
    server.sendmail(From, to_send, msg)
    print("Email sent!!")
    server.quit()

else:
    print("Price is still high!!")
   
