from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import config

@given('I am on the Saucedemo login page')
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.inventory_page = InventoryPage(context.page)
    context.login_page.navigate_to_url(config.APP_URL)

@when('I login with valid credentials')
def step_impl(context):
    context.login_page.login()

@then('I should see the inventory page')
def step_impl(context):
    assert context.inventory_page.is_inventory_page_loaded(), "Inventory page failed to load"

@when('I login with invalid credentials "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login_with_invalid_credentials(username, password)

@then('I should see an error message')
def step_impl(context):
    assert context.login_page.is_error_message_displayed(), "Error message NOT displayed"
    print(f"Error Message: {context.login_page.get_error_message()}")

