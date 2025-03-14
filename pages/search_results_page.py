from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    PRODUCTS_LIST = (By.CSS_SELECTOR, "[data-cy='title-recipe']")
    SECOND_PAGE_BUTTON = (By.CSS_SELECTOR, "[aria-label='2 sayfasına git']")

    def get_products_list(self):
        return self.get_multiple(*self.PRODUCTS_LIST)

    def click_on_second_page(self):
        self.hover_and_click(*self.SECOND_PAGE_BUTTON)

    def click_on_specific_product(self, index):
        element = self.get_products_list()[index - 1]
        hover = ActionChains(self.driver)
        hover.move_to_element(element).perform()
        element.click()
