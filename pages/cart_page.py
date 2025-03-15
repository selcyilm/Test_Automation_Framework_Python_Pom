from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CardPage(BasePage):
    CART_PRODUCT_FULL_NAME = (By.CSS_SELECTOR, "[class='a-truncate-full a-offscreen']")
    DELETE_PRODUCT_FROM_CARD_BUTTON = (By.CSS_SELECTOR, "[value='Sil']")

    def get_cart_product_full_name(self):
        """
        :return: The complete product name of the item in the cart
        """
        return self.get(*self.CART_PRODUCT_FULL_NAME).get_attribute("textContent")

    def delete_product_from_cart(self):
        """
        Removes a product from the shopping cart
        """
        self.hover_and_click(*self.DELETE_PRODUCT_FROM_CARD_BUTTON)
