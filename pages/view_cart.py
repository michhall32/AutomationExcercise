from selenium.webdriver.common.by import By

from pages.base import BasePage


class ViewCart(BasePage):

    cart_items_selector = (By.CSS_SELECTOR, '.cart_info tbody tr')
    cart_item_name = (By.CSS_SELECTOR, '.cart_description a')
    cart_item_price = (By.CSS_SELECTOR, '.cart_total p')

    def products_in_cart(self):
        elements = self.driver.find_elements(*self.cart_items_selector)
        return len(elements)

    def product_names_in_cart(self):
        list_of_names = []
        names = self.driver.find_elements(*self.cart_item_name)
        for name in names:
            list_of_names.append(name.text)

        return list_of_names

    def product_prices_in_cart(self):
        list_of_prices = []
        prices = self.driver.find_elements(*self.cart_item_price)
        for price in prices:
            list_of_prices.append(price.text.strip('Rs. '))

        return list_of_prices


