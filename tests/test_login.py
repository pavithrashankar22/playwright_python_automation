import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.users import STANDARD_USER, INVALID_USER, LOCKED_OUT_USER


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    expect(inventory_page.get_page_title()).to_have_text("Products")
    expect(inventory_page.get_shopping_cart_icon()).to_be_visible()


@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize(
    "user_data",
    [
        INVALID_USER,
        LOCKED_OUT_USER,
    ],
)
def test_login_error_scenarios(page, user_data):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(user_data["username"], user_data["password"])

    expect(login_page.get_error_message()).to_contain_text(
        user_data["expected_error"]
    )