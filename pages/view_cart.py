from selenium.webdriver.common.by import By

from pages.base import BasePage


class ViewCart(BasePage):

    view_cart_tab_selector = (By.CSS_SELECTOR, '.shop-menu a[href="/view_cart"')
    checkout_selector = (By.CSS_SELECTOR, 'a[class="btn btn-default check_out"]')

    def check_cart(self):
        self.driver.find_element(*self.view_cart_tab_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_selector).click()
