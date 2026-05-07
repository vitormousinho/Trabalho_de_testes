from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    _summary = (By.ID, "checkout_summary_container")
    _finish_btn = (By.ID, "finish")

    def wait_loaded(self) -> None:
        self.wait(40).until(EC.url_contains("checkout-step-two"))
        self.wait(40).until(EC.presence_of_element_located(self._summary))

    def finish(self) -> None:
        btn = self.wait(40).until(EC.presence_of_element_located(self._finish_btn))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait(40).until(EC.url_contains("checkout-complete"))
