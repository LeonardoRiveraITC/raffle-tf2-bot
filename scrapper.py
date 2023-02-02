#! python3
import requests, bs4
backpack = requests.get('https://backpack.tf/stats/Unique/Taunt%3A%20The%20Box%20Trot/Tradable/Craftable')
comparision = bs4.BeautifulSoup(backpack.text,features="lxml")
print(comparision.find(id="listing-440_9090022478"))
