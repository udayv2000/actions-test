from playwright.sync_api import expect
from playwright.sync_api import Page
from utils import helpers



class LoginPage:
    def __init__(self, page: Page) -> None:
        self._page = page
        self._email_input = self._page.locator("#username")
        self._password_input = self._page.locator("#password")
        self._login_button = self._page.locator(".login-btn")

        self.forgot_password_link = self._page.locator("//div[@class='forgot-password']")
        self.signup_link = self._page.locator("//button[normalize-space()='Sign up']")

        # Login TC-014
        self.googleLoginButton = self._page.locator("//img[@alt='google']")
        self.microsoftLoginButton = self._page.locator("//img[@alt='microsoft']")
        self.linkedinLoginButton = self._page.locator("//img[@alt='linkedIn']")

        # Login TC-015    
        self.googleEmailField = self._page.locator("//input[@type='email']")
        self.googleNextButton = self._page.locator("//span[normalize-space()='Next']")
        self.googlepassword = self._page.locator("//input[@type='password']")

        # Login TC-016
        self.linkedinEmailField = self._page.locator("//input[@id='username']")
        self.linkedinpasswordField = self._page.locator("//input[@id='password']")
        self.linkedinSignin_button = self._page.locator("//button[normalize-space()='Sign in']")
        self.keepmeloggedin_checkbox = self._page.locator("//input[@type='checkbox']")

        # Login Tc-005
        self.account_popup_manu = self._page.locator("//div[@class='auth mobile-hide']//button[2]")
        self.logoutButton = self._page.locator("//span[normalize-space()='Logout']")
        self.headerLogin_button = self._page.locator("//div[@class='auth mobile-hide']//span[contains(text(),'LOG IN')]")

    def login_user(self, *, email: str, password: str) -> None:
        
        #self._page.pause()
        self._email_input.fill(email)
        self._password_input.fill(password)
        self._page.wait_for_load_state("networkidle")
        self._login_button.click(timeout=10000)
        self._page.wait_for_load_state("networkidle")
        #self._page.wait_for_load_state("networkidle")

    def click_login_btn(self):
        #self._page.pause()
        self.headerLogin_button.click()    

     
    def is_login_page_loaded(self) -> bool:
        """Verify login page loads correctly"""
        return (
            self._email_input.is_visible() and
            self._password_input.is_visible() and
            self._login_button.is_visible()
        ) 
    
    def get_current_url(self):
        return self._page.url
    
    def get_page_tittle(self) -> str:
        self._page.wait_for_load_state("domcontentloaded")
        page_title = self._page.title()
        return page_title   
    

    def get_form_field_visibility(self):
        """Returns a dictionary with field name and visibility status."""
        self._page.wait_for_load_state("domcontentloaded")
        return {
            "email": self._email_input.is_visible(),
            "password": self._password_input.is_visible(),
            "loginbtn": self._login_button.is_visible(),
            
        }  
    
    def click_signup_link(self):
        self.signup_link.scroll_into_view_if_needed()
        self.signup_link.click()  
        
    def click_forgot_password_link(self):
        self.forgot_password_link.click() 


    def verify_signup_link(self):
        self.signup_link.scroll_into_view_if_needed()
        self.signup_link.wait_for(state="visible", timeout=5000)

        self.signup_link.click()   
        #self._page.wait_for_load_state("domcontentloaded")
        signup_page_url = self._page.url
        return signup_page_url   

    def verify_forgot_password_link(self): 
        self.forgot_password_link.click() 
        self._page.wait_for_load_state("domcontentloaded")
        forgot_password_page_url = self._page.url
        return forgot_password_page_url 
    
    def verify_google_signin(self):
        self.googleLoginButton.scroll_into_view_if_needed()
        self.signup_link.wait_for(state="visible", timeout=5000)
        self.googleLoginButton.click()

    # Login TC-014
    def is_social_login_buttons_visible(self):
        self._page.wait_for_load_state("domcontentloaded")
        return {
            "google": self.googleLoginButton.is_visible(),
            "microsoft": self.microsoftLoginButton.is_visible(),
            "linkedin": self.linkedinLoginButton.is_visible(),
            
        }  

    # Login TC-015 
    def verify_login_with_gmail(self, mail, pwd, homePageURL):
        self.googleLoginButton.scroll_into_view_if_needed()
        self.googleLoginButton.click()
        self.googleEmailField.fill(mail)
        self.googleNextButton.click()
        self.googlepassword.fill(pwd)
        self.googleNextButton.click()
        self._page.wait_for_url(homePageURL.strip(), timeout=15000)
        latticeflow_url = self._page.url
        return latticeflow_url 
    
    # Login TC-016
    def verify_login_with_linkedin(self, mail, pwd, homePageURL):
        self.linkedinLoginButton.scroll_into_view_if_needed()
        self.linkedinLoginButton.click()
        self.linkedinEmailField.fill(mail)
        self.linkedinpasswordField.fill(pwd)
        #self.keepmeloggedin_checkbox.uncheck()
        self.linkedinSignin_button.click()
        self._page.wait_for_url(homePageURL.strip(), timeout=15000)
        latticeflow_url = self._page.url
        return latticeflow_url
    
    # Login TC-005
    def verify_latticeflow_login_success_or_not(self):
        self.headerLogin_button.click()
        self._email_input.fill()
        self._password_input.fill()
        self._login_button.click()
        #self._page.pause()
        #self.account_popup_manu.click()
        #self._page.wait_for_load_state("domcontentloaded")
        #self.logoutButton.wait_for(state="visible", timeout=10000)
        #return self.logoutButton.is_visible()







    
