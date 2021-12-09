from pytest_bdd import scenario, given, when, then
from src.pages.home import HomePage
from src.browsers.browserfactory import BrowserFactory

# parameters
targetUrl = "https://blog.testproject.io/"
queryStr = "selenium"
# variables
home = None


@scenario("search_article.feature", "search keyword selenium")
def test_search_article():
    # try:
    #     targetUrl = "https://blog.testproject.io/"
    #     queryStr = "selenium"

    #     driver = BrowserFactory.get_chrome()
    #     driver.get(targetUrl)
    #     driver.maximize_window()
    #     home = HomePage(driver)
    #     home = home.keyin_search(queryStr)
    #     home = home.press_keyboard_enter()
    #     home, searchResultsTitle = home.get_search_results_title(queryStr)
    #     # verify query string in the search results title
    #     assert (queryStr in searchResultsTitle)
    # except Exception:
    #     assert False
    # finally:
    #     driver.close()
    pass


@given("navigate to the home page of the TestProject Test Automation Blog")
def navigate_to_home():
    driver = BrowserFactory.get_chrome()
    driver.get(targetUrl)
    driver.maximize_window()
    home = HomePage(driver)


@when("I keyin the keyword in the keyword search field and click Enter on keyboard in the keyword search field")
def keyin_keyword():
    home = home.keyin_search(queryStr)
    home = home.press_keyboard_enter()


@then("search results title contain the keyword that I searched for")
def contain_keyword():
    home, searchResultsTitle = home.get_search_results_title(queryStr)
    # verify query string in the search results title
    assert (queryStr in searchResultsTitle)
