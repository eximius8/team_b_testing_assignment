"""Страница входа в приложение moodle."""
from locators.auth_locators import AuthLocators
from locators.profile_locators import EditProfileLocators
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

    def user_menu(self):
        return self.find_element(AuthLocators.USER_MENU)

    def user_menu_settings(self):
        return self.find_element(AuthLocators.USER_MENU_SETTINGS)

    def go_to_editing_personal_data(self):
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(EditProfileLocators.EDIT_INFO))

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
