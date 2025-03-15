from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def get(self, *locator):
        """
        Find the web element with using specific locator
        :param locator: tuple containing locator type and value
        :return: WebElement, first element its find
        """
        return self.driver.find_element(*locator)

    def get_multiple(self, *locator):
        """
        Finds multiple web elements using locator
        :param locator: tuple containing locator type and value
        :return: list of WebElements its find
        """
        return self.driver.find_elements(*locator)

    def click_element(self, *by_locator):
        """
        Clicks on the element identified by locator
        :param by_locator: tuple containing locator type and value
        """
        self.get(*by_locator).click()

    def hover(self, *by_locator):
        """
        Hovers to specific element identified by locator
        :param by_locator: tuple containing locator type and value
        """
        action = ActionChains(self.driver)
        action.move_to_element(self.get(*by_locator)).perform()

    def hover_and_click(self, *by_locator):
        """
        Hovers and clicks to specific element identified by locator
        :param by_locator: tuple containing locator type and value
        """
        element = self.get(*by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        element.click()

    def get_current_url(self):
        """
        :return: current url of the page
        """
        return self.driver.current_url

    def get_page_title(self):
        """
        :return: title of the page
        """
        return self.driver.title

    def wait_element(self, method, message=''):
        """
        Waits to element until it is clickable
        :param method: Locator tuple for element
        :param message: Optional message for timeout exception
        :return: clickable WebElement
        """
        return self.wait.until(EC.element_to_be_clickable(method), message)

    def get_text(self, locator):
        """
        Waits and get the text of an element
        :param locator: Locator tuple for element
        :return: WebElement's text value
        """
        return self.wait_element(locator).text

    def select_by_visible_text(self, locator, visible_text):
        """
        Select option from drop down with visible text
        :param locator: Locator tuple for element
        :param visible_text: Option to select
        """
        select = Select(self.get(*locator))
        select.select_by_visible_text(visible_text)
