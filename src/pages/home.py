from selenium.webdriver.common.by import By
from src.pages.basepage import BasePage
from src.utils.waits import Waits
from src.utils.actions import Actions


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.search = (By.CLASS_NAME, 'gLFyf gsfi')
        self.search_button = (
            By.CSS_SELECTOR, "//input[value='Google Search']")

    def keyin_search(self, text):
        webelement = Waits.get_visible_element(self.driver,self.search)
        webelement = Actions.clear_input_element(webelement)
        webelement.sendKeys(text)
        return self

    def click_search(self):
        webelement = Waits.get_visible_element(self.driver, self.search)
        webelement.click()
        return self
