from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


class TestCarrinho:
    def test_adicionar_produto_ao_carrinho(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.wait_loaded()
        inventory.add_backpack_to_cart()
        assert inventory.cart_badge_count() == 1

        inventory.open_cart()
        cart = CartPage(logged_in_driver)
        cart.wait_loaded()
        assert cart.items_count() == 1

    def test_remover_produto_do_carrinho(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.wait_loaded()
        inventory.add_backpack_to_cart()
        assert inventory.cart_badge_count() == 1

        inventory.open_cart()
        cart = CartPage(logged_in_driver)
        cart.wait_loaded()
        cart.remove_backpack()
        assert cart.items_count() == 0
