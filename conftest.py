"""Pytest fixtures live here."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.application import Application


@pytest.fixture(scope="session")
def app():
    base_url = 'https://qacoursemoodle.innopolis.university/login/index.php'
    headless_type = True

    if headless_type:
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
    fixture.quit()
