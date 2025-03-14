from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from pages.base_page import BasePage


class HomePage(BasePage):
    ACCEPT_COOKIES_BUTTON = (By.ID, "sp-cc-accept")

    def accept_cookies(self):
        self.click_element(*self.ACCEPT_COOKIES_BUTTON)
