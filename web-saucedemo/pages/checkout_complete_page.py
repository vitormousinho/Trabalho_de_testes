from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    _container = (By.ID, "checkout_complete_container")
    _complete_header = (By.CLASS_NAME, "complete-header")

    def wait_loaded(self) -> None:
        self.wait(40).until(EC.url_contains("checkout-complete"))
        self.wait(40).until(EC.presence_of_element_located(self._container))

    def header_text(self) -> str:
        return self.driver.find_element(*self._complete_header).text.strip()
