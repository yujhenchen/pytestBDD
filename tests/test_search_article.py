import pytest
from pytest_bdd import scenario, given, when, then
from src.pages.home import HomePage
from src.browsers.browserfactory import BrowserFactory

# parameters
pytest.targetUrl = "https://blog.testproject.io/"
pytest.queryStr = "selenium"
# variables
pytest.home = None



@scenario("search_article.feature", "search keyword selenium")
def test_search_article():
    pass


@given("navigate to the home page of the TestProject Test Automation Blog")
def navigate_to_home():
    driver = BrowserFactory.get_chrome()
    driver.get(pytest.targetUrl)
    driver.maximize_window()
    pytest.home = HomePage(driver)


@when("I keyin the keyword in the keyword search field and click Enter on keyboard in the keyword search field")
def keyin_keyword():
    pytest.home = pytest.home.keyin_search(pytest.queryStr)
    pytest.home = pytest.home.press_keyboard_enter()


@then("search results title contain the keyword that I searched for")
def contain_keyword():
    pytest.home, searchResultsTitle = pytest.home.get_search_results_title(pytest.queryStr)
    # verify query string in the search results title
    assert (pytest.queryStr in searchResultsTitle)
