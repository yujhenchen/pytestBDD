from src.pages.home import HomePage
from src.browsers.browserfactory import BrowserFactory


def test_search():
    try:
        driver = BrowserFactory.get_chrome()
        driver.get("https://blog.testproject.io/")
        driver.maximize_window()
        home = HomePage(driver)
        home.keyin_search("selenium")
    except Exception:
        assert False
    finally:
        driver.close()
