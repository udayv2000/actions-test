from playwright.sync_api import Page


class LandingPage:
    def __init__(self, page: Page) -> None:
        self._page = page
        self._cards = self._page.locator("xpath=//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-72dktb']")
        

    def click_all_cards(self) -> None:
        #self._page.pause()
        count = self._cards.count()
        print(f"Found {count} cards.")

        if count == 0:
            raise AssertionError("❌ No cards found! Possible UI change or locator issue.")

        
        for i in range(count):
            print(f"\n➡️ Clicking card #{i + 1}")

            # Re-locate the cards after back navigation
            cards = self._page.locator("//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-72dktb']")
            card = cards.nth(i)

            # Scroll card into view and click
            card.scroll_into_view_if_needed()
            self._page.wait_for_timeout(300)
            card.click()

            # Wait for page content to load
            self._page.wait_for_load_state("networkidle")
            self._page.wait_for_timeout(1000)

            # ✅ Print page title
            page_title = self._page.title()
            print(f"📝 Page title after clicking card #{i + 1}: '{page_title}'")

            # ✅ Scroll to bottom (footer)
            footer = self._page.locator("//div[@class='footer-left footer-logo']")
            footer.scroll_into_view_if_needed()
            self._page.wait_for_timeout(1000)

            # ✅ Scroll back to top (top header element)
            top_element = self._page.locator("//div[@class='MuiStack-root css-149sczi']")
            top_element.scroll_into_view_if_needed()
            self._page.wait_for_timeout(1000)

            # Go back to card list
            self._page.go_back()

            # Wait for cards to appear again
            self._page.wait_for_selector("//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-72dktb']")