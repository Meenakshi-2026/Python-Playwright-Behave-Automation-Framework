# Playwright Python Automation Framework

![Playwright Tests](https://github.com/Meenakshi-2026/Playwright-Python-Automation-Framework/actions/workflows/playwright-tests.yml/badge.svg)

A simple and easy-to-understand automation framework for testing the Saucedemo website using the Page Object Model (POM) design pattern.

## Project Structure

```
Playwright-Python-Automation-Framework/
├── .github/workflows/         # GitHub Actions workflows
│   └── playwright-tests.yml   # Automated test execution workflow
├── config.py                  # Configuration file with app URL, credentials, and browser settings
├── requirements.txt           # Python dependencies
├── behave.ini                 # Behave configuration
├── pages/                     # Page Object Models
│   ├── __init__.py
│   ├── base_page.py          # Base page class with common methods
│   ├── login_page.py         # Login page object
│   └── inventory_page.py     # Inventory page object
├── tests/                     # Pytest Test cases
│   ├── __init__.py
│   └── test_saucedemo.py     # Pytest test cases
├── features/                  # Behave/Gherkin Feature files
│   ├── environment.py        # Behave hooks
│   ├── saucedemo_login.feature
│   └── steps/
│       └── login_steps.py    # Step definitions
└── README.md                  # This file
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Install Required Packages

```bash
pip install -r requirements.txt
```

Or install individual packages:

```bash
pip install playwright pytest pytest-html behave behave-html-formatter
```

### Step 2: Install Browser Binaries

```bash
playwright install
```

This command installs the required browser binaries (Chromium, Firefox, WebKit).

## Configuration

Edit the `config.py` file to customize your test environment:

```python
# Application URL
APP_URL = "https://www.saucedemo.com/"

# Browser Configuration
BROWSER_TYPE = "chromium"     # chromium, firefox, webkit
HEADLESS_MODE = False         # Set to True for headless mode
SLOW_MOTION = 1000           # Milliseconds to slow down execution
TIMEOUT = 30000              # Timeout in milliseconds

# Credentials
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

```

## Understanding the Framework

### Page Object Model (POM)

The Page Object Model is a design pattern where each web page is represented as a class:

1. **BasePage** (`pages/base_page.py`): Contains common methods used across all pages
   - `navigate_to_url()` - Navigate to a URL
   - `click()` - Click an element
   - `fill()` - Fill text input
   - `get_text()` - Get element text
   - `take_screenshot()` - Capture screenshots
   - `is_element_visible()` - Check if element exists

2. **LoginPage** (`pages/login_page.py`): Represents the login page
   - Contains selectors for username, password, and login button
   - `login()` - Perform login with credentials
   - `get_error_message()` - Get error message text
   - `is_error_message_displayed()` - Check for error messages

3. **InventoryPage** (`pages/inventory_page.py`): Represents the products inventory page
   - `is_inventory_page_loaded()` - Check if page loaded
   - `get_page_title()` - Get page title
   - `add_item_to_cart()` - Add product to cart
   - `logout()` - Logout from application

### Test Cases

The `tests/test_saucedemo.py` file contains three test cases:

1. **test_successful_login()** - Tests login with valid credentials
2. **test_login_with_invalid_credentials()** - Tests login error handling
3. **test_add_item_to_cart()** - Tests adding items to cart

## Running the Tests

```bash
pytest tests/test_saucedemo.py --html=report.html --self-contained-html
```

## Running BDD Tests (Behave)

To run the Behavior-Driven Development (BDD) tests defined in `.feature` files:

```bash
behave
```

### Generating BDD HTML Reports

To run tests and generate a readable HTML report:

```bash
behave -f html -o behave-report.html
```

This will create a `behave-report.html` file in the project root.

## Running on GitHub

This project is configured to automatically run tests on GitHub Actions whenever code is pushed or a pull request is created.

### Automated Execution

The tests run automatically on:
- Push to `main` or `master` branches
- Pull requests to `main` or `master` branches
- Manual trigger via the "Actions" tab

### Manual GitHub Actions Execution

1. Go to the **Actions** tab in your GitHub repository
2. Select the **Playwright Python Tests** workflow
3. Click **Run workflow** button
4. Choose the branch and click **Run workflow**

### Viewing Test Results

After the workflow completes:
1. Go to the **Actions** tab
2. Click on the workflow run
3. Download the **test-report** artifact to view the HTML test report
4. If tests fail, download the **screenshots** artifact to see failure screenshots

### Configuration for CI/CD

The framework automatically runs in headless mode on GitHub Actions. The `config.py` file reads the `HEADLESS_MODE` environment variable, which is set to `true` in the workflow.

## Key Features

**Easy to Understand** - Simple, well-documented code
**Page Object Model** - Maintainable and scalable structure
**Configuration File** - Centralized settings management
**Reusable Methods** - Common functionality in BasePage class
**Automatic Screenshots** - Capture page state at each step
**Clear Test Cases** - Well-structured and commented test methods
**GitHub Actions Integration** - Automated test execution on every push/PR
**CI/CD Ready** - Environment variable support for headless mode

## Troubleshooting

- **Browser not found**: Run `playwright install` to install browser binaries
- **Tests failing**: Check if Saucedemo website is accessible
- **Selectors not working**: Use browser DevTools to inspect elements and update selectors

## Current behavior:
Report location: report.html in the project root (not in reports/ folder)
Screenshots: Embedded as base64 directly inside report.html (no separate files)
The --self-contained-html flag ensures everything is in one file.

## Support

For issues or questions, refer to:
- [Playwright Documentation](https://playwright.dev/python/)