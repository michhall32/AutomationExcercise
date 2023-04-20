from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage


class ProductDetailsPage(BasePage):
    product_name_selector = (By.CSS_SELECTOR, '.product-information h2')
    product_price_selector = (By.CSS_SELECTOR, '.product-information span span')
    subcategory_name_selector = (By.CSS_SELECTOR, '.product-information p')

    quantity_selector = (By.ID, 'quantity')
    add_to_cart_selector = (By.CSS_SELECTOR, 'button[class="btn btn-default cart"]')
    continue_shopping_selector = (By.CLASS_NAME, 'btn-success')
    view_cart_selector = (By.CSS_SELECTOR, '.modal-body a')

    review_name_selector = (By.CSS_SELECTOR, 'form[id="review-form"] input[id="name"]')
    review_email_selector = (By.CSS_SELECTOR, 'form[id="review-form"] input[id="email"]')
    review_message_selector = (By.CSS_SELECTOR, 'form[id="review-form"] textarea[id="review"]')
    review_submit_selector = (By.ID, 'button-review')
    success_message_selector = (By.CSS_SELECTOR, 'form[id="review-form"] div[class="alert-success alert"]')

    def get_product_details(self):
        product_name = self.driver.find_element(*self.product_name_selector).text
        product_price = self.driver.find_element(*self.product_price_selector).text.strip('Rs. ')
        subcategory_name = self.driver.find_element(*self.subcategory_name_selector).text
        return product_name, product_price, subcategory_name.upper()

    def set_quantity(self, amount):
        self.driver.find_element(*self.quantity_selector).clear()
        self.driver.find_element(*self.quantity_selector).send_keys(amount)

    def add_to_cart(self, action):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_selector)).click()
        if action == 'ContinueShopping':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping_selector)).click()
        elif action == 'ViewCart':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.view_cart_selector)).click()

    def send_review_form(self, name, email, message):
        self.driver.find_element(*self.review_name_selector).send_keys(name)
        self.driver.find_element(*self.review_email_selector).send_keys(email)
        self.driver.find_element(*self.review_message_selector).send_keys(message)
        self.driver.find_element(*self.review_submit_selector).click()

    def review_success_message(self):
        return self.driver.find_element(*self.success_message_selector).text

