import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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

        self.products_page.close_ad()
        self.products_page.navigate_to_products()

    def test_add_2_products_to_cart(self):
        product1_name, product1_price = self.products_page.add_product_to_cart('unicorn', 'ContinueShopping')
        product2_name, product2_price = self.products_page.add_product_to_cart('jeans', 'ViewCart')

        number_of_products_in_cart = self.view_cart_page.products_in_cart()

        product1_cart_name, product2_cart_name = self.view_cart_page.product_names_in_cart()
        product1_cart_price, product2_cart_price = self.view_cart_page.product_prices_in_cart()

        self.assertEqual(number_of_products_in_cart, 2)
        self.assertEqual(product1_name, product1_cart_name)
        self.assertEqual(product2_name, product2_cart_name)
        self.assertEqual(product1_price, product1_cart_price)
        self.assertEqual(product2_price, product2_cart_price)


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
