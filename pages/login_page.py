"""Страница входа в приложение moodle."""
from locators.auth_locators import AuthLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page to check login of users."""

    def auth(self, data):
        """Функция входа в личный кабинет."""

        login = data.username
        password = data.password
        self.fill_element(self.find_element(AuthLocators.USERNAME), login)
        self.fill_element(self.find_element(AuthLocators.PASSWORD), password)
        self.click_element(self.find_element(AuthLocators.LOGIN_BTN))
