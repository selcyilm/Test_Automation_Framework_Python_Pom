from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def get(self, *locator):
        return self.driver.find_element(*locator)

    def get_multiple(self, *locator):
        return self.driver.find_elements(*locator)

    def click_element(self, *by_locator):
        self.get(*by_locator).click()

    def hover(self, *by_locator):
        action = ActionChains(self.driver)
        action.move_to_element(self.get(*by_locator)).perform()

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, method, message=''):
        return self.wait.until(EC.element_to_be_clickable(method), message)

    def get_text(self, locator):
        return self.wait_element(locator).text
