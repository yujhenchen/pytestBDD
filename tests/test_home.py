from src.pages.home import HomePage
from src.browsers.browserfactory import BrowserFactory

def test_search():
    driver = BrowserFactory.get_chrome()
    driver.get('https://www.google.com/')
    driver.maximize_window()
    home = HomePage(driver)
    home.keyin_search('search')
    driver.close()