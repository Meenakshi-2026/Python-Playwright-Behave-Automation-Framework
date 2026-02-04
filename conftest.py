import pytest
from playwright.sync_api import sync_playwright
import sys
import os
import base64
from datetime import datetime

import pytest_html

# Add config to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config

# ===== Fixture 1: Start Playwright =====
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

# ===== Fixture 2: Launch Browser =====
@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        headless=config.HEADLESS_MODE,
        slow_mo=config.SLOW_MOTION
    )
    yield browser
    browser.close()

# ===== Fixture 3: Create Page with Screenshot on Failure =====
@pytest.fixture
def page(browser, request):
    # Create page
    page = browser.new_page()
    
    yield page
    page.close()
    
# ===== Hook: Capture Screenshot on Test Failure =====
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            try:
                screenshot_bytes = page.screenshot()
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode('ascii')

                html = (
                    f'<div><img src="data:image/png;base64,{screenshot_base64}" '
                    f'style="width:600px;height:auto;border:2px solid red;" '
                    f'onclick="window.open(this.src)" /></div>'
                )
                
                # Attach screenshot to pytest-html report
                extra = getattr(rep, 'extras', [])
                extra.append(pytest_html.extras.html(html))
                rep.extras = extra
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
