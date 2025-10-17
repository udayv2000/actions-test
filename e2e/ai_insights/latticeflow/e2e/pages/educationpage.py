from playwright.sync_api import Page

class educationpage:
   def __init__(self, page: Page) -> None:
        self._page = page

        self.cards = self._page.locator("//div[@class='MuiCardContent-root css-15q2cw4']//h4[@class='css-pl4o4b']")
        self.back_btn = self._page.locator("//button[contains(@class, 'MuiButtonBase-root') and .//label[text()='Back']]")
        self.search_field = self._page.locator("//input[@class='MuiInputBase-input MuiOutlinedInput-input css-1pk1fka']")

        # Site Verification TC-001
        self.ComplAIcard = self._page.locator("//h4[text()='Compl AI']")
        self.AIinsights_footer = self._page.locator("//div[@class='flex-container']")

   def verify_cards_are_displayed(self) -> None:
        # Wait for the first card to be visible before proceeding
        self.cards.first.wait_for(state="visible", timeout=10000)

        count = self.cards.count()
        print(f"Found {count} cards.")

        if count == 0:
            raise AssertionError("❌ No cards found! Possible UI change or locator issue.")

        for i in range(count):
            card = self.cards.nth(i)

            # Scroll into view to handle cards that are off-screen or lazy-loaded
            card.scroll_into_view_if_needed()

            # Wait until card is visible and text is populated
            card.wait_for(state="visible", timeout=5000)

            # Small buffer for dynamic text loading
            self._page.wait_for_timeout(200)

            card_text = card.inner_text().strip()
            print(f"➡️ Card #{i + 1}: {card_text}")

   def verify_cards_open_correct_page(self) -> None:
    self.cards.first.wait_for(state="visible", timeout=10000)
    count = self.cards.count()
    print(f"Found {count} cards.")

    if count == 0:
        raise AssertionError("❌ No cards found!")

    failures = []

    for i in range(count):
        card = self.cards.nth(i)
        card.scroll_into_view_if_needed()
        card.wait_for(state="visible", timeout=5000)
        self._page.wait_for_timeout(200)

        card_text = card.inner_text().strip()
        print(f"➡️ Checking Card #{i+1}: {card_text}")

        card.click()

        # Wait for the title to update to include the card text
        try:
            self._page.wait_for_function(
                """(expected) => document.title.toLowerCase().includes(expected.toLowerCase())""",
                arg=card_text,
                timeout=5000
            )
        except Exception:
            pass  # Let the check fail below if the title never matched

        page_title_text = self._page.title().strip()
        print(f"   Expected to find in title: {card_text}")
        print(f"   Actual page title: {page_title_text}")

        if card_text.lower().strip() not in page_title_text.lower().strip():
            msg = f"❌ Card '{card_text}' not found in page title '{page_title_text}'"
            print(msg)
            failures.append(msg)
        else:
            print(f"✅ Card text found in page title: {page_title_text}")

        # Back navigation
        self.back_btn.scroll_into_view_if_needed()
        self.back_btn.wait_for(state="visible", timeout=3000)
        self.back_btn.click()
        self.cards.first.wait_for(state="visible", timeout=5000)

    if failures:
        failure_report = "\n".join(failures)
        raise AssertionError(f"Some cards failed:\n{failure_report}")

        

   def verify_education_report_search_field(self, search_text: str) -> str:
        self.search_field.fill(search_text)
        card_text = self.cards.inner_text().strip()
        return card_text  

   # Site Verification TC-001
   def verify_Public_Education_Article_Without_Login(self):
       self.ComplAIcard.click()    
       self.AIinsights_footer.scroll_into_view_if_needed()