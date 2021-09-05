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
            "Неверный логин или пароль, попробуйте заново." \
            == app.login.find_element(
                (By.ID, "loginerrormessage")
            ).text, "Тест на вход для случайных данных."
