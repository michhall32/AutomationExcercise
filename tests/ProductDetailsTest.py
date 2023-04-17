import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.products import ProductsPage
from pages.product_details import ProductDetailsPage
from utilities.DataGiver import getRandomData
from utilities.DataGiver import REVIEW_SUCCESS_MESSAGE, CORRECT_EMAIL


class ProductDetails(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(4)
        self.driver.get('https://automationexercise.com/')

        self.products_page = ProductsPage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)

        self.products_page.close_ad()
        self.products_page.navigate_to_products()

    def test_product_details(self):
        subcategory_name1 = self.products_page.select_random_category()
        product_price1, product_name1 = self.products_page.view_product()
        product_name2, product_price2, subcategory_name2 = self.product_details_page.product_details()
        self.assertEqual(product_name1, product_name2, 'The name of the product is not the same!')
        self.assertEqual(product_price1, product_price2, 'The price of the product is not the same!')
        self.assertIn(subcategory_name1, subcategory_name2, 'The category of the product is not the same')

    def test_review_form(self):
        self.products_page.select_random_category()
        self.products_page.view_product()
        self.product_details_page.send_review_form(getRandomData(6), CORRECT_EMAIL, getRandomData(300))
        self.assertEqual(REVIEW_SUCCESS_MESSAGE, self.product_details_page.review_success_message())


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
