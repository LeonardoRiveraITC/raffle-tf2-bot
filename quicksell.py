#!python3
from selenium import webdriver
import bs4,requests,re,time
counter = 0
cell = []
scraptfBeautifulSoup= bs4.BeautifulSoup(requests.get('https://scrap.tf/items').text)
print(scraptfBeautifulSoup.find_all(["tr"], string= re.compile(r'[a-zA-Z0-9]')))
# table = (scraptfBeautifulSoup.find('tbody'))
# for row in table:
#       if type(row)==bs4.element.Tag:
#          cell+=row
# for data in cell:
#     print (data)
#     print('+++++++++++++++++')
