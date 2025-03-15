from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class HeaderComp(BasePage):
    """
    Component class representing Amazon's header navigation bar.
    Provides methods to interact with common header elements.
    """
    LOGO_ICON = (By.ID, "nav-logo-sprites")
    LOCATION_LINK = (By.ID, "nav-global-location-popover-link")
    SEARCH_DD_CATEGORY = (By.ID, "searchDropdownBox")
    SEARCH_BOX_AREA = (By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON = (By.ID, "nav-search-submit-button")
    ACCOUNT_LIST_LINK = (By.ID, "nav-link-accountList")
    ORDERS_LINK = (By.ID, "nav-orders")
    CART_LINK = (By.ID, "nav-cart")
    CART_COUNT_TEXT = (By.ID, "nav-cart-count")

    def navigate_to_homepage(self):
        """
        Clicks on the Amazon logo to navigate back to homepage.
        """
        self.get(*self.LOGO_ICON).click()

    def click_on_location(self):
        """
        Clicks on the location link to open the delivery location dialog.
        """
        self.click_element(*self.LOCATION_LINK)

    def pick_category(self, category_name):
        """
        Selects a specific category from the search dropdown.

        :arg category_name: The visible text of the category to select
        """
        self.select_by_visible_text(self.SEARCH_DD_CATEGORY, category_name)

    def search_product(self, product_name):
        """
        Searches for a product by entering text and clicking search button.

        :arg product_name: Keywords to search for
        """
        self.get(*self.SEARCH_BOX_AREA).send_keys(product_name)
        self.click_element(*self.SEARCH_SUBMIT_BUTTON)

    def navigate_to_cart_page(self):
        """
        Navigates to the shopping cart page by clicking the cart icon.
        """
        self.click_element(*self.CART_LINK)

    def get_number_of_products_on_cart(self):
        """
        On the card page icon, there is a number representing how many products
        are on the cart page, It basically extracts the numerical value displayed
        on the cart icon
        :return: Number of items on the shopping cart
        """
        return int(self.get_text(self.CART_COUNT_TEXT))