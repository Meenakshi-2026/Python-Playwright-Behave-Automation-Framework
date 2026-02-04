from pages.base_page import BasePage
import config

class LoginPage(BasePage):
    """
    Login Page Object - Contains all locators and methods for the login page.
    This class represents the Saucedemo login page.
    """

    # Locators (CSS selectors for page elements)
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def login(self, username: str = config.USERNAME, password: str = config.PASSWORD):
        # Login with provided or default credentials
        print(f"Logging in with username: {username}")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def login_with_invalid_credentials(self, username: str, password: str):
        # Attempt login with invalid credentials
        print(f"Logging in with invalid credentials: {username}")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.page.wait_for_timeout(2000)

    def get_error_message(self) -> str:
        # Get error message text from login page
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_message_displayed(self) -> bool:
        # Check if error message is visible on login page
        return self.is_element_visible(self.ERROR_MESSAGE)
