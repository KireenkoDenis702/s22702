from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

s= Service('D:\driverselenium\chromedriver.exe')
browser=webdriver.Chrome(service=s)
browser.get('https://www.kinopoisk.ru/lists/movies/top250/')
time.sleep(9)

html_text=browser.page_source

soup=BeautifulSoup(html_text, 'lxml')
films=soup.find_all('div', class_='base-movie-main-info_mainInfo__ZL_u3')


print(films[0].text)