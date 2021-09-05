"""Страница входа в приложение moodle."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page to check login of users."""

    def auth(self, data):
        """Функция входа в личный кабинет."""

        login = data.username
        password = data.password
        self.fill_element(self.find_element((By.ID, "username")), login)
        self.fill_element(self.find_element((By.ID, "password")), password)
        self.click_element(self.find_element((By.ID, "loginbtn")))
