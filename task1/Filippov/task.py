from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

s= Service('C:\1\chromedriver.exe')
browser=webdriver.Chrome(service=s)
browser.get('https://www.kinopoisk.ru/lists/movies/top250/')
time.sleep(10)