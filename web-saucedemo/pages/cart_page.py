from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    _cart_list = (By.CLASS_NAME, "cart_list")
    _cart_items = (By.CLASS_NAME, "cart_item")

    def wait_loaded(self) -> None:
        self.wait(40).until(EC.url_contains("cart"))
        self.wait(40).until(EC.presence_of_element_located(self._cart_list))

    def items_count(self) -> int:
        return len(self.driver.find_elements(*self._cart_items))

    def remove_backpack(self) -> None:
        btn = self.wait(40).until(
            EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack"))
        )
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait(40).until(
            lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) == 0
        )

    def start_checkout(self) -> None:
        btn = self.wait(40).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait(40).until(EC.url_contains("checkout-step-one"))
