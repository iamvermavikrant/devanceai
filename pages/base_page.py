import logging
import os
from playwright.sync_api import Page, TimeoutError

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 7000  # 7-second explicit wait ceiling for element visibility

    def navigate(self, path: str = ""):
        """Navigates safely using the strict system environment configuration."""
        base_url = os.getenv("PLAYWRIGHT_BASE_URL")
        
        # Guardrail: Force execution to stop if environment configuration is broken
        if not base_url:
            error_msg = "Configuration Error: 'PLAYWRIGHT_BASE_URL' is not defined in the environment or .env file."
            logger.critical(error_msg)
            raise RuntimeError(error_msg)

        target_url = f"{base_url}{path}"
        logger.info(f"Navigating to target URL: {target_url}")
        self.page.goto(target_url)

    def click_element(self, selector: str):
        """Waits for visibility and clicks an element. Throws an AssertionError if it fails."""
        try:
            logger.info(f"Attempting to click element: '{selector}'")
            self.page.wait_for_selector(selector, state="visible", timeout=self.timeout)
            self.page.click(selector)
        except TimeoutError as e:
            error_msg = f"Automation Error: Element '{selector}' not interactable or visible within {self.timeout}ms."
            logger.error(error_msg)
            raise AssertionError(error_msg) from e

    def fill_input(self, selector: str, text: str):
        """Waits for visibility, clears, and populates an input field safely."""
        try:
            logger.info(f"Attempting to fill text in selector: '{selector}'")
            self.page.wait_for_selector(selector, state="visible", timeout=self.timeout)
            self.page.fill(selector, text)
        except TimeoutError as e:
            error_msg = f"Automation Error: Input field '{selector}' could not be populated within {self.timeout}ms."
            logger.error(error_msg)
            raise AssertionError(error_msg) from e