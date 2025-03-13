import time

from selenium.common import NoSuchElementException

from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

class TestCheckAddAndDeleteCartAmazon(BaseTest):
    def test_check_add_and_delete_cart_amazon(self):
        #1. Go to https://www.amazon.com.tr/

        #2. Verify that you are on the home page
        self.assertEqual(self.driver.current_url, "https://www.amazon.com.tr/")

        # have to manage cookies
        cookie_accept_button_locator = (By.ID, "sp-cc-accept")
        cookie_accept_button_element = self.driver.find_element(*cookie_accept_button_locator)
        cookie_accept_button_element.click()
        #3. Type 'samsung' in the search field at the top of the screen and perform search.
        search_area_locator = (By.ID, "twotabsearchtextbox")
        search_area_element = self.driver.find_element(*search_area_locator)
        search_area_element.send_keys("samsung", Keys.ENTER)

        #4. Verify that there are results for Samsung on the page that appears.
        #first approach
        products_list_locator = (By.CSS_SELECTOR, "[data-cy='title-recipe']")
        products_list_elements = self.driver.find_elements(*products_list_locator)
        self.assertTrue(len(products_list_elements) > 1)

        #second approach
        products_info_locator = (By.XPATH, "//*[@class='a-size-base a-spacing-small a-spacing-top-small a-text-normal']")
        product_info_element_text = self.driver.find_element(*products_info_locator).text.split(' ')[0]
        product_info_element_text = product_info_element_text.replace(".", "")
        product_result_number = int(product_info_element_text)
        self.assertTrue(product_result_number > 0)

        #5. Click on the 2nd page from the search results and verify that the 2nd page is
        #currently displayed on the page that opens.
        second_page_button_locator = (By.CSS_SELECTOR, "[aria-label='2 sayfasına git']")
        second_page_button_element = self.driver.find_element(*second_page_button_locator)
        hover = ActionChains(self.driver)
        hover.move_to_element(second_page_button_element).perform()
        second_page_button_element.click()

        #first approach
        second_page_url = self.driver.current_url
        self.assertTrue(second_page_url.__contains__("page=2"))

        #second approach
        #hover = ActionChains(self.driver)
        current_page_button_locator = (By.CSS_SELECTOR, "[aria-current='page']")
        current_page_button_element = self.driver.find_element(*current_page_button_locator)
        hover.move_to_element(current_page_button_element).perform()
        self.assertEqual("2", current_page_button_element.text)

        #6. Go to the 3rd Product page from the top
        products_list_elements = self.driver.find_elements(*products_list_locator)
        hover.move_to_element(products_list_elements[2]).perform()
        products_list_elements[2].click()

        #7. Verify that you are on the product page
        product_title_locator = (By.CSS_SELECTOR, "span#productTitle")
        product_title_element = self.driver.find_element(*product_title_locator)
        product_title_text = product_title_element.text
        self.assertTrue(product_title_element.is_displayed())

        #8. Add the product to the cart
        add_to_cart_button_locator = (By.ID, "add-to-cart-button")
        add_to_cart_button_element = self.driver.find_element(*add_to_cart_button_locator)
        hover.move_to_element(add_to_cart_button_element).perform()
        add_to_cart_button_element.click()
        #9. Verify that the product has been added to the cart

        #first approach
        time.sleep(3)
        cart_count_locator = (By.ID, "nav-cart-count")
        cart_count_element = self.driver.find_element(*cart_count_locator)
        self.assertEqual(int(cart_count_element.text), 1)

        #second approach
        add_to_cart_message_locator = (By.XPATH, "//*[@class='a-fixed-left-grid']//h1")
        add_to_cart_message_element_text = self.driver.find_element(*add_to_cart_message_locator).text
        self.assertEqual(add_to_cart_message_element_text, "Sepete eklendi")

        #10. Go to the cart page
        cart_page_button_locator = (By.ID, "nav-cart")
        cart_page_button_element = self.driver.find_element(*cart_page_button_locator)
        cart_page_button_element.click()
        time.sleep(2)

        #11. Verify that you are on the cart page and that the correct product has been added to
        #the cart
        cart_product_full_name_locator = (By.CSS_SELECTOR, "[class='a-truncate-full a-offscreen']")
        cart_product_full_name_element = self.driver.find_element(*cart_product_full_name_locator)
        self.assertEqual(product_title_text, cart_product_full_name_element.get_attribute("textContent"))

        #12. Delete the product from the cart and verify that it has been deleted
        product_count_in_cart_locator = (By.CSS_SELECTOR, "[data-a-selector='value']")
        product_count_in_cart_element = self.driver.find_element(*product_count_in_cart_locator)
        product_count_in_card_size = int(product_count_in_cart_element.text)

        decrement_cart_size_locator = (By.CSS_SELECTOR, "[data-a-selector='decrement-icon']")
        decrement_cart_size_element = self.driver.find_element(*decrement_cart_size_locator)

        for i in range(product_count_in_card_size):
            decrement_cart_size_element.click()

        #first approach
        subtotal_amount_after_delete_locator = (By.ID, "sc-subtotal-label-activecart")
        subtotal_amount_after_delete_element = (self.
                                                driver.
                                                find_element(*subtotal_amount_after_delete_locator))
        subtotal_amount_after_delete_size = int(subtotal_amount_after_delete_element.text.split(' ')[2].replace("(", ""))
        self.assertEqual(0, subtotal_amount_after_delete_size)

        #second approach
        msg_after_delete_locator = (By.CLASS_NAME, "sc-list-item-removed-msg-text-delete")
        msg_after_delete_element = self.driver.find_element(*msg_after_delete_locator)
        self.assertTrue(msg_after_delete_element.text.__contains__("kaldırıldı."))

        #13. Return to the home page and verify that it is on the home page
        home_page_logo_locator = (By.ID, "nav-logo-sprites")
        home_page_logo_element = self.driver.find_element(*home_page_logo_locator)
        home_page_logo_element.click()
        self.assertEqual(self.driver.current_url, "https://www.amazon.com.tr/ref=nav_logo")

