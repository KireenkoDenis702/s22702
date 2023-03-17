from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

s = Service('F:\Chromedriver\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.kinopoisk.ru/lists/movies/top250/')
time.sleep(10)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
films = soup.find_all("a", class_="base-movie-main-info_link__YwtP1")

print(films[0].text)
