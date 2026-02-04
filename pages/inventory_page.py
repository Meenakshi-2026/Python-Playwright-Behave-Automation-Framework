from pages.base_page import BasePage

class InventoryPage(BasePage):
    """
    Inventory Page Object - Contains all locators and methods for the inventory page.
    This class represents the Saucedemo products inventory page.
    """

    # Locators (CSS selectors for page elements)
    PRODUCT_TITLE = ".title"
    PRODUCT_ITEMS = "[data-test='inventory-item']"
    ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"
    CART_ICON = "[data-test='shopping-cart-link']"
    LOGOUT_BUTTON = "#logout_sidebar_link"
    MENU_BUTTON = "#react-burger-menu-btn"

    def is_inventory_page_loaded(self) -> bool:
        # Check if inventory page is loaded
        return self.is_element_visible(self.PRODUCT_TITLE)

    def get_page_title(self) -> str:
        # Get inventory page title
        return self.get_text(self.PRODUCT_TITLE)

    def add_item_to_cart(self):
        # Add product to cart
        print("Adding item to cart")
        self.click(self.ADD_TO_CART_BUTTON)
        self.page.wait_for_timeout(1000)

    def open_cart(self):
        # Open cart page
        print("Opening cart")
        self.click(self.CART_ICON)
        self.page.wait_for_load_state("networkidle")

    def open_menu(self):
        # Open side menu
        self.click(self.MENU_BUTTON)
        self.page.wait_for_timeout(500)

    def logout(self):
        # Logout from application
        print("Logging out")
        self.open_menu()
        self.click(self.LOGOUT_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def get_product_count(self) -> int:
        # Get count of products on page
        return len(self.page.query_selector_all(self.PRODUCT_ITEMS))
