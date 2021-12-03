from selenium import webdriver
from src.browsers.chrome import Chrome
class BrowserFactory(object):
    def __init__(self):
        super().__init__()

    def get_chrome():
        chrome = Chrome()
        return chrome.driver
