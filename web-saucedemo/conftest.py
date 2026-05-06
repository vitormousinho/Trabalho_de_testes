import os

import pytest
from pages.login_page import LoginPage
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
    options.add_argument("--disable-gpu")
    options.add_argument("--single-process")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=9222")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def sauce_user() -> str:
    return os.getenv("SAUCE_USERNAME", "standard_user")


@pytest.fixture
def sauce_password() -> str:
    return os.getenv("SAUCE_PASSWORD", "secret_sauce")


@pytest.fixture
def logged_in_driver(driver, base_url: str, sauce_user: str, sauce_password: str):
    page = LoginPage(driver)
    page.load(base_url)
    page.login(sauce_user, sauce_password)
    return driver

