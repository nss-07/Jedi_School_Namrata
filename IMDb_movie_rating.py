import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_rating(movie_name):
    driver = webdriver.Chrome(executable_path=r"filepath-to-chromedriver")  # edit in chromedriver path
    driver.get("https://www.google.com/")
    print("Let's google stuff")
    driver.find_element_by_name("q").send_keys(movie_name + " imdb")
    time.sleep(1)
    print("Search is on!")
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_class_name('LC20lb.DKV0Md').click()
    print("Page opened... fetching rating")

    link = driver.current_url
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    rating = soup.find('div', class_='ratingValue').text.strip()

    print("Rating of", movie_name, "on IBDb is", rating)


if __name__ == '__main__':
    movie_name = input("Enter movie name: ")
    get_rating(movie_name)