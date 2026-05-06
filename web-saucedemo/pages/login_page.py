from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    _username = (By.ID, "user-name")
    _password = (By.ID, "password")
    _login_btn = (By.ID, "login-button")
    _error = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self, base_url: str) -> None:
        self.open(base_url)

    def login(self, username: str, password: str) -> None:
        self.wait().until(EC.visibility_of_element_located(self._username)).clear()
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._password).clear()
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_btn).click()

    def error_message(self) -> str | None:
        els = self.driver.find_elements(*self._error)
        return els[0].text.strip() if els else None

