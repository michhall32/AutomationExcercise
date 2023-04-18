from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.CSS_SELECTOR, '.shop-menu a[href="/products"]')
    brands_button_selector = (By.CSS_SELECTOR, '.brands-name span')
    product_item_selector = (By.CSS_SELECTOR, '.single-products .productinfo p')

    category_button_selector = (By.CSS_SELECTOR, '.category-products .panel-title a')
    subcategory_button_selector = (By.CSS_SELECTOR, '.category-products div[class="panel-collapse in"] li a')

    view_product_selector = (By.CSS_SELECTOR, '.choose a')
    product_price_selector = (By.CSS_SELECTOR, '.single-products h2')

    searchbox_selector = (By.CSS_SELECTOR, '.container #search_product')
    search_button_selector = (By.CSS_SELECTOR, "button[id='submit_search']")
    add_to_cart_selector = (By.CSS_SELECTOR, '.overlay-content .add-to-cart')
    continue_shopping_selector = (By.CLASS_NAME, 'btn-success')
    view_cart_selector = (By.CSS_SELECTOR, '.modal-body a')

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
        products = self.driver.find_elements(*self.product_item_selector)
        return len(products)

    def get_name_of_random_visible_product(self):
        products = self.driver.find_elements(*self.product_item_selector)
        product = random.choice(products)
        return product.text

    def select_random_category(self):
        categories = self.driver.find_elements(*self.category_button_selector)
        random.choice(categories).click()
        subcategories = WebDriverWait(self.driver, 6).until(
            EC.presence_of_all_elements_located(self.subcategory_button_selector))
        subcategory = random.choice(subcategories)
        subcategory_name = subcategory.text
        subcategory.click()
        return subcategory_name

    def view_product(self):
        product_price = self.driver.find_element(*self.product_price_selector).text
        product_name = self.driver.find_element(*self.product_item_selector).text
        self.driver.find_element(*self.view_product_selector).click()
        return product_price, product_name

    def add_product_to_cart(self, item_name, action):
        self.driver.find_element(*self.searchbox_selector).clear()
        self.driver.find_element(*self.searchbox_selector).send_keys(item_name)
        self.driver.find_element(*self.search_button_selector).click()

        product = self.driver.find_element(*self.product_item_selector)
        product_name = self.driver.find_element(*self.product_item_selector).text
        product_price = self.driver.find_element(*self.product_price_selector).text.strip('Rs. ')
        ActionChains(self.driver).move_to_element(product).perform()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_selector)).click()
        if action == 'ContinueShopping':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping_selector)).click()
        elif action == 'ViewCart':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.view_cart_selector)).click()

        return product_name, product_price
