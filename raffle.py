#!python3
from selenium import webdriver
import bs4,requests,re,time
#importar los modulos a usar
browser = webdriver.Firefox()
def login():
    browser.get('https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=https%3A%2F%2Fscrap.tf%2Flogin&openid.realm=https%3A%2F%2Fscrap.tf&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select')
    username = browser.find_element_by_id("steamAccountName")
    password = browser.find_element_by_id("steamPassword")
    username.send_keys("user")
    password.send_keys("pass")
    browser.find_element_by_id("imageLogin").click()
    time.sleep(12)
"""insecure plaintext """
def getRaffleList():
   scraptfBeautifulSoup= bs4.BeautifulSoup(requests.get('https://scrap.tf/raffles').text)
   for link in scraptfBeautifulSoup.findAll('a', attrs={'href': re.compile("/raffles/")}):
      try:
         browser.get('https://scrap.tf'+link.get('href'))
         browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[5]/div[2]/button[2]').click()
         time.sleep(3)
      except:
          print('already in') #Si no se encuentra el botòn en el xpath se retorna un error, para evitar
          #afectara la ejecuciòn un except pero esto puede ser retardante en algunos aspectos
          #ej. en /puzzle y /create no existe el botòn por lo que se retorna el error
          #ej.2
"""Obtiene una lista de links de scrap.tf/raffles, corregir problema en el que incluye navegar en
/puzzles y /create """
login()

getRaffleList()
