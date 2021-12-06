from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.utils.waits import Waits


class HomePage(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

        # search area
        self.searchForm = (By.CSS_SELECTOR, "form[class='search-form']")
        self.searchInput = (By.XPATH, "/form/label/input[@class='search-field']")  # inside a form
        self.searchIcon = (By.CLASS_NAME, "glass")

        # login and signup area
        # login
        self.emailInput = (By.NAME, "your-email")
        self.createAccountButton = (
            By.CSS_SELECTOR, "input[value='Create an Account']")
        # signup
        self.signUpWithGoogleLink = (
            By.CSS_SELECTOR, "a[href='https://auth.testproject.io/auth/realms/TP/protocol/openid-connect/auth?client_id=tp.app&redirect_uri=https://app.testproject.io/callback.html&response_type=code&scope=openid&kc_idp_hint=google']")
        self.signUpWithGoogleLink = (
            By.CSS_SELECTOR, "a[href='https://auth.testproject.io/auth/realms/TP/protocol/openid-connect/auth?client_id=tp.app&redirect_uri=https://app.testproject.io/callback.html&response_type=code&scope=openid&kc_idp_hint=microsoft']")
        self.subscribeSubmitButton = (
            By.CLASS_NAME, "yikes-easy-mc-submit-button yikes-easy-mc-submit-button-1 btn btn-primary  popup-link")

        # subscribe
        self.subscribeEmailInput = (By.ID, "yikes-easy-mc-form-1-EMAIL")

    def keyin_search(self, text):
        # webelement = Waits.get_visible_element(self.driver, self.searchInput)
        # webelement.send_keys(Keys.CONTROL + "a")
        # webelement.send_keys(Keys.DELETE)
        # webelement.send_keys(text)
        webelement = Waits.get_visible_element(self.driver, self.searchForm)
        webelement.click()
        return self

    def click_search_icon(self):
        webelement = Waits.get_visible_element(self.driver, self.searchInput)
        webelement.click()
        return self
