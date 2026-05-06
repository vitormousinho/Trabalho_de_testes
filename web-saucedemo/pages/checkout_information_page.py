from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    _js_set_field = """
        const input = arguments[0];
        const text = arguments[1];
        const setter = Object.getOwnPropertyDescriptor(
          window.HTMLInputElement.prototype,
          'value'
        ).set;
        setter.call(input, text);
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """
    _first_name = (By.ID, "first-name")
    _last_name = (By.ID, "last-name")
    _postal_code = (By.ID, "postal-code")
    _continue_btn = (By.ID, "continue")
    _error = (By.CSS_SELECTOR, "[data-test='error']")

    def wait_loaded(self) -> None:
        self.wait().until(EC.visibility_of_element_located(self._first_name))

    def fill_and_continue(self, first_name: str, last_name: str, postal_code: str) -> None:
        el_fn = self.driver.find_element(*self._first_name)
        el_ln = self.driver.find_element(*self._last_name)
        el_zip = self.driver.find_element(*self._postal_code)
        self.driver.execute_script(self._js_set_field, el_fn, first_name)
        self.driver.execute_script(self._js_set_field, el_ln, last_name)
        self.driver.execute_script(self._js_set_field, el_zip, postal_code)
        btn_continue = self.wait(40).until(EC.element_to_be_clickable(self._continue_btn))
        self.driver.execute_script("arguments[0].click();", btn_continue)

        def _navigated_or_error(drv) -> bool:
            if "checkout-step-two" in drv.current_url:
                return True
            return len(drv.find_elements(*self._error)) > 0

        self.wait(40).until(_navigated_or_error)
        if "checkout-step-two" not in self.driver.current_url:
            raise AssertionError(self.error_message() or "Falha ao avançar no checkout")

    def error_message(self) -> str | None:
        els = self.driver.find_elements(*self._error)
        return els[0].text.strip() if els else None

