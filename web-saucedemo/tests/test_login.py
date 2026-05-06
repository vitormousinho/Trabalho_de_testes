import pytest

from pages.login_page import LoginPage


class TestLogin:
    def test_login_valido_redireciona_para_inventory(
        self,
        driver,
        base_url: str,
        sauce_user: str,
        sauce_password: str,
    ):
        page = LoginPage(driver)
        page.load(base_url)
        page.login(sauce_user, sauce_password)
        assert "inventory" in driver.current_url

    @pytest.mark.parametrize(
        "username,password,expected",
        [
            ("standard_user", "senha_errada", "Username and password do not match"),
            ("usuario_inexistente", "secret_sauce", "Username and password do not match"),
            ("", "secret_sauce", "Username is required"),
            ("standard_user", "", "Password is required"),
        ],
    )
    def test_login_invalido_exibe_mensagem_de_erro(self, driver, base_url: str, username, password, expected):
        page = LoginPage(driver)
        page.load(base_url)
        page.login(username, password)
        msg = page.error_message()
        assert msg is not None
        assert expected in msg

