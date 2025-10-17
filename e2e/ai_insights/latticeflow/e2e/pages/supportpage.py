from playwright.sync_api import Page, expect
from utils import helpers


class SupportPage:
    def __init__(self, page: Page) -> None:
        self._page = page
        
        self.supportemail_input = self._page.locator("//input[@id='support-email']")
        self.subject_input = self._page.locator("//input[@id='support-email-subject']")
        self.message_input = self._page.locator("//textarea[@id='support-email-message']")
        self.submitRequest_btn = self._page.locator("//button[@id='support-request-btn']")
        self.submit_confirm_popup = self._page.locator("//h2[normalize-space()='Request Submitted!']")



    def Verify_successful_form_submission(self, mail, subject, message): 
        self.supportemail_input.wait_for(state="visible", timeout=10000)
        self.supportemail_input.fill(mail)
        self.subject_input.fill(subject)
        self.message_input.fill(message)
        self.submitRequest_btn.scroll_into_view_if_needed()
        self.submitRequest_btn.click()
        self.submit_confirm_popup.wait_for(state="visible", timeout=3000)
        return self.submit_confirm_popup.is_visible()