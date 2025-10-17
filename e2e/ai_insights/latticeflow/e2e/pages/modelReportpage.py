from playwright.sync_api import Page

class ModelReportpage:
    def __init__(self, page: Page) -> None:
        self._page = page

        self.cards = self._page.locator("//h4[@class='css-pl4o4b']")
        self.firstcard = self._page.locator("(//h4[@class='css-pl4o4b'])[1]")
        self.search_field = self._page.locator("//input[@class='MuiInputBase-input MuiOutlinedInput-input css-1pk1fka']")
        self.loginToviewTheFullReport_button = self._page.locator("//button[normalize-space()='LOGIN TO VIEW THE FULL REPORT']")
        self.firstReportcard = self._page.locator("(//h4[@class='css-pl4o4b'])[1]")
        self.mailfield = self._page.locator("//input[@placeholder='Enter Email']")
        self.passwordfield = self._page.locator("//input[@id='password']")
        self.loginButton = self._page.locator("//button[contains(@class, 'MuiButton-containedPrimary')]")
        self.account_popup_manu = self._page.locator("//div[@class='auth mobile-hide']//button[2]")
        self.logoutButton = self._page.locator("//span[normalize-space()='Logout']")

        self.googleButton = self._page.locator("//img[@alt='google']")
        self.googleEmailField = self._page.locator("//input[@type='email']")
        self.googleNextButton = self._page.locator("//span[normalize-space()='Next']")
        self.googlepassword = self._page.locator("//input[@type='password']")

        # Profile TC-020
        self.add_button = self._page.locator("//button[normalize-space()='Add']//*[name()='svg']")
        self.selectVendor = self._page.locator("//div[text()='Select Vendor']")
        self.selectModel = self._page.locator("//div[text()='Select Model']")

        # Profile TC-021
        self.announcedDate_input = self._page.locator("//input[@placeholder='MM/DD/YYYY']")
        self.selectEvaluated = self._page.locator("//div[text()='Select Evaluated']")
        self.select_Planned = self._page.locator("//li[@data-value='planned']")
        self.selectRiskProfile = self._page.locator("//div[text()='Select Risk Profile']")
        self.selectCustom = self._page.locator("//div[text()='Select Custom']")
        self.selectSummary = self._page.locator("//div[text()='Select Summary']")
        self.benchmarkNotAvailable_checkBox = self._page.locator("//input[@type='checkbox']")
        self.uploadButton = self._page.locator("(//button[contains(@class, 'MuiButton-containedPrimary')])[1]")
        self.model_added_success_popup = self._page.locator("//h2[normalize-space()='Model Availability Added Successfully']")
        self.model_edited_success_popup = self._page.locator("//h2[normalize-space()='Model Availability Updated Successfully']")

        # Site Verification TC-003
        self.header_one = self._page.locator("//h2[normalize-space()='Executive Summary']")
        self.header_two = self._page.locator("//h2[normalize-space()='Model Evaluation Details']")
        self.header_three = self._page.locator("//h2[normalize-space()='Model Performance Comparison']")
        self.header_four = self._page.locator("//h2[normalize-space()='Cybersecurity Guardrails']")
        self.header_five = self._page.locator("//h2[contains(text(),'Example Use Case 1: Cybersecurity Ticket Triage an')]")
        self.header_six = self._page.locator("//h2[contains(text(),'Example Use Case 2: Developer Productivity and Cod')]")
        self.header_seven = self._page.locator("//h2[normalize-space()='Conclusion & Recommendations']")
        self.header_eight = self._page.locator("//h2[normalize-space()='Contact and Further Resources']")

        # Content Access TC-002
        self.backButton = self._page.locator("//label[text()='Back']")
        self.firstcards = self._page.locator("(//h4[@class='css-pl4o4b'])[1]")
        self.LoginpromptButton = self._page.locator("//button[contains(@class, 'MuiButton-fullWidth css-1jphbt6')]")

        # TC-005
        self.report_card = self._page.locator("//div[@class='MuiCardContent-root css-15q2cw4']")
        

    def verify_all_model_cards_are_displayed(self) -> None:
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

        if count == 0:
            raise AssertionError("❌ No cards found!")

        for i in range(count):
            card = self.cards.nth(i)
            card.scroll_into_view_if_needed()
            card.wait_for(state="visible", timeout=5000)
            self._page.wait_for_timeout(200)
            card_text = card.inner_text().strip()
            print(f"➡️ Checking Card #{i+1}: {card_text}")

            card.click()
            self._page.wait_for_load_state("domcontentloaded")

            page_title_text = self._page.title().strip()

        if card_text != page_title_text:
            raise AssertionError(
                f"❌ Mismatch for card '{card_text}'. Page title: '{page_title_text}'"
            )
        else:
            print(f"✅ Card text matches page title: {page_title_text}")

        self.backButton.scroll_into_view_if_needed()
        #self._page.go_back()
        self._page.wait_for_timeout(1500)  # wait for the intermediate page
        #self._page.go_back()
        self.cards.first.wait_for(state="visible", timeout=5000)



    def verify_model_report_search_field(self, search_text: str) -> str:
        self.search_field.fill(search_text)
        card_text = self.cards.inner_text().strip()
        return card_text    
    
    def verify_modelReportpage(self) -> str:
        self._page.wait_for_load_state("domcontentloaded")
        page_title = self._page.title()
        return page_title
    

    # Login TC-010
    def verify_signin_or_signup_from_the_modelReport(self, mail, password):
        #self._page.pause()
        self.firstReportcard.click()
        self._page.wait_for_load_state("domcontentloaded")
        self.loginToviewTheFullReport_button.scroll_into_view_if_needed()
        self.loginToviewTheFullReport_button.click()
        self.mailfield.fill(mail)
        self.passwordfield.fill(password)
        self.loginButton.click()
        self._page.wait_for_load_state("domcontentloaded")
        self.account_popup_manu.click()
        #self._page.wait_for_load_state("domcontentloaded")
        self.logoutButton.wait_for(state="visible", timeout=10000)
        return self.logoutButton.is_visible()
    

    def verify_Gmail_login_to_view_report_from_Model_report(self, mail, password):
        self.firstReportcard.click()
        self._page.wait_for_load_state("domcontentloaded")
        self.loginToviewTheFullReport_button.scroll_into_view_if_needed()
        self.loginToviewTheFullReport_button.click()
        self.googleButton.click()
        self.googleEmailField.fill(mail)
        self.googleNextButton.click()
        self.googlepassword.fill(password)
        self.googleNextButton.click()
        self._page.wait_for_load_state("domcontentloaded")
        self.account_popup_manu.click()
        #self._page.wait_for_load_state("domcontentloaded")
        self.logoutButton.wait_for(state="visible", timeout=10000)
        return self.logoutButton.is_visible()
    

    # Profile TC-020
    def click_add_model_report_button(self):
        self.add_button.click()
        self._page.wait_for_load_state("domcontentloaded")    

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

    # Profile TC-021

    def add_new_model(self, vendor_name, model_name):
        self.add_button.click()
        self._page.wait_for_load_state("domcontentloaded")

        success_vendor = self.select_option_from_dropdown(self.selectVendor, vendor_name)
        if not success_vendor:
            raise Exception(f"Failed to select vendor '{vendor_name}'")
        
        success_model = self.select_option_from_dropdown(self.selectModel, model_name)
        if not success_model:
            raise Exception(f"Failed to select model '{model_name}'")
        
        self.announcedDate_input.fill("10/10/2025")
        self.selectEvaluated.click()
        self.select_Planned.click()
        self.selectSummary.click()
        self.select_Planned.click()
        self.selectRiskProfile.click()
        self.select_Planned.click()
        self.selectCustom.click()
        self.select_Planned.click()
        self.benchmarkNotAvailable_checkBox.check()
        self.uploadButton.click()
        self.model_added_success_popup.wait_for(state="visible", timeout=10000)
        #self._page.wait_for_load_state("domcontentloaded")
        return self.model_added_success_popup.is_visible()
    
    # Profile TC-025
    def verify_newly_added_model_appears_availability_board(self, org_name):
        #self._page.reload()
        self._page.reload(wait_until="networkidle", timeout=20000)
        self._page.wait_for_load_state("networkidle")
        dropdown = self._page.locator("select")
        dropdown.wait_for(state="visible", timeout=10000)
        dropdown.scroll_into_view_if_needed()
        dropdown.select_option(value="All")

        # Optional: Verify selection
        selected_value = dropdown.evaluate("el => el.value")
        #print(f"✅ Successfully selected: {selected_value}")

        # Step 2: Wait for the org name to appear
        org_cell = self._page.locator(f"//div[text()='{org_name}']")
        #org_cell.wait_for(state="visible", timeout=10000)

        # Step 3: Scroll into view
        org_cell.scroll_into_view_if_needed()

        # Step 4: Get parent row and find edit button
        row = org_cell.locator("..")
        edit_button = row.locator("button[aria-label='Edit']")

            # Step 5: Validate and click
        if edit_button.count() == 0:
            raise Exception(f"Edit button not found for {org_name}")

        edit_button.click()

        # Optional: Wait for modal
        self._page.wait_for_timeout(1000)
        self.announcedDate_input.scroll_into_view_if_needed()
        self.announcedDate_input.fill("03/10/2025")
        self.uploadButton.click()

        self.model_edited_success_popup.wait_for(state="visible", timeout=10000)
        return self.model_edited_success_popup.is_visible()
    
    def verify_Row_shows_NA_icon_in_evaluated_column(self, model_name):
        """
        Waits for model evaluation to complete, then verifies the 'Benchmark not available' icon appears.
        Uses polling logic to avoid flakiness due to async backend processing.
        Returns True if icon found, False otherwise.
        """
        # Step 1: Refresh page to ensure latest state
        self._page.reload(wait_until="networkidle", timeout=20000)
        self._page.wait_for_load_state("networkidle")

        # Step 2: Show all rows
        dropdown = self._page.locator("select")
        dropdown.wait_for(state="visible", timeout=10000)
        dropdown.select_option(value="All")

        # Step 3: Locate model row
        model_cell = self._page.locator(f"//div[text()='{model_name}']")
        model_cell.wait_for(state="visible", timeout=10000)
        model_cell.scroll_into_view_if_needed()

        row = model_cell.locator("..")
        evaluated_cell = row.locator("div[data-field='evaluated']")

        print(f"🔍 Waiting for evaluation to complete for '{model_name}'...")

        # Step 4: Poll until evaluation finishes (max 60 seconds)
        max_attempts = 60  # 60 x 1s = 60s total
        for attempt in range(max_attempts):
            # Get current text/content of the evaluated cell
            cell_text = evaluated_cell.inner_text().strip()
            cell_has_spinner = evaluated_cell.locator("svg[role='progressbar']").count() > 0

            print(f"   [Attempt {attempt+1}] Evaluated cell content: '{cell_text}' | Has spinner: {cell_has_spinner}")

            # ✅ If we see "Benchmark not available" icon → success!
            na_icon = evaluated_cell.locator("button[aria-label='Benchmark not available']")
            if na_icon.is_visible():
                print(f"✅ Found 'Benchmark not available' icon after {attempt+1} attempts.")
                return True

            # ✅ If cell shows "Not Available" as text (fallback)
            if cell_text == "Not Available":
                print(f"✅ Found 'Not Available' text in evaluated column after {attempt+1} attempts.")
                return True

            # ✅ If spinner gone and cell is empty or has no text → likely ready for icon
            if not cell_has_spinner and (not cell_text or cell_text == "-"):
                # Wait a bit more — sometimes icon loads after text clears
                self._page.wait_for_timeout(1000)
                continue

            # Wait 1 second between checks
            self._page.wait_for_timeout(1000)

        # Step 5: Timeout reached — icon never appeared
        print(f"❌ 'Benchmark not available' icon did not appear within 60 seconds.")
        return False
    
    # Site Verification TC-003
    def selected_article_loads_with_content(self):
        self.firstcard.click()
        self.header_eight.scroll_into_view_if_needed() 
        return self.header_eight.is_visible()
    

    # Content Access TC-002

    def verify_Login_prompt_shown_Model_Report(self):
        self.firstcards.click()
        self.LoginpromptButton.scroll_into_view_if_needed()
        self.LoginpromptButton.wait_for(state="visible", timeout=10000)
        return self.LoginpromptButton.is_visible()
    

    # Model Report TC-005
    def search_report(self, search_text: str) -> str:
        self.search_field.fill(search_text)


    def open_report(self):
        self.report_card.click()    

    def scroll_to_Login_prompt(self):
        self.LoginpromptButton.scroll_into_view_if_needed()
        self.LoginpromptButton.wait_for(state="visible", timeout=10000)
        return self.LoginpromptButton.is_visible()
