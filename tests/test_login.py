import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.get_page_title()).to_have_text("Products")
    expect(inventory_page.get_shopping_cart_icon()).to_be_visible()


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "wrong_user",
            "wrong_password",
            "Username and password do not match",
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Sorry, this user has been locked out",
        ),
    ],
)
def test_login_error_scenarios(page, username, password, expected_error):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, password)

    expect(login_page.get_error_message()).to_contain_text(expected_error)