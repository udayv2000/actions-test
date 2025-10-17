from playwright.sync_api import expect
from playwright.sync_api import Page
from utils import helpers


class Aboutpage:
    def __init__(self, page: Page) -> None:
        self._page = page

        # TC-002
        self.logo = self._page.locator("div.logo img[alt='logo']")
        self.latticeFlow_tagline = self._page.locator("//p[@class='lead fs-1 text-muted']")
        self.latticeFlow_link = self._page.locator("(//a[@href='https://latticeflow.ai'])[1]")

        # TC-003
        self.footer_privacy_policy = self._page.locator("//a[normalize-space()='Privacy Policy']")
        



    # TC-002
    def verify_logo(self) -> bool:
        """Waits for logo to be visible and returns True/False"""
        try:
            expect(self.logo).to_be_visible(timeout=5000)
            return True
        except Exception:
            return False    

    def get_latticeFlow_tagline_text(self):
        return helpers.get_text(self.latticeFlow_tagline)   

    def validate_link_functionality(self):
       latticeFlow_link = self.latticeFlow_link.get_attribute("href")
       self.latticeFlow_link.click()
       latticeFlow_main_url = self._page.url
       
       return latticeFlow_link, latticeFlow_main_url

    
    
    # TC-003
    def verify_privacy_policy(self):
        child = helpers.switch_to_child(self._page, self.footer_privacy_policy)
        privacy_policy_url=child.url
        helpers.switch_to_parent(child, self._page)
        return privacy_policy_url