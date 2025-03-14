import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, "span#productTitle")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_COUNT_NUMBER = (By.ID, "nav-cart-count")
    CART_PAGE_ICON = (By.ID, "nav-cart")

    def add_product_to_card(self):
        self.hover_and_click(*self.ADD_TO_CART_BUTTON)

    def get_how_many_product_on_cart(self):
        #time.sleep(2)
        return int(self.get_text(self.CART_COUNT_NUMBER))

    def navigate_to_card_page(self):
        self.hover_and_click(*self.CART_PAGE_ICON)

    def get_product_title(self):
        return self.get(*self.PRODUCT_TITLE)
