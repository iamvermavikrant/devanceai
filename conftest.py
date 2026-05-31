import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

# Force load the local environment configurations before any test suites execute
load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def configure_environment():
    """Validates core configuration primitives before spinning up automation hardware."""
    base_url = os.getenv("PLAYWRIGHT_BASE_URL")
    if not base_url:
        raise RuntimeError("Infrastructure Failure: 'PLAYWRIGHT_BASE_URL' variable missing from environment configuration.")

@pytest.fixture(scope="session")
def browser_context():
    """Spins up a single isolated browser engine session for the test run."""
    with sync_playwright() as p:
        # Check if we should run headless (no UI) or headed (visible UI)
        is_headless = os.getenv("HEADLESS", "False").lower() == "true"
        
        browser = p.chromium.launch(headless=is_headless)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    """Provides a completely clean, isolated tab (page) for every single test case."""
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def home_page(page):
    """Dependency Injection: Automatically initializes and provides the HomePage Object."""
    return HomePage(page)