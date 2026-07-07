class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.page_title = page.locator(".title")
        self.shopping_cart = page.locator(".shopping_cart_link")

    def get_page_title(self):
        return self.page_title

    def get_shopping_cart_icon(self):
        return self.shopping_cart
