import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.product_details import ProductDetailsPage
from pages.products import ProductsPage
from pages.view_cart import ViewCart


class AddToCart(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(4)
        self.driver.get('https://automationexercise.com/')

        self.products_page = ProductsPage(self.driver)
        self.view_cart_page = ViewCart(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)

        self.products_page.close_ad()
        self.products_page.navigate_to_products()

    def test_add_products_to_cart(self):
        product1_name, product1_price = self.products_page.add_product_to_cart('unicorn', 'ContinueShopping')
        product2_name, product2_price = self.products_page.add_product_to_cart('jeans', 'ViewCart')

        number_of_products_in_cart = self.view_cart_page.amount_of_products_in_cart()

        product1_cart_name, product2_cart_name = self.view_cart_page.get_product_names_in_cart()
        product1_cart_price, product2_cart_price = self.view_cart_page.get_product_prices_in_cart()

        self.assertEqual(number_of_products_in_cart, 2)
        self.assertEqual(product1_name, product1_cart_name)
        self.assertEqual(product2_name, product2_cart_name)
        self.assertEqual(product1_price, product1_cart_price)
        self.assertEqual(product2_price, product2_cart_price)

    def test_positive_quantity_in_cart(self):
        amount1, amount2 = 3, 4
        self.products_page.select_random_category()
        self.products_page.view_product()
        _, product_price, _ = self.product_details_page.get_product_details()
        self.product_details_page.set_quantity(amount1)
        self.product_details_page.add_to_cart('ContinueShopping')
        self.product_details_page.set_quantity(amount2)
        self.product_details_page.add_to_cart('ViewCart')

        quantity_in_cart = self.view_cart_page.get_quantity_of_product()
        self.assertEqual(int(amount1+amount2), quantity_in_cart, 'The quantity does not match!')

        total_price = int(product_price) * int(amount1+amount2)
        cart_price = int(self.view_cart_page.get_product_prices_in_cart()[0])
        self.assertEqual(total_price, cart_price, 'The price does not match!')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
