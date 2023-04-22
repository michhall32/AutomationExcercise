from selenium.webdriver.common.by import By

from pages.base import BasePage


class ViewCart(BasePage):

    cart_tab_selector = (By.CSS_SELECTOR, '.shop-menu a[href="/view_cart"')

    cart_items_selector = (By.CSS_SELECTOR, '.cart_info tbody tr')
    cart_item_name = (By.CSS_SELECTOR, '.cart_description a')
    cart_item_price = (By.CSS_SELECTOR, '.cart_total p')
    quantity_indicator_selector = (By.CLASS_NAME, 'cart_quantity')

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_tab_selector).click()

    def amount_of_products_in_cart(self):
        elements = self.driver.find_elements(*self.cart_items_selector)
        return len(elements)

    def get_product_names_in_cart(self):
        list_of_names = []
        names = self.driver.find_elements(*self.cart_item_name)
        for name in names:
            list_of_names.append(name.text)

        return list_of_names

    def get_product_prices_in_cart(self):
        list_of_prices = []
        prices = self.driver.find_elements(*self.cart_item_price)
        for price in prices:
            list_of_prices.append(price.text.strip('Rs. '))

        return list_of_prices

    def get_quantity_of_product(self):
        return int(self.driver.find_element(*self.quantity_indicator_selector).text)

