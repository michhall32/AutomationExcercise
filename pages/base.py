from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    home_tab_selector = (By.CSS_SELECTOR, '.shop-menu  a[href="/"]')
    login_tab_selector = (By.CSS_SELECTOR, '.shop-menu  a[href="/login"]')

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def get_button_color(self, tab):
        if tab == 'home_tab':
            style = self.driver.find_element(*self.home_tab_selector).get_attribute('style')
        elif tab == 'login_tab':
            style = self.driver.find_element(*self.login_tab_selector).get_attribute('style')
        color = style[7:-1]
        return color
