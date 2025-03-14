from pages.cart_page import CardPage
from pages.components.header_comp import HeaderComp
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage
from tests.base_test import BaseTest


class TestClass(BaseTest):

    def test_check_add_and_delete_cart_amazon(self):
        #1. Go to https://www.amazon.com.tr/
        self.driver.get(self.get_json_config()["base_url"])

        #2. Verify that you are on the home page
        header_comp = HeaderComp(self.driver)
        home_page = HomePage(self.driver)
        self.assertEqual(self.get_base_url(),
                         home_page.get_current_url(),
                         "Error: You're not in the home page!")
        home_page.accept_cookies()

        #3. Type 'samsung' in the search field at the top of the screen and perform search.
        header_comp.search_product("samsung")

        #4. Verify that there are results for Samsung on the page that appears.
        result_page = SearchResultsPage(self.driver)
        product_size = len(result_page.get_products_list())
        self.assertTrue(product_size > 0,
                        "Error: There are no results!")

        #5. Click on the 2nd page from the search results and verify that the 2nd page is
        #currently displayed on the page that opens.
        result_page.click_on_second_page()
        second_page_url = result_page.get_current_url()
        self.assertTrue(second_page_url.__contains__("page=2"),
                        "Error: You're not on the 2nd page!")

        #6. Go to the 3rd Product page from the top
        result_page.click_on_specific_product(3)

        #7. Verify that you are on the product page
        product_page = ProductPage(self.driver)
        product_title_text = product_page.get_product_title().text
        self.assertTrue(product_page.get_product_title().is_displayed(),
                        "Error: You're not on product page!")

        #8. Add the product to the cart
        product_page.add_product_to_card()

        #9. Verify that the product has been added to the cart
        self.assertEqual(header_comp.get_number_of_products_on_cart(), 1,
                         "Error: Product hasn't been added to the cart!")

        #10. Go to the cart page
        header_comp.navigate_to_cart_page()

        #11. Verify that you are on the cart page and that the correct product has been added to
        #the cart
        cart_page = CardPage(self.driver)
        self.assertEqual(product_title_text,
                         cart_page.get_cart_product_full_name(),
                         "Error: Wrong product has been added to the cart!")

        #12. Delete the product from the cart and verify that it has been deleted
        cart_page.delete_product_from_cart()
        self.assertEqual(header_comp.get_number_of_products_on_cart(), 0)

        #13. Return to the home page and verify that it is on the home page
        header_comp.navigate_to_homepage()
        self.assertEqual(cart_page.get_current_url(),
                         "https://www.amazon.com.tr/ref=nav_logo",
                         "Error: You're not on the home page!")
