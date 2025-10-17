from playwright.sync_api import Page

class Leaderboardpage:
    def __init__(self, page: Page) -> None:
        self._page = page  

        self.iframe = page.frame_locator("iframe[sandbox='allow-same-origin allow-scripts allow-presentation allow-downloads allow-forms allow-popups']")

        self.filterButton = self.iframe.locator("span[aria-label='filter']")

        

    def verify_default_filters_applied(self):  
        self.filterButton.click()
