from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CardPage(BasePage):
    CART_PRODUCT_FULL_NAME = (By.CSS_SELECTOR, "[class='a-truncate-full a-offscreen']")
    DELETE_PRODUCT_FROM_CARD_BUTTON = (By.CSS_SELECTOR, "[value='Sil']")
    HOME_PAGE_ICON_LINK = (By.ID, "nav-logo-sprites")

    def get_cart_product_full_name(self):
        return self.get(*self.CART_PRODUCT_FULL_NAME).get_attribute("textContent")

    def delete_product_from_cart(self):
        self.hover_and_click(*self.DELETE_PRODUCT_FROM_CARD_BUTTON)

    def return_home_page(self):
        self.hover_and_click(*self.HOME_PAGE_ICON_LINK)