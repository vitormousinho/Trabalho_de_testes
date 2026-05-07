import os

import pytest
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
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
    driver.get(base_url)
    page = LoginPage(driver)
    page.login(sauce_user, sauce_password)
    WebDriverWait(driver, 40).until(EC.url_contains("inventory"))
    return driver
