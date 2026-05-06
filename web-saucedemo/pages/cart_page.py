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
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        self.wait().until_not(EC.presence_of_element_located(self._cart_items))

    def start_checkout(self) -> None:
        self.driver.find_element(*self._checkout_btn).click()

