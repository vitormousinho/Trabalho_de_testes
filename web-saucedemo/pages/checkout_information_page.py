from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    _first_name = (By.ID, "first-name")
    _last_name = (By.ID, "last-name")
    _postal_code = (By.ID, "postal-code")
    _continue_btn = (By.ID, "continue")
    _error = (By.CSS_SELECTOR, "[data-test='error']")

    def wait_loaded(self) -> None:
        self.wait().until(EC.visibility_of_element_located(self._first_name))

    def fill_and_continue(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.driver.find_element(*self._first_name).clear()
        self.driver.find_element(*self._first_name).send_keys(first_name)
        self.driver.find_element(*self._last_name).clear()
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).clear()
        self.driver.find_element(*self._postal_code).send_keys(postal_code)
        self.wait().until(EC.element_to_be_clickable(self._continue_btn)).click()

        def _navigated_or_error(drv) -> bool:
            if "checkout-step-two" in drv.current_url:
                return True
            return len(drv.find_elements(*self._error)) > 0

        self.wait().until(_navigated_or_error)
        if "checkout-step-two" not in self.driver.current_url:
            raise AssertionError(self.error_message() or "Falha ao avançar no checkout")

    def error_message(self) -> str | None:
        els = self.driver.find_elements(*self._error)
        return els[0].text.strip() if els else None

