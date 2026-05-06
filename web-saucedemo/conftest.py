import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,768")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def sauce_user() -> str:
    return os.getenv("SAUCE_USERNAME", "standard_user")


@pytest.fixture
def sauce_password() -> str:
    return os.getenv("SAUCE_PASSWORD", "secret_sauce")

