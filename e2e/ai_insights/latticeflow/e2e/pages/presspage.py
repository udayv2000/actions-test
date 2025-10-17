from playwright.sync_api import Page

class presspage:
   def __init__(self, page: Page) -> None:
        self._page = page

        self._logout_button = self._page.locator("xpath=//span[normalize-space()='Logout']")

        