from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    _inventory_container = (By.ID, "inventory_container")
    _cart_link = (By.CLASS_NAME, "shopping_cart_link")
    _cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def wait_loaded(self) -> None:
        self.wait().until(EC.visibility_of_element_located(self._inventory_container))

    def add_backpack_to_cart(self) -> None:
        btn = self.wait(30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait(30).until(
            lambda d: d.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        )

    def remove_backpack_from_cart(self) -> None:
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def open_cart(self) -> None:
        self.driver.find_element(*self._cart_link).click()

    def cart_badge_count(self) -> int:
        els = self.driver.find_elements(*self._cart_badge)
        return int(els[0].text) if els else 0

