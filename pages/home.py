from selenium.webdriver.common.by import By

from pages.base import BasePage


class HomePage(BasePage):
    home_tab_selector = (By.CSS_SELECTOR, '.shop-menu  a[href="/"]')
    login_tab_selector = (By.CSS_SELECTOR, '.shop-menu  a[href="/login"]')
    username_label_selector = (By.CSS_SELECTOR, "div[class='shop-menu pull-right'] ul li a b")
    delete_account_button_selector = (By.CSS_SELECTOR, '.shop-menu a[href="/delete_account"]')

    def navigate_to_homepage(self):
        self.driver.find_element(*self.home_tab_selector).click()

    def username_is_displayed(self):
        return self.driver.find_element(*self.username_label_selector).text

    def delete_account(self):
        self.driver.find_element(*self.delete_account_button_selector).click()


