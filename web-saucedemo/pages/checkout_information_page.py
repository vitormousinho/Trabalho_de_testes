from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

_SET_REACT_VALUE = """
    var setter = Object.getOwnPropertyDescriptor(
        window.HTMLInputElement.prototype, 'value'
    ).set;
    setter.call(arguments[0], arguments[1]);
    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
"""


class CheckoutInformationPage(BasePage):
    _first_name = (By.ID, "first-name")
    _last_name = (By.ID, "last-name")
    _postal_code = (By.ID, "postal-code")
    _continue_btn = (By.ID, "continue")
    _error = (By.CSS_SELECTOR, "[data-test='error']")

    def wait_loaded(self) -> None:
        self.wait(40).until(EC.url_contains("checkout-step-one"))
        self.wait(40).until(EC.presence_of_element_located(self._first_name))

    def fill_and_continue(self, first_name: str, last_name: str, postal_code: str) -> None:
        el_fn = self.wait(40).until(EC.presence_of_element_located(self._first_name))
        self.driver.execute_script(_SET_REACT_VALUE, el_fn, first_name)

        el_ln = self.driver.find_element(*self._last_name)
        self.driver.execute_script(_SET_REACT_VALUE, el_ln, last_name)

        el_zip = self.driver.find_element(*self._postal_code)
        self.driver.execute_script(_SET_REACT_VALUE, el_zip, postal_code)

        btn = self.wait(40).until(EC.presence_of_element_located(self._continue_btn))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait(40).until(EC.url_contains("checkout-step-two"))

    def error_message(self) -> str | None:
        els = self.driver.find_elements(*self._error)
        return els[0].text.strip() if els else None
