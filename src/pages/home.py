from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.basepage import BasePage
from src.utils.waits import Waits


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.search = (By.NAME, "q")
        self.search_button = (
            By.CSS_SELECTOR, "//input[value='Google Search']")

    def keyin_search(self, text):
        webelement = Waits.get_visible_element(self.driver, self.search)
        webelement.send_keys(Keys.CONTROL + "a")
        webelement.send_keys(Keys.DELETE)
        webelement.send_keys(text)
        return self

    def click_search(self):
        webelement = Waits.get_visible_element(self.driver, self.search)
        webelement.click()
        return self
