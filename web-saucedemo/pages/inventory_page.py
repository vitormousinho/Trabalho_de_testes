from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    _inventory_container = (By.ID, "inventory_container")
    _cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def wait_loaded(self) -> None:
        self.wait(40).until(EC.url_contains("inventory"))
        self.wait(40).until(EC.presence_of_element_located(self._inventory_container))

    def add_backpack_to_cart(self) -> None:
        btn = self.wait(40).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def open_cart(self) -> None:
        icon = self.wait(40).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        )
        self.driver.execute_script("arguments[0].click();", icon)
        self.wait(40).until(EC.url_contains("cart"))

    def cart_badge_count(self) -> int:
        els = self.driver.find_elements(*self._cart_badge)
        return int(els[0].text) if els else 0
