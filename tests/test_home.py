import logging

logger = logging.getLogger(__name__)

def test_home_page_navigation(home_page):
    """Verifies infrastructure navigation by validating the live page title."""
    logger.info("Executing Enterprise Integration Check: Initializing navigation.")
    
    # 1. Navigate to the base URL
    home_page.navigate()
    
    # 2. Extract the browser's page title
    page_title = home_page.get_page_title()
    logger.info(f"UI Component Validation Success! Extracted Page Title: '{page_title}'")
    
    # 3. Verify that we successfully retrieved a title string
    assert len(page_title) > 0, "Infrastructure Failure: Page title returned an empty string."