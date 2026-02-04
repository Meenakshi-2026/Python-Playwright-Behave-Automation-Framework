import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import config

def test_successful_login(page):
    # Test login with valid credentials
    print("\n" + "="*50)
    print("Test: Successful Login")
    print("="*50)
    
    # Initialize pages
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    # Navigate to login page
    login_page.navigate_to_url(config.APP_URL)
    
    # Perform login
    login_page.login()
    
    # Verify inventory page
    assert inventory_page.is_inventory_page_loaded(), "Inventory page not loaded"
    print("Inventory page loaded successfully")
    
    # Verify page title
    title = inventory_page.get_page_title()
    print(f"Page title: {title}")
    
    # Get product count
    product_count = inventory_page.get_product_count()
    print(f"Products displayed: {product_count}")
    
    # Logout
    inventory_page.logout()
    print("Test Passed!")


def test_login_with_invalid_credentials(page):
    # Test login error handling with invalid credentials
    print("\n" + "="*50)
    print("Test: Invalid Credentials Login")
    print("="*50)
    
    # Initialize pages
    login_page = LoginPage(page)
    
    # Navigate to login page
    login_page.navigate_to_url(config.APP_URL)
    
    # Try login with invalid credentials
    login_page.login_with_invalid_credentials("invalid_user", "invalid_pass")
    
    # Verify error message
    assert login_page.is_error_message_displayed(), "Error message not displayed"
    error_message = login_page.get_error_message()
    print(f"Error message displayed: {error_message}")
    print("Test Passed!")


def test_add_item_to_cart(page):
    # Test adding item to cart functionality
    print("\n" + "="*50)
    print("Test: Add Item to Cart")
    print("="*50)
    
    # Initialize pages
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    # Navigate and login
    login_page.navigate_to_url(config.APP_URL)
    login_page.login()
    
    # Verify inventory page
    assert inventory_page.is_inventory_page_loaded(), "Inventory page not loaded"
    print("Inventory page loaded")
    
    # Add item to cart
    inventory_page.add_item_to_cart()
    print("Item added to cart")
    
    # Logout
    inventory_page.logout()
    print("Test Passed!")