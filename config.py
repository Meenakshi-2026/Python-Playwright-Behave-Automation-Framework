# Configuration File for Saucedemo Testing
import os

# Application URL
APP_URL = "https://www.saucedemo.com/"

# Browser Configuration
BROWSER_TYPE = "chromium"  # Options: chromium, firefox, webkit
# Support environment variable for CI/CD (GitHub Actions)
HEADLESS_MODE = os.getenv('HEADLESS_MODE', 'False').lower() == 'true'
SLOW_MOTION = 1000  # Milliseconds to slow down execution (0 = no slowdown)
TIMEOUT = 30000  # Timeout in milliseconds for wait operations

# Credentials
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# Screenshot Configuration
TAKE_SCREENSHOTS = True
SCREENSHOT_PATH = "screenshots/"

# Report Configuration
REPORT_PATH = "reports/"
REPORT_NAME = "report.html"
