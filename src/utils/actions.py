from selenium.webdriver.common.keys import Keys


class Actions(object):
    def __init__(self):
        super().__init__()

    def clear_input_element(webelement):
        webelement.clear()
        return webelement

    def clear_input_element_by_key(webelement):
        webelement.sendKeys(Keys.CONTROL + "a")
        webelement.sendKeys(Keys.DELETE)
        return webelement
