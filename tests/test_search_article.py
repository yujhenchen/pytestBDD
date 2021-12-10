import pytest
from pytest_bdd import scenario, given, when, then, parsers
from src.pages.home import HomePage
from src.browsers.browserfactory import BrowserFactory

# # parameters
# pytest.targetUrl = "https://blog.testproject.io/"
# pytest.queryStr = "selenium"
# # variables
# pytest.home = None


@pytest.fixture(scope="class")
def set_global_variables():
    # parameters
    pytest.targetUrl = "https://blog.testproject.io/"
    # pytest.queryStr = "selenium"
    # variables
    pytest.home = None
    pytest.driver = None
    # print("before")  # debug use
    yield


@pytest.fixture(scope="class")
def close_browsers():
    yield
    # print("after")  # debug use
    if pytest.driver is not None:
        pytest.driver.close()


@pytest.mark.usefixtures("close_browsers", "set_global_variables")
@scenario("search_article.feature", "search keyword of articles")
def test_search_article():
    pass


@given("navigate to the home page of the TestProject Test Automation Blog")
def navigate_to_home():
    pytest.driver = BrowserFactory.get_chrome()
    pytest.driver.get(pytest.targetUrl)
    pytest.driver.maximize_window()
    pytest.home = HomePage(pytest.driver)


@when("I keyin {keyword} in the search field and click Enter in the keyword search field", target_fixture="keyin_keyword")
def keyin_keyword():
    pytest.home = pytest.home.keyin_search(keyword)
    pytest.home = pytest.home.press_keyboard_enter()


@then("search results title contain {keyword}", target_fixture="contain_keyword")
def contain_keyword():
    pytest.home, searchResultsTitle = pytest.home.get_search_results_title(
        keyword)
    # verify query string in the search results title
    assert (keyword in searchResultsTitle)
