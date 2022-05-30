import os.path
import time
import sqlite3
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

DRIVER_PATH = os.path.abspath("driver-chrome/chromedriver")
URL = "https://www.wildberries.ru/"


class Parser:

    def __init__(self, driver):
        self.__driver = driver

    def parse(self, url, category: list):
        for cat in category:
            url = self.__get_category(url, cat.capitalize())

    def __get_category(self, url, category) -> str:
        """
        получаем ссылку на категорию товаров
        """
        self.__driver.get(url)
        time.sleep(100)
        category_link = self.__driver.find_element(By.XPATH, f"//a[contains(text(),'{category}')]")
        return category_link.get_attribute("href")


def run():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
    wld = Parser(driver)
    wld.parse(URL, ['обувь', 'детская', 'для мальчиков'])


def cok():
    db = sqlite3.connect('chrome-data/Default/Cookies')
    cur = db.cursor()
    cur.execute("select * from cookies where name = 'WILDAUTHNEW_V3' ")



if __name__ == '__main__':
      # run()
     cok()
