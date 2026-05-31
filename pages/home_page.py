from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def get_page_title(self) -> str:
        """Returns the actual document title from the browser context."""
        return self.page.title()