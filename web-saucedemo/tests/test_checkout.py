from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.inventory_page import InventoryPage


class TestCheckout:
    def test_finalizar_compra_completa(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.wait_loaded()
        inventory.add_backpack_to_cart()
        inventory.open_cart()

        cart = CartPage(logged_in_driver)
        cart.wait_loaded()
        assert cart.items_count() == 1
        cart.start_checkout()

        info = CheckoutInformationPage(logged_in_driver)
        info.wait_loaded()
        info.fill_and_continue("Vitor", "QA", "01000000")

        overview = CheckoutOverviewPage(logged_in_driver)
        overview.wait_loaded()
        overview.finish()

        done = CheckoutCompletePage(logged_in_driver)
        done.wait_loaded()
        assert "checkout-complete" in logged_in_driver.current_url
        assert "Thank you for your order" in done.header_text()
