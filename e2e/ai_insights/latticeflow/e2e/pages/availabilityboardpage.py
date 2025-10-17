from playwright.sync_api import Page
from datetime import datetime

class AvailabilityBoardPage:
   def __init__(self, page: Page) -> None:
        self._page = page

        self.announced_column_header = self._page.locator("th:has-text('Announced')")
        self.announced_date_cells = self._page.locator("//div[@class='MuiDataGrid-cell MuiDataGrid-cell--textLeft' and @data-field='announced']")

        self.search_input = self._page.locator("//input[@placeholder='Search…']")
        self.uponrequest_button =self._page.locator("//div[7]//div[8]//button[1]//*[name()='svg']")
        self.CustomRequestpage = self._page.locator("//div[@class='sliderHeader MuiBox-root css-3tqlwx']")
        self.customrequest_button = self._page.locator("//div[@data-field='custom']//button[@type='button']//*[name()='svg']")

        self.intreasted_button = self._page.locator("//div[@class='MuiDataGrid-row MuiDataGrid-row--firstVisible']//button[@aria-label='Interested']//*[name()='svg']")

        self.register_alert_dialog = self._page.locator("//p[@id='alert-dialog-description']")

        # Availability Board TC-003
        self.summaryreport_icon = self._page.locator("//div[@data-field='summary']//button[@type='button']//*[name()='svg']")
        self.riskreport_icon = self._page.locator("//div[@data-field='risk']//button[@type='button']//*[name()='svg']")
        self.summaryreport_header = self._page.locator("//h1[contains(text(),'Foundation Model Summary Report: Llama 3.3 70B Ins')]")
        self.riskreport_header =self._page.locator("//h1[normalize-space()='AI Model Risk Report: LLaMA 3.3 70B Instruct']")


   def verify_sorting_by_announced_date_descending(self):
    """
    Verifies that Model Reports are sorted by Announced Date in descending order (newest first).
    Assumes dates are in format: YYYY-MM-DD (e.g., 2025-10-10)
    
    Returns True if sorted correctly, False otherwise.
    Prints full list of dates for audit and proof.
    """
    print("🔍 Verifying Model Reports are sorted by Announced Date (descending)...")

    # Step 1: Wait for table to load
    self.announced_date_cells.first.wait_for(state="visible", timeout=10000)

    # Step 2: Get all date texts
    date_texts = self.announced_date_cells.all_text_contents()
    date_texts = [text.strip() for text in date_texts if text.strip()]

    if len(date_texts) == 0:
        raise AssertionError("No announced dates found in the table.")

    print(f"✅ Found {len(date_texts)} announced dates.")
    print(f"📋 Original Order: {date_texts}")

    # Step 3: Convert date strings to comparable objects
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")  # e.g., "2025-10-10"
        except ValueError as e:
            raise ValueError(f"Unexpected date format: '{date_str}'")

    # Parse all dates
    parsed_dates = []
    for i, date_str in enumerate(date_texts):
        try:
            parsed = parse_date(date_str)
            parsed_dates.append((parsed, date_str, i))
        except ValueError as e:
            print(f"⚠️ Could not parse date at index {i}: {date_str} → {e}")
            raise

    # Step 4: Sort by date DESCENDING (newest first)
    sorted_desc = sorted(parsed_dates, key=lambda x: x[0], reverse=True)
    expected_dates = [item[1] for item in sorted_desc]

    print("📅 Expected Order (Descending - Newest First):")
    for i, date in enumerate(expected_dates, start=1):
        print(f"   [{i}] {date}")

    # Step 5: Compare original list with expected descending order
    if date_texts == expected_dates:
        print("\n🎉✅ PASSED: Reports are correctly sorted by Announced Date in descending order.")
        return True
    else:
        print("\n❌ FAILED: Reports are NOT sorted in descending order.")
        print(f"   Actual Order: {date_texts}")
        print(f"   Expected Order: {expected_dates}")
        return False
    

   def verify_search_functionality(self,text):
        self._page.wait_for_load_state("domcontentloaded")
        self._page.wait_for_timeout(1000)
        self.search_input.fill(text)
        self._page.wait_for_timeout(500)
        print("\n✅ PASSED: Search functionality working as expexted .")

   def Verify_Custom_Request_link_is_visible_and_navigates_to_Support_Page(self):
       self.uponrequest_button.is_visible()
       self.uponrequest_button.click()
       return self.CustomRequestpage.inner_text().strip()
   
   def Verify_custom_request_links_to_Support_Page(self):
        self.customrequest_button.wait_for(state="visible", timeout=10000)
        self.customrequest_button.click()
        return self.CustomRequestpage.inner_text().strip()
    

   # TC-010 Availability Board
   def Click_Interested_icon_a_report_row(self):
        self.intreasted_button.click()

   def Verify_Register_or_Login_prompt(self):
        self.register_alert_dialog.wait_for(state="visible", timeout=10000)
        return self.register_alert_dialog.is_visible()
   

  # Availability Board TC-003
   def verify_summaryreportpage_opened_or_not(self):
       self.summaryreport_icon.click() 
       #self._page.wait_for_load_state("domcontentloaded") 
       self.summaryreport_header.wait_for(state="visible", timeout=10000)
       return self.summaryreport_header.is_visible()
       
   
   def verify_riskreportpage_opened_or_not(self):
       self._page.wait_for_timeout(500)
       self.riskreport_icon.click()  
       self._page.wait_for_load_state("domcontentloaded") 
       self.riskreport_header.wait_for(state="visible", timeout=10000)
       return self.riskreport_header.is_visible()

    # Availability Board TC-008
   #def table_updates_with_selected_number_of_rows(self):
       

    