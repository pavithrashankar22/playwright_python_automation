class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.page_title = page.locator(".title")
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.backpack_add_to_cart_button = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_page_title(self):
        return self.page_title

    def get_shopping_cart_icon(self):
        return self.shopping_cart

    def add_backpack_to_cart(self):
        self.backpack_add_to_cart_button.click()

    def get_cart_badge(self):
        return self.cart_badge
