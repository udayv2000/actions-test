from playwright.sync_api import expect
from playwright.sync_api import Page
from utils import helpers


class Homepage:
    def __init__(self, page: Page) -> None:
        self._page = page

        ## Home ##
        self._login_button = self._page.locator(".mobile-hide .auth-button")
        self._profile_icon = self._page.locator(".auth .MuiAvatar-root")
        self._cards = self._page.locator("xpath=//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-72dktb']")
        self.logo = self._page.locator("div.logo img[alt='logo']")
        self.mainHeading = self._page.locator("//h1[text()='Make smarter AI model decisions']")

        ## Resourse ##
        self.resources_menu = self._page.locator("//span[text()='Resources']")
        self.press_link = self._page.locator("//span[normalize-space()='Press']")
        self.header_education_link = self._page.locator("//span[normalize-space()='Education']")
        self.model_reports_link = self._page.locator("//ul[@role='menu']//span[text()='Model Reports']")

        ## Evaluation Results ##
        # HomePage TC-004
        self.evaluationResults_menu = self._page.locator("//span[text()='Evaluation Results']")
        self.AIinsightsLeaderboard_link = self._page.locator("//span[text()='AI Insights Leaderboard']")
        self.modelInsights_link = self._page.locator("//span[text()='Model Insights']")

        ## Model Reports ##
        # HomePage TC-005
        self.modelReports_link = self._page.locator("//span[normalize-space()='Model Reports']")

        ## Support ##
        # HomePage TC-005
        self.support_link = self._page.locator("//span[normalize-space()='Support']")
        self.supportPage_header = self._page.locator("(//h2[text()='General Request'])[1]")

        ## About ##
        # HomePage TC-005
        self.about_link = self._page.locator("//span[normalize-space()='About']")

        ## Footer ##
        # HomePage TC-008
        self.footer = self._page.locator("//footer[@class='footer']")

        # HomePage TC-009
        self.footer_modelreport = self._page.locator("//a[normalize-space()='Model Reports']")

        # HomePage TC-007
        self.footer_modelinsights = self._page.locator("//a[normalize-space()='Model Insights']")
        self.cancel_register_or_Login_popup = self._page.locator("//button[normalize-space()='Cancel']")
        self.leaderboard_link = self._page.locator("//a[normalize-space()='AI Insights Leaderboard']")
        self.education_link = self._page.locator("//a[normalize-space()='Education']")
        self.modelReports = self._page.locator("//a[normalize-space()='Model Reports']")
        self.footer_about = self._page.locator("//a[normalize-space()='About']")
        self.tearmsofservice = self._page.locator("//a[normalize-space()='Terms of Service']")

        # HomePage TC-008
        self.latticeflow_linkedin_icon = self._page.locator("//a[@href='https://www.linkedin.com/company/latticeflow']")
        self.latticeflow_X_icon = self._page.locator("//a[@href='https://x.com/latticeflowai']")
        self.latticeflow_youtube_icon = self._page.locator("//a[@href='https://www.youtube.com/@latticeflow']")

        # Others TC-002
        self.footer_about = self._page.locator("//a[normalize-space()='About']")

        # Others TC-004
        self.footer_PrivacyPolicy = self._page.locator("//a[normalize-space()='Privacy Policy']")

        # Profile TC-002
        self.account_popup_manu = self._page.locator("//div[@class='auth mobile-hide']//button[2]//*[name()='svg']//*[name()='path' and contains(@d,'M7,10L12,1')]")
        self.account_button = self._page.locator("//span[normalize-space()='Account']")
        self.changePassword_Button = self._page.locator("//button[normalize-space()='Change Password']")

        # Profile TC-001
        self.header_loginButton = self._page.locator("//div[@class='auth mobile-hide']//span[contains(text(),'LOG IN')]")
        self._email_input = self._page.locator("#username")
        self._password_input = self._page.locator("#password")
        self.submit_button = self._page.locator("//button[@type='submit']")
        self.superadmin_button = self._page.locator("//span[normalize-space()='Super Admin']")
        self.logout_button = self._page.locator("//span[normalize-space()='Logout']")

        # Profile TC-006
        self.organizationMenuItem = self._page.locator("//li[normalize-space()='Organization']")
        self.usersMenuItem = self._page.locator("//li[normalize-space()='Users']")
        self.modelMenuItem = self._page.locator("//li[normalize-space()='Models']")
        self.vendorsMenuItem = self._page.locator("//li[normalize-space()='Vendors']")

        # Profile TC-004
        self.oldPassword_input = self._page.locator("//input[@placeholder='Enter old password']")
        self.newPasswprd_input = self._page.locator("//input[@placeholder='Enter new password']")
        self.confirmPassword_input = self._page.locator("//input[@placeholder='Confirm new password']")
        self.save_button = self._page.locator("//button[normalize-space()='Save']")
        self.errorPopup = self._page.locator("//h4[contains(text(),'Old password validation failed: Invalid user crede')]")


        # Profile TC-006
        self.remembermecheckbox = self._page.locator("//input[@name='rememberMe']")

        # Profile TC-007
        self.forgotpassword_link = self._page.locator("//div[@class='forgot-password']")
        self.resetpasswordsentconfirm_popup = self._page.locator("//h4[normalize-space()='Reset password URL has been sent to your email.']")
        self.forgotresetSubmitButton = self._page.locator("//button[normalize-space()='Submit']")

        # Profile TC-03
        self.headerLogin_button = self._page.locator("//div[@class='auth mobile-hide']//span[contains(text(),'LOG IN')]")
        
    def launch_application(self):
        self.goto    

    def open_login(self) -> None:
        self._login_button.click()

    def verify_user_logged_in(self) -> None:
        expect(self._profile_icon).to_be_visible(timeout=3000)

        # Resourse
    def open_resources_dropdown(self):
        self._page.wait_for_load_state("domcontentloaded")
        self.resources_menu.click()    

    def go_to_press(self):
        
        self._page.wait_for_load_state("domcontentloaded")
        self.open_resources_dropdown()

        # Expect a new tab to open
        with self._page.expect_popup() as popup_info:
            self.press_link.click()

        # Get the new page (tab)
        new_page = popup_info.value
    
         # Wait for the new page to load
        new_page.wait_for_load_state()

        # Store the new page so we can access its URL later
        self._current_popup_page = new_page      

    def get_popup_url(self):
        # Returns new tab URL
        if hasattr(self, '_current_popup_page'):
            return self._current_popup_page.url
        raise Exception("No popup page available")      

        
    def go_to_education(self):
        #self._page.wait_for_load_state("domcontentloaded")
        self.open_resources_dropdown()
        self._page.wait_for_load_state("domcontentloaded")
        self.header_education_link.click()

    def go_to_modelReport(self):
        self.open_resources_dropdown()    
        self.model_reports_link.click()
        self._page.wait_for_load_state("domcontentloaded")

    def verify_logo(self) -> bool:
        """Waits for logo to be visible and returns True/False"""
        try:
            expect(self.logo).to_be_visible(timeout=5000)
            return True
        except Exception:
            return False   
        
    def get_current_url(self):
        return self._page.url
        
    def get_page_tittle(self) -> str:
        self._page.wait_for_load_state("domcontentloaded")
        page_title = self._page.title()
        return page_title    
        
    def verify_Main_heading(self):
        return self.mainHeading.inner_text().strip()
    
    
    # HomePage TC-004
    def go_to_AIinsightsLeaderboard(self):
        self.evaluationResults_menu.click()
        self.AIinsightsLeaderboard_link.click()
        self._page.wait_for_load_state("domcontentloaded")

    def go_to_modelInsights(self):
        self.evaluationResults_menu.click()
        self.modelInsights_link.click()
    
    # HomePage TC-005
    def go_to_modelReports(self):
        self.modelReports_link.click()
        self._page.wait_for_load_state("networkidle")

    def go_to_support(self):
        self.support_link.click() 
          
    
    def verify_supportPage_header(self):
        return self.supportPage_header.inner_text().strip()
    
    def go_to_about(self):
        self.about_link.click()

    # HomePage TC-007
         
    def go_to_footer(self):
       # self._page.pause()
        self.footer.scroll_into_view_if_needed()
    

    def click_modelReport_link_from_footer(self):
        self.footer_modelreport.click()

    def click_modelinsights_link_from_footer(self):   
        self.footer_modelinsights.click()
        #self._page.pause()

    def click_Leaderboard_link_from_footer(self):
        self.leaderboard_link.click() 
        #self._page.wait_for_load_state("domcontentloaded")  

    def click_Education_link_from_footer(self):    
        self.education_link.click()

    def click_ModelReports_link_from_footer(self):  
        self.modelReports.click()  

    def cancel_register_or_Login_popup_from_model_insightsPage(self): 
        self.cancel_register_or_Login_popup.click() 

    def click_about_link_from_footer(self):
        self.footer_about.click()

    def click_terms_of_service_from_footer(self):
        self.tearmsofservice.click()

    # HomePage TC-008
    def verify_linkedin(self):
        child = helpers.switch_to_child(self._page, self.latticeflow_linkedin_icon)
        linkedin_url = child.url
        helpers.switch_to_parent(child, self._page)
        return linkedin_url

    def verify_youtube(self):
        child = helpers.switch_to_child(self._page, self.latticeflow_youtube_icon)
        youtube_url = child.url
        helpers.switch_to_parent(child, self._page)
        return youtube_url
    
    def verify_X(self):
        child = helpers.switch_to_child(self._page, self.latticeflow_X_icon)
        x_url = child.url
        helpers.switch_to_parent(child, self._page)
        return x_url
    

    # Others TC-002
    def click_about_link_footer(self):
        self.footer_about.click()

    # Others TC-004
    def click_privacyPolicy_link_footer(self):
         # self.footer_PrivacyPolicy.click()   
         child = helpers.switch_to_child(self._page, self.footer_PrivacyPolicy)
         latticeflow_url = child.url
         print(f"➡️ Validating URL: Actual='{latticeflow_url}'")

    def verify_Account_Page_Loads_For_Normal_User(self): 
        self.account_popup_manu.click()
        self.account_button.click()
        return self.changePassword_Button.is_visible()
    
    
    # Evaluation Results TC-001
    def verify_evaluationResults_dropdown(self):
        self._page.wait_for_load_state("domcontentloaded")
        self.evaluationResults_menu.click() 

        return{
            "Model Insights": self.modelInsights_link.is_visible(),
            "AI Insights Leaderboard": self.AIinsightsLeaderboard_link.is_visible()
        }      

    # Profile TC-001
    def login_Super_Admin(self, email, password):
        #self._page.pause()
        self.header_loginButton.click()
        self._email_input.fill(email)
        self._password_input.fill(password)
        self._page.wait_for_load_state("networkidle")
        self.submit_button.click(timeout=10000)
        #self.submit_button.click()
        self._page.wait_for_load_state("networkidle")

    def verify_Account_Page_Loads_For_SuperAdmin(self):    
        self.account_popup_manu.click()
        return{
             "Super Admin": self.superadmin_button.is_visible(),
             "Account": self.account_button.is_visible(),
             "Logout": self.logout_button.is_visible()
        }

    # Profile TC-006
    def verify_super_admin_dropdown(self):
        #self._page.pause()
        self.account_popup_manu.click()
        self.superadmin_button.click()
        return {
            "organization": self.organizationMenuItem.is_visible(),
            "user": self.usersMenuItem.is_visible(),
            "models": self.modelMenuItem.is_visible(),
            "vendors": self.vendorsMenuItem.is_visible()
            
        } 
    
    # Profile TC-004
    def login_user(self, email, password) -> None:
        
       #self._page.pause()
        self._email_input.fill(email)
        self._password_input.fill(password)
        self._page.wait_for_load_state("networkidle")
        self.submit_button.click(timeout=10000)
        
        self._page.wait_for_load_state("networkidle")
        #self.account_popup_manu.wait_for(state="visible", timeout=10000)

    def change_Password_with_invalid_credentials(self):
        #self.account_popup_manu.wait_for(state="visible", timeout=5000)
        self._page.wait_for_timeout(2000)
        self.account_popup_manu.click()
        self.account_button.click()    
        self.changePassword_Button.scroll_into_view_if_needed()
        self.changePassword_Button.click()
        self.oldPassword_input.fill("abcdefg")
        self.newPasswprd_input.fill("newpassword")
        self.confirmPassword_input.fill("newpassword")
        self.save_button.click()
        self.errorPopup.wait_for(state="visible", timeout=10000)
        return self.errorPopup.is_visible()
    

    def logout_SuperAdmin(self):
        self.account_popup_manu.wait_for(state="visible", timeout=10000)
        self.account_popup_manu.click()
        self.logout_button.click()

    # Profile TC-007
    def verify_Limited_Menu_Options_For_Normal_User(self):
        self.account_popup_manu.click()
        return{
            "Account" : self.account_button.is_visible(),
            "Logout Button" :self.logout_button.is_visible()
        }
    

    def Verify_Remember_Me_option_works(self, email, password):

        self.header_loginButton.click()
        self._email_input.fill(email)
        self._password_input.fill(password)
        self._page.wait_for_load_state("networkidle")
        self.remembermecheckbox.check()
        self.submit_button.click(timeout=10000)
        #self.submit_button.click()
        self._page.wait_for_load_state("networkidle")

    def verify_forgot_password_functionality(self, mail):   

        self.header_loginButton.click()
        self.forgotpassword_link.click()
        self._email_input.fill(mail)
        self.forgotresetSubmitButton.click()
        self.resetpasswordsentconfirm_popup.wait_for(state="visible", timeout=10000)
        return self.resetpasswordsentconfirm_popup.is_visible()
    
    # Profile TC-03
    def change_Password_with_valid_credentials(self, oldPWD, newPWD,confirmPWD):
        self._page.wait_for_timeout(2000)
        self.account_popup_manu.click()
        self.account_button.click()    
        self.changePassword_Button.scroll_into_view_if_needed()
        self.changePassword_Button.click()
        self.oldPassword_input.fill(oldPWD)
        self.newPasswprd_input.fill(newPWD)
        self.confirmPassword_input.fill(confirmPWD)
        self.save_button.click()
        self.headerLogin_button.wait_for(state="visible", timeout=10000)
        return  self.headerLogin_button.is_visible()