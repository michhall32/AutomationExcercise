from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.CSS_SELECTOR, '.shop-menu a[href="/products"]')
    brands_button_selector = (By.CSS_SELECTOR, '.brands-name span')
    products_items_selector = (By.CSS_SELECTOR, '.single-products .productinfo p')

    category_button_selector = (By.CSS_SELECTOR, '.category-products .panel-title a')
    subcategory_button_selector = (By.CSS_SELECTOR, '.category-products div[class="panel-collapse in"] li a')

    def close_ad(self):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.refresh()

    def navigate_to_products(self):
        self.driver.find_element(*self.products_tab_selector).click()

    def list_of_brands(self):
        return self.driver.find_elements(*self.brands_button_selector)

    def number_of_items(self, brand_element):
        number_of_items = int(brand_element.text.strip('()'))
        brand_element.click()
        return number_of_items

    def get_amount_of_visible_products(self):
        products = self.driver.find_elements(*self.products_items_selector)
        return len(products)

    def get_name_of_random_visible_product(self):
        products = self.driver.find_elements(*self.products_items_selector)
        product = random.choice(products)
        return product.text

    def select_random_category(self):
        categories = self.driver.find_elements(*self.category_button_selector)
        random.choice(categories).click()
        subcategories = WebDriverWait(self.driver, 6).until(EC.presence_of_all_elements_located(self.subcategory_button_selector))
        subcategory = random.choice(subcategories)
        subcategory_name = subcategory.text
        subcategory.click()
        return subcategory_name
