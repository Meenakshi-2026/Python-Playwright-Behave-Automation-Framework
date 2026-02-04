from playwright.sync_api import Page
import config
from datetime import datetime
import os

class BasePage:
    """
    Base Page class that contains common methods used across all page objects.
    This class handles navigation, waiting, clicking, and taking screenshots.
    """

    def __init__(self, page: Page):
        # Initialize with Playwright Page object
        self.page = page
        self.timeout = config.TIMEOUT

    def navigate_to_url(self, url: str):
        # Navigate to a specific URL
        self.page.goto(url)

    def click(self, selector: str):
        # Click on an element by CSS selector
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        # Fill text field with provided text
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        # Get text content of an element
        return self.page.text_content(selector)

    def wait_for_element(self, selector: str):
        # Wait for element to be visible on page
        self.page.wait_for_selector(selector, timeout=self.timeout)

    def take_screenshot(self, name: str):
        # Take screenshot of current page with timestamp
        if config.TAKE_SCREENSHOTS:
            # Create screenshots directory if it doesn't exist
            if not os.path.exists(config.SCREENSHOT_PATH):
                os.makedirs(config.SCREENSHOT_PATH)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{config.SCREENSHOT_PATH}{name}_{timestamp}.png"
            self.page.screenshot(path=filename)
            print(f"Screenshot saved: {filename}")

    def is_element_visible(self, selector: str) -> bool:
        # Check if element is visible on page
        try:
            self.page.wait_for_selector(selector, timeout=5000)
            return True
        except:
            return False

    def close(self):
        # Close the page
        self.page.close()
