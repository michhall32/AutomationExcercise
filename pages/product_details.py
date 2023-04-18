from selenium.webdriver.common.by import By

from pages.base import BasePage


class ProductDetailsPage(BasePage):
    product_name_selector = (By.CSS_SELECTOR, '.product-information h2')
    product_price_selector = (By.CSS_SELECTOR, '.product-information span span')
    subcategory_name_selector = (By.CSS_SELECTOR, '.product-information p')

    review_name_selecor = (By.CSS_SELECTOR, 'form[id="review-form"] input[id="name"]')
    review_email_selector = (By.CSS_SELECTOR, 'form[id="review-form"] input[id="email"]')
    review_message_selector = (By.CSS_SELECTOR, 'form[id="review-form"] textarea[id="review"]')
    review_submit_selector = (By.ID, 'button-review')
    success_message_selector = (By.CSS_SELECTOR, 'form[id="review-form"] div[class="alert-success alert"]')

    def product_details(self):
        product_name = self.driver.find_element(*self.product_name_selector).text
        product_price = self.driver.find_element(*self.product_price_selector).text
        subcategory_name = self.driver.find_element(*self.subcategory_name_selector).text
        return product_name, product_price, subcategory_name.upper()

    def send_review_form(self, name, email, message):
        self.driver.find_element(*self.review_name_selecor).send_keys(name)
        self.driver.find_element(*self.review_email_selector).send_keys(email)
        self.driver.find_element(*self.review_message_selector).send_keys(message)
        self.driver.find_element(*self.review_submit_selector).click()

    def review_success_message(self):
        return self.driver.find_element(*self.success_message_selector).text
