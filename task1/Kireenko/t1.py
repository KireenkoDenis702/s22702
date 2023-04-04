from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import wget

place = 0
s = Service('C:/1/chromedriver')
browser = webdriver.Chrome(service=s)
browser.get(f'https://eksmo.ru/ratings/RaitingYear/')
time.sleep(3)

for page in range(1):
    count = 0
    k = 0
    browser.get(f'https://eksmo.ru/ratings/RaitingYear/page{page}/')
    html_text = browser.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    books = soup.find_all("a", class_="book__link")
    photos = soup.find_all("img", class_="book__img book__img_shadow")
    for k in photos:
            photos = 20
            count += 1
            url = k.find('img', class_="book__img book__img_shadow")
            l = url.get('src')
            wget.download(l, f'C:/Users/kiree/PycharmProjects/s22702/task1/Kireenko/photo{count}.jpg')



    def main():
        place = 0
        data = []



        for book in books:
            place += 1
            name = book.find("div", class_="book__name")
            author = book.find("div", class_="book__author")
            format = book.find("div", class_="book__format")

            data.append(f" {place} | {name.get_text()} | {author.get_text()} | {format.get_text()}")

        return data


    if __name__ == "__main__":
        main()