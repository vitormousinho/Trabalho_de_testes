from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def _login(driver, base_url: str, username: str, password: str) -> None:
    login = LoginPage(driver)
    login.load(base_url)
    login.login(username, password)


class TestCheckout:
    def test_finalizar_compra_completa(self, driver, base_url: str, sauce_user: str, sauce_password: str):
        _login(driver, base_url, sauce_user, sauce_password)

        inventory = InventoryPage(driver)
        inventory.wait_loaded()
        inventory.add_backpack_to_cart()
        inventory.open_cart()

        cart = CartPage(driver)
        cart.wait_loaded()
        assert cart.items_count() == 1
        cart.start_checkout()

        info = CheckoutInformationPage(driver)
        info.wait_loaded()
        info.fill_and_continue("Vitor", "QA", "01000000")

        overview = CheckoutOverviewPage(driver)
        overview.wait_loaded()
        overview.finish()

        done = CheckoutCompletePage(driver)
        done.wait_loaded()
        assert "checkout-complete" in driver.current_url
        assert "Thank you for your order" in done.header_text()

