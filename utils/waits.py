from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits(object):

    wait_time = 5

    def __init__(self):
        super().__init__()

    def get_visible_element(driver, locator):
        webelement = WebDriverWait(driver, Waits.wait_time).until(
            EC.visibility_of_element_located(locator))
        return webelement
