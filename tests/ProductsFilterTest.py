import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.products import ProductsPage


class ProductsFilters(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(4)
        self.driver.get('https://automationexercise.com/')

        self.products_page = ProductsPage(self.driver)

        self.products_page.close_ad()
        self.products_page.navigate_to_products()

    def test_brands(self):
        brands_elements = self.products_page.list_of_brands()
        error_log = []

        for i in range(len(brands_elements)):
            try:
                brand_element = self.products_page.list_of_brands()[i]
                expected_number_of_products = self.products_page.number_of_items(brand_element)
                actual_number_of_products = self.products_page.get_amount_of_visible_products()
                self.assertEqual(expected_number_of_products, actual_number_of_products)
            except AssertionError as e:
                error = f'Element no. {i + 1} from the list failed. More details: {e}'
                error_log.append(error)
                continue

        self.assertTrue(error_log == [], '\n' + '\n'.join(error_log))

    def test_category(self):
        subcategory_name = self.products_page.select_random_category()
        products_amount = self.products_page.get_amount_of_visible_products()
        products_name = self.products_page.get_name_of_random_visible_product()
        self.assertGreater(products_amount, 0, 'This subcategory does not have any products in it.')
        self.assertIn(subcategory_name, products_name.upper(), "This product does not have category's name in it")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
