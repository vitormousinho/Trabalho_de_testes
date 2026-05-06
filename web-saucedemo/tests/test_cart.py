from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def _login(driver, base_url: str, username: str, password: str) -> None:
    login = LoginPage(driver)
    login.load(base_url)
    login.login(username, password)


class TestCarrinho:
    def test_adicionar_produto_ao_carrinho(self, driver, base_url: str, sauce_user: str, sauce_password: str):
        _login(driver, base_url, sauce_user, sauce_password)

        inventory = InventoryPage(driver)
        inventory.wait_loaded()
        inventory.add_backpack_to_cart()
        assert inventory.cart_badge_count() == 1

        inventory.open_cart()
        cart = CartPage(driver)
        cart.wait_loaded()
        assert cart.items_count() == 1

    def test_remover_produto_do_carrinho(self, driver, base_url: str, sauce_user: str, sauce_password: str):
        _login(driver, base_url, sauce_user, sauce_password)

        inventory = InventoryPage(driver)
        inventory.wait_loaded()
        inventory.add_backpack_to_cart()
        assert inventory.cart_badge_count() == 1

        inventory.open_cart()
        cart = CartPage(driver)
        cart.wait_loaded()
        cart.remove_backpack()
        assert cart.items_count() == 0

