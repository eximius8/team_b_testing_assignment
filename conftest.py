"""Pytest fixtures live here."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    '''Фикстура для открытия браузера.'''

    base_url = request.config.getoption("--base-url")
    headless_type = request.config.getoption("--headless").lower()
    if headless_type == "true":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        fixture = Application(
            webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            ),
            base_url,
        )
    else:
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()), base_url)
    yield fixture
    # Чистим после себя
    fixture.quit()


@pytest.fixture
def auth(app, request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_auth_page()
    auth_data = AuthData(login=username, password=password)
    app.login.auth(auth_data)
    assert app.login.is_auth(), "Вход не выполнен"
    yield
    app.login.sign_out()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="'true' для режима без видимого браузера,\n"
        "'false' - для режима где браузер виден",
    ),
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="url сайта для тестирования",
    ),
    parser.addoption(
        "--username", action="store", default="eximius", help="имя пользователя",
    ),
    parser.addoption(
        "--password", action="store", default="!123456789Ab", help="пароль",
    ),
