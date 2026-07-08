import pytest
from playwright.sync_api import expect
from test_data.users import STANDARD_USER


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_add_backpack_to_cart(login_page, inventory_page):
    login_page.navigate()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.get_cart_badge()).to_have_text("1")