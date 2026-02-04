from playwright.sync_api import sync_playwright
import sys
import os
import base64

# Add the project root to sys.path to allow imports from pages and config
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

import config

def before_all(context):
    context.playwright = sync_playwright().start()
    
    launch_args = {
        "headless": config.HEADLESS_MODE,
        "slow_mo": config.SLOW_MOTION
    }
    
    if config.BROWSER_TYPE == 'firefox':
        context.browser = context.playwright.firefox.launch(**launch_args)
    elif config.BROWSER_TYPE == 'webkit':
        context.browser = context.playwright.webkit.launch(**launch_args)
    else:
        context.browser = context.playwright.chromium.launch(**launch_args)

def after_all(context):
    context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    context.page = context.browser.new_page()

def after_step(context, step):
    if step.status == "failed":
        print("Step failed, taking screenshot...")
        screenshot_bytes = context.page.screenshot()
        encoded_screenshot = base64.b64encode(screenshot_bytes).decode("utf-8")
        
        # Workaround for context.embed missing in some behave versions
        embed_found = False
        if hasattr(context, 'embed'):
            context.embed(mime_type="image/png", data=encoded_screenshot, caption="Screenshot")
            embed_found = True
        
        # Fallback: Manually invoke embedding on configured formatters
        if not embed_found and hasattr(context, '_runner') and hasattr(context._runner, 'formatters'):
            for formatter in context._runner.formatters:
                if hasattr(formatter, 'embedding'):
                    formatter.embedding(mime_type="image/png", data=encoded_screenshot, caption="Screenshot")
                    embed_found = True
        
        if not embed_found:
             print("WARNING: Could not embed screenshot. context.embed missing and no suitable formatter found.")


def after_scenario(context, scenario):
    context.page.close()
