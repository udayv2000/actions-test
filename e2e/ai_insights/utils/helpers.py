"""
helpers.py
If you find yourself writing the same logic more than twice in different places (e.g., generating emails, cleaning prices), 
it's a prime candidate to be refactored into a function in helpers.py. This centralizes the logic, making it easier to maintain and update.

"""
from playwright.sync_api import Page, BrowserContext
from faker import Faker
import uuid
from datetime import datetime

# Initialize Faker once at the module level (better performance)
fake = Faker()


# --- Data Generation Helpers ---
def generate_user_data() -> dict:
    # Generate base names (short, clean)
    first = fake.first_name()[:8]      # e.g., "John"
    last = fake.last_name()[:8]        # e.g., "Smith"

    # Generate a 4-char unique ID (hex, lowercase)
    uid = uuid.uuid4().hex[:4]         # e.g., "a1b2"

    # ✅ Make names unique by appending UID — still readable!
    unique_first = f"{first}_{uid}"
    unique_last = f"{last}_{uid}"

    # Email uses the *clean* base names (no UID) for format
    email = f"{first.lower()}.{last.lower()}+AUTO_{uid}@example.com"

    return {
        "first_name": unique_first,   # e.g., "John_a1b2"
        "last_name": unique_last,     # e.g., "Smith_a1b2"
        "email": email                # e.g., "john.smith+AUTO_a1b2@example.com"
    }

# --- Window Helpers ---
def switch_to_child(page: Page, locator: str) -> Page:
    with page.context.expect_page() as new_page_event:
        locator.click()
    child_page = new_page_event.value
    child_page.wait_for_load_state("domcontentloaded")
    return child_page

def switch_to_parent(child_page: Page, parent_page: Page) -> Page:
    if not child_page.is_closed():
        child_page.close()
    return parent_page

# --- Dropdown Helper ---
def select_option_from_dropdown(self, dropdown_locator, option_text):
        """
        Opens the Vendor dropdown, scrolls to the specified vendor, and clicks it.
        Works for scrollable, lazy-loaded MUI menus.
        Automatically normalizes whitespace to match UI display format.
        Returns True if successfully clicked, False otherwise.
        """

        # Step 0: Ensure page is ready
        # self.add_button.click()
        # self._page.wait_for_load_state("domcontentloaded")

        # Step 1: Click the dropdown to open it
        dropdown_locator.click()

        # Step 2: Wait for the menu list to appear
        dropdown_list = self._page.locator("ul[role='listbox']")
        dropdown_list.wait_for(state="visible", timeout=5000)

        # Step 3: Find all options
        options = dropdown_list.locator("li[role='option']")

        # ✅ Normalize input: remove ALL spaces and convert to lowercase
        normalized_search = option_text.replace(" ", "").lower()

        # Step 4: Try to find and click the vendor directly (if visible)
        for i in range(options.count()):
            option = options.nth(i)
            text = option.inner_text().strip()
        
            # ✅ Normalize dropdown text: remove spaces + lowercase
            normalized_text = text.replace(" ", "").lower()

            if normalized_text == normalized_search:
                print(f"✅ Found Dropdown '{option_text}' (normalized: '{normalized_text}') — clicking immediately.")
                option.click()
                self._page.wait_for_timeout(500)  # Let UI update
                return True

        # Step 5: If not found, scroll down incrementally until found or max attempts
        print(f"🔍 Dropdown '{option_text}' not visible. Scrolling down to locate...")
    
        max_attempts = 15
        scroll_attempts = 0
        last_option_count = 0

        while scroll_attempts < max_attempts:
            # Scroll container down by 200px
            dropdown_list.evaluate("ul => ul.scrollTop += 200")
        
            # Wait for new content to load (lazy loading)
            self._page.wait_for_timeout(800)

            # Re-check total count
            current_option_count = options.count()
            if current_option_count == last_option_count:
                # No new items loaded — likely reached end of list
                break
            last_option_count = current_option_count

            # Search again after scroll
            for i in range(current_option_count):
                option = options.nth(i)
                text = option.inner_text().strip()
                normalized_text = text.replace(" ", "").lower()

                if normalized_text == normalized_search:
                    print(f"✅ Found Dropdown '{option_text}' after scrolling (normalized: '{normalized_text}') — clicking now.")
                    option.click()
                    self._page.wait_for_timeout(500)  # Allow UI to update
                    return True

            scroll_attempts += 1

        # Step 6: Not found after all attempts
        print(f"❌ Dropdown '{option_text}' not found in dropdown after scrolling.")
        return False

# --- Element Helpers ---
def get_text(locator: str) -> str:
    return locator.inner_text().strip()

def get_current_url(self):
        return self._page.url


