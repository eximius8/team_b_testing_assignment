"""Тесты входа в систему находятся здесь."""
from selenium.webdriver.common.by import By

from models.auth import AuthData


class TestAuth:
    """Тестирование возможности входа в систему."""

    def test_auth_invalid(self, app):
        """Тестирование входа с неверными данными."""

        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        assert \
            app.login.find_element(
                (By.ID, "loginerrormessage")
            ).text in ['Invalid login, please try again',
                       "Неверный логин или пароль, попробуйте заново."], \
            "Тест на вход для случайных данных."
