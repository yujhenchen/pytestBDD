from pytest_bdd import scenario, given, when, then
from src.pages.home import HomePage
from src.browsers.browserfactory import BrowserFactory


@scenario('search_article.feature', 'search keyword selenium')
def test_search_article():
    try:
        targetUrl = "https://blog.testproject.io/"
        queryStr = "selenium"

        driver = BrowserFactory.get_chrome()
        driver.get(targetUrl)
        driver.maximize_window()
        home = HomePage(driver)
        home = home.keyin_search(queryStr)
        home = home.click_search_icon()
        home, searchResultsTitle = home.get_search_results_title(queryStr)
        # verify query string in the search results title
        assert (queryStr in searchResultsTitle)
    except Exception:
        assert False
    finally:
        driver.close()
