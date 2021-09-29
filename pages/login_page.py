"""Страница входа в приложение moodle."""
from locators.auth_locators import AuthLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page to check login of users."""

    def is_auth(self):
        """Проверка, что вход был осуществлен."""

        element = self.find_elements(AuthLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def confirm_exit_window(self):
        element = self.find_elements(AuthLocators.CONFIRM_EXIT_BUTTON)
        if len(element) > 0:
            return True
        return False

    def auth(self, data):
        """Функция входа в личный кабинет."""

        login = data.username
        password = data.password
        self.fill_element(self.find_element(AuthLocators.USERNAME), login)
        self.fill_element(self.find_element(AuthLocators.PASSWORD), password)
        self.click_element(self.find_element(AuthLocators.LOGIN_BTN))

    def sign_out(self):
        """Выйти из системы."""

        if self.is_auth():
            self.click_element(self.find_element(AuthLocators.USER_MENU))
            self.click_element(self.find_element(AuthLocators.EXIT))
        if self.confirm_exit_window():
            self.click_element(self.find_element(AuthLocators.CONFIRM_EXIT_BUTTON))
