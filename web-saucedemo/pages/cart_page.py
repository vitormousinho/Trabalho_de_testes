from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    _cart_list = (By.CLASS_NAME, "cart_list")
    _cart_items = (By.CLASS_NAME, "cart_item")
    _checkout_btn = (By.ID, "checkout")

    def wait_loaded(self) -> None:
        self.wait().until(EC.visibility_of_element_located(self._cart_list))

    def items_count(self) -> int:
        return len(self.driver.find_elements(*self._cart_items))

    def remove_backpack(self) -> None:
        btn = self.wait(30).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        )
        btn.click()
        self.wait(30).until(
            lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) == 0
        )

    def start_checkout(self) -> None:
        self.wait(30).until(EC.element_to_be_clickable(self._checkout_btn)).click()

