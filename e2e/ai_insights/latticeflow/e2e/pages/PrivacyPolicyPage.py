from playwright.sync_api import Page
from utils import helpers


class PrivacyPolicyPage:
    def __init__(self, page: Page) -> None:
        self._page = page

        # Others TC-004
        self.allheader = self._page.locator("//h2[@style='margin-top:3.75rem']")

        
    def privacyPolicy_headers_with_scrolling(self):
        header_count = self.allheader.count()

    