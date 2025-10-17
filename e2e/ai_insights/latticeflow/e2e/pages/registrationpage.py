from playwright.sync_api import Page, expect
from utils import helpers

class RegistrationPage:
    def __init__(self, page: Page) -> None:
        self._page = page

        # Registration Page TC-001
        self.signup_btn = self._page.locator("//div[@class='auth mobile-hide']//span[contains(text(),'SIGN UP')]")

        # Registration Page TC-002
        self.first_name_field = page.locator('p:has-text("FIRST NAME*") + div input')
        self.last_name_field = page.locator('p:has-text("LAST NAME*") + div input')
        self.email_field = page.locator('p:has-text("EMAIL*") + div input')
        self.job_title_field = page.locator('p:has-text("JOB TITLE") + div input')
        self.company_name_field = page.locator('p:has-text("COMPANY NAME") + div input')

        # Registration Page TC-003
        self.termsOfService_link = page.locator("//div[@class='tos']//a[contains(text(),'Terms of Service')]")

        # Registration Page TC-004
        self.registration_btn = page.locator("//button[normalize-space()='REGISTER']")

        # Registration Page TC-006
        self.termsOfservice_checkbox = page.locator("(//input[@type='checkbox'])[1]")
        self.marketing_checkbox = page.locator("(//input[@type='checkbox'])[2]")
        self.registration_success_popup = page.locator("//h2[normalize-space()='Registered Successfully']")
        


    # Registration Page TC-001
    def click_on_signup(self): 
        self.signup_btn.click() 
   
    def verify_header_has_registration_option(self):
        self._page.wait_for_load_state("domcontentloaded")
        return self._page.url  
    
    
    # Registration Page TC-002 
    def verify_registrationpage_load_correctly(self):
        self._page.wait_for_load_state("domcontentloaded")
        return self._page.url 
    
    def get_form_field_visibility(self):
        """Returns a dictionary with field name and visibility status."""
        self._page.wait_for_load_state("domcontentloaded")
        self.first_name_field.wait_for(state="visible", timeout=5000)
        return {
            "first_name": self.first_name_field.is_visible(),
            "last_name": self.last_name_field.is_visible(),
            "email": self.email_field.is_visible(),
            "job_title": self.job_title_field.is_visible(),
            "company_name": self.company_name_field.is_visible(),
            
        }
    
    # Registration Page TC-003
    def verify_termsOfservice_links_on_registration_page(self):
        self.termsOfService_link.scroll_into_view_if_needed()
        child = helpers.switch_to_child(self._page, self.termsOfService_link)
        termsOFService_url = child.url
        return termsOFService_url
        #print(f"➡️ Validating URL: Actual='{termsOFService_url}'")


    def user_registration(self, fill_job_title=True, fill_company=True, check_tos=True, check_marketing=False):
        """
        Perform user registration and return success status.
    
        :param fill_job_title: Fill job title field
        :param fill_company: Fill company name field
        :param check_tos: Check Terms of Service checkbox
        :param check_marketing: Check Marketing consent checkbox
        :return: dict - {"success": bool, "user": dict or None}
        """
        try:
            # Step 1: Click Sign Up
            self.signup_btn.click()
            self._page.wait_for_load_state("domcontentloaded")

            # Step 2: Generate test data
            user = helpers.generate_user_data()

            # Step 3: Fill required fields
            self.first_name_field.fill(user["first_name"])
            self.last_name_field.fill(user["last_name"])
            self.email_field.fill(user["email"])

            # Step 4: Fill optional fields
            if fill_job_title:
                self.job_title_field.fill("Software Engineer")

            if fill_company:
                self.company_name_field.fill("Automation Labs")

            # Step 5: Handle checkboxes
            if check_tos:
                self.termsOfservice_checkbox.check()
            else:
                if self.termsOfservice_checkbox.is_checked():
                    self.termsOfservice_checkbox.uncheck()

            if check_marketing:
                self.marketing_checkbox.check()
            else:
                if self.marketing_checkbox.is_checked():
                    self.marketing_checkbox.uncheck()

            # Step 6: Click Register
            self.registration_btn.click()

            # Step 7: Wait for success popup (non-blocking check)
            self.registration_success_popup.wait_for(state="visible", timeout=10000)

             # Step 8: Return result
            return {
                "success": True,
                "user": user,
                "message": "Registration successful"
            }

        except Exception as e:
            print(f"❌ Registration failed: {str(e)}")
            return {
                "success": False,
                "user": None,
                "message": str(e)
            }   
