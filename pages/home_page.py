from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from pages.base_page import BasePage


class HomePage(BasePage):
    ACCEPT_COOKIES_BUTTON = (By.ID, "sp-cc-accept")

    def accept_cookies(self):
        """
        Accept cookies by clicking accept button
        This method should be called when you access the website first time
        to handle the cookie consent
        """
        self.click_element(*self.ACCEPT_COOKIES_BUTTON)
