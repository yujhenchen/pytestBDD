from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.utils.waits import Waits


class HomePage(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

        # search area
        self.searchFormXpath = "//aside[@id='secondary']//form[@class='search-form']"
        self.searchInput = (
            By.XPATH, self.searchFormXpath + "//input[@class='search-field']")
        # self.searchIcon = (
        #     By.XPATH, self.searchFormXpath + "/child::span")  # fail to locate
        # Search Results for:
        self.searchResultsHeader = (By.CLASS_NAME, "page-title")

        # login and signup area
        # login
        self.emailInput = (By.NAME, "your-email")
        self.createAccountButton = (
            By.CSS_SELECTOR, "input[value='Create an Account']")
        # signup
        self.thirdPartySignUpUrl = "https://auth.testproject.io/auth/realms/TP/protocol/openid-connect/auth?client_id=tp.app&redirect_uri=https://app.testproject.io/callback.html&response_type=code&scope=openid"
        self.signUpWithGoogleLink = (
            By.CSS_SELECTOR, "a[href='" + self.thirdPartySignUpUrl + "&kc_idp_hint=google']")
        self.signUpWithGoogleLink = (
            By.CSS_SELECTOR, "a[href='" + self.thirdPartySignUpUrl + "&kc_idp_hint=microsoft']")
        self.subscribeSubmitButton = (
            By.CLASS_NAME, "yikes-easy-mc-submit-button yikes-easy-mc-submit-button-1 btn btn-primary  popup-link")

        # subscribe
        self.subscribeEmailInput = (By.ID, "yikes-easy-mc-form-1-EMAIL")

    def keyin_search(self, searchText):
        webelement = Waits.get_visible_element(self.driver, self.searchInput)
        webelement.send_keys(Keys.CONTROL + "a")
        webelement.send_keys(Keys.DELETE)
        webelement.send_keys(searchText)
        return self

    def click_search_icon(self):
        # failed to locate search icon
        # webelement = Waits.get_visible_element(self.driver, self.searchInput)
        # webelement.click()

        # use send key enter to perform search
        webelement = Waits.get_visible_element(self.driver, self.searchInput)
        webelement.send_keys(Keys.ENTER)
        return self

    def get_search_results_title(self, searchText):
        webelement = Waits.get_visible_element(
            self.driver, self.searchResultsHeader)
        searchResultsTitle = webelement.text
        return self, searchResultsTitle
