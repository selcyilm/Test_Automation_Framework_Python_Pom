import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, "span#productTitle")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    def add_product_to_card(self):
        self.hover_and_click(*self.ADD_TO_CART_BUTTON)

    def get_product_title(self):
        return self.get(*self.PRODUCT_TITLE)
