"""All pages inherit from BasePage class."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """BaseBage дает удобное представление вебстраниц."""

    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def select_value(self, select_element, value):
        select_element.select_by_value(value)

    @staticmethod
    def set_value_select(element, value):
        return Select(element).select_by_visible_text(value)

    @staticmethod
    def fill_element(element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    @staticmethod
    def click_element(element):
        element.click()
