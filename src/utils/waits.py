from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Waits(object):

    wait_time = 5

    def __init__(self):
        super().__init__()

    def get_visible_element(driver, locator):
        webelement = None
        try:
            webelement = WebDriverWait(driver, Waits.wait_time).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException as ex:
            print("get_visible_element: TimeoutException: " +
                  str(ex.__class__.__name__))
        return webelement
