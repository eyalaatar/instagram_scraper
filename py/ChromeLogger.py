from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class ChromeLogger:
    def __init__(self, path, username, password):
        self.path = path
        self.username = username
        self.password = password
        self.driver = None

    def connect(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.get("https://www.instagram.com/")
        time.sleep(10)
        username = self.driver.find_element_by_css_selector("input[name='username']")
        password = self.driver.find_element_by_css_selector("input[name='password']")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(10)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        time.sleep(10)
        searchbox = self.driver.find_element_by_css_selector("input[placeholder='Rechercher']")
        keyword = "#jacqueschiracforever"
        searchbox.send_keys(keyword)
        time.sleep(10)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(10)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(10)
        self.scroll()
        return self.driver

    def scroll(self):
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while match == False:
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True
