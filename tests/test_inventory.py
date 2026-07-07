from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_backpack_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.get_cart_badge()).to_have_text("1")
