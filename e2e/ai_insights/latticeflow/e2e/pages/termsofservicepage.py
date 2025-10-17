from playwright.sync_api import Page
from utils import helpers

class TermsofServicePage:
    def __init__(self, page: Page) -> None:
        self._page = page

        self.termsofservice_header = self._page.locator("//h1[@class='display-3 fw-bold mb-3']")
        self.notices_header = self._page.locator("//h2[contains(text(), 'Notices')]")
        self.communication_mail = self._page.locator("//a[contains(text(),'contact@latticeflow.ai')]")
        self.securityIssuesReporting_mail = self._page.locator("//a[contains(text(),'security@latticeflow.ai')]")


    def validate_communication_mails(self):
        self.notices_header.scroll_into_view_if_needed()
        return self.communication_mail.is_visible()
    
    def validate_securityIssuesReporting_mail(self):
        return self.securityIssuesReporting_mail.is_visible()






