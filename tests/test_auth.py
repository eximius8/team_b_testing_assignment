"""Тесты входа в систему находятся здесь."""
from locators.auth_locators import AuthLocators
from models.auth import AuthData


class TestAuth:
    """Тестирование возможности входа в систему."""

    def test_auth_invalid(self, app):
        """Тестирование входа с неверными данными.
        Steps
        1. Открыть страницу авторизации
        2. Сгенерировать случайную пару логин - пароль
        3. Попробовать войти, используя сгенерированные данные
        4. Проверить наличие сообщения о неверном логине и пароле
        """

        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        assert app.login.find_element(AuthLocators.LOGIN_ERROR_MESSAGE).text in [
            "Invalid login, please try again",
            "Неверный логин или пароль, попробуйте заново.",
        ], "Тест на вход для случайных данных."

    def test_auth_valid(self, app):
        """Тестирование входа с верными данными.
        Steps
        1. Открыть страницу авторизации
        2. Войти, используя правильные данные авторизации
        3. Проверить наличие элемента 'Недавно посещенные курсы'
        """

        app.open_auth_page()
        data = AuthData(username="eximius", password="!123456789Ab")
        app.login.auth(data)
        assert (
            app.login.find_element(AuthLocators.RECENT_COURSES).text
            == "Недавно посещенные курсы"
        )
