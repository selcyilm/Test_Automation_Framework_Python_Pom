from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from pages.base_page import BasePage


class HomePage(BasePage):
    ACCEPT_COOKIES_BUTTON = (By.ID, "sp-cc-accept")
    SEARCH_BOX_AREA = (By.ID, "twotabsearchtextbox")

    def accept_cookies(self):
        self.click_element(*self.ACCEPT_COOKIES_BUTTON)

    def search_product(self, product_to_search):
        search_box_element = self.get(*self.SEARCH_BOX_AREA)
        search_box_element.send_keys(product_to_search, Keys.ENTER)
