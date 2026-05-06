from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    _summary = (By.ID, "checkout_summary_container")
    _finish_btn = (By.ID, "finish")

    def wait_loaded(self) -> None:
        self.wait().until(EC.url_contains("checkout-step-two"))
        self.wait().until(EC.visibility_of_element_located(self._summary))
        self.wait().until(EC.element_to_be_clickable(self._finish_btn))

    def finish(self) -> None:
        btn_finish = self.driver.find_element(*self._finish_btn)
        self.driver.execute_script("arguments[0].click();", btn_finish)
        self.wait().until(EC.url_contains("checkout-complete"))

