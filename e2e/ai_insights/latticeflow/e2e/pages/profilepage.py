from playwright.sync_api import Page, expect
from utils import helpers


class ProfilePage:
    def __init__(self, page: Page) -> None:
        self._page = page    

        self.profileButton = self._page.locator("//div[@class='auth mobile-hide']//button[2]//*[name()='svg']//*[name()='path' and contains(@d,'M7,10L12,1')]")
        self.superadmin_button = self._page.locator("//span[normalize-space()='Super Admin']")
        self.organizationMenuItem = self._page.locator("//li[normalize-space()='Organization']")
        self.modelMenuItem = self._page.locator("//li[normalize-space()='Models']")
        self.vendorsMenuItem = self._page.locator("//li[normalize-space()='Vendors']")

        # Profile TC-009
        self.addOrganizations_button = self._page.locator("//button[normalize-space()='Add']//*[name()='svg']")
        self.organizationName_input = self._page.locator("//input[@placeholder='Enter Name']")
        self.accountStatusDropdown = self._page.locator("//div[text()='Select Account Status']")
        self.accountStatus_Active = self._page.locator("//li[normalize-space()='Active']")
        self.accountStatus_Deactivated = self._page.locator("//li[normalize-space()='Deactivated']")
        self.tierDropdown = self._page.locator("//div[text()='Select Tier']")
        self.tier_public = self._page.locator("//li[normalize-space()='Tier 1 - Public']")
        self.accessTypeDropdown = self._page.locator("//div[normalize-space()='Select Access Type']")
        self.accessType_customer = self._page.locator("//li[normalize-space()='Customer']")
        self.subscriptionEndDate_input = self._page.locator("//input[@placeholder='MM/DD/YYYY']")
        self.subscriptionTypeDropdown = self._page.locator("//div[text()='Select Subscription Type']")
        self.subscriptionType_Free = self._page.locator("//li[normalize-space()='Free']")
        self.save_button = self._page.locator("(//button[contains(@class, 'MuiButton-containedPrimary')])[1]")
        self.Organization_added_success_popup = self._page.locator("//h4[contains(text(),'Organization Added Successfully, You can now manag')]")

        # Profile TC-010
        self.delete_confirm_popup = self._page.locator("//button[normalize-space()='Delete']")
        self.org_delete_confirm_popup = self._page.locator("//h2[normalize-space()='Organization Deleted Successfully!']")
        
        # Profile TC-013
        self.addModel_Button = self._page.locator("//button[normalize-space()='Add']//*[name()='svg']")
        self.modelCode_input = self._page.locator("//input[@placeholder='Enter Code']")
        self.modelName_input = self._page.locator("//input[@placeholder='Enter Name']")
        self.details_input = self._page.locator("//input[@placeholder='Enter details']")
        self.model_added_success_popup = self._page.locator("//h2[normalize-space()='Model Added Successfully!']")

        # Profile TC-014
        self.model_edit_success_popup = self._page.locator("//h2[normalize-space()='Model Updated Successfully!']")
        self.model_deleted_success_popup  =self._page.locator("//h2[normalize-space()='Model Deleted Successfully!']")

        # Profile TC-017
        self.vendorCode_input = self._page.locator("//input[@placeholder='Enter Code']")
        self.vendorName_input = self._page.locator("//input[@placeholder='Enter Name']")
        self.vendor_added_success_popup = self._page.locator("//h2[normalize-space()='Vendor Added Successfully!']")
        self.cancel_popup = self._page.locator("//button[@title='Close']//*[name()='svg']")

        # Profile TC-018
        self.vendor_edited_success_popup = self._page.locator("//h2[normalize-space()='Vendor Updated Successfully!']")

        # Profile TC-019
        self.vendor_deleted_success_popup  = self._page.locator("//h2[normalize-space()='Vendor Deleted Successfully!']")

        # Profile TC-023
        self.models_search_input = self._page.locator("//input[@placeholder='Search…']")

        # Profile TC-031
        self.user_columnHeader = self._page.locator("//div[@class='MuiDataGrid-columnHeaderTitleContainerContent']")

        # Profile TC-032
        self.add_uesr_button = self._page.locator("//button[normalize-space()='Add']//*[name()='svg']")
        self.User_mail_input = self._page.locator("//input[@placeholder='Enter Email']")
        self.User_firstName_input = self._page.locator("//input[@placeholder='Enter First Name']")
        self.User_LastName_input = self._page.locator("//input[@placeholder='Enter Last Name']")
        self.Primary_user_dropdown = self._page.locator("//div[text()='Select Primary User']")
        self.Primary_user_yes = self._page.locator("//li[normalize-space()='Yes']")
        self.accessType_general_user = self._page.locator("//li[normalize-space()='general_user']")
        self.user_added_success_popup = self._page.locator("//h2[normalize-space()='User Added Successfully']")

        # Profile TC-033
        self.user_role_input = self._page.locator("//input[@placeholder='Enter Role/Title']")
        self.user_edited_success_popup = self._page.locator("//h2[normalize-space()='User Updated Successfully']")

        # Profile TC-034
        self.user_deleted_success_popup = self._page.locator("//h2[normalize-space()='User Deleted Successfully!']")
        


    def Verify_Organization_list_page_loads(self):
        self.profileButton.click()
        self.superadmin_button.click()
        self.organizationMenuItem.click()
        self._page.wait_for_load_state("domcontentloaded")
        return self._page.url
    
    def Verify_Models_page_loads(self):
        self.profileButton.click()
        self.superadmin_button.click()
        self.modelMenuItem.click()
        self._page.wait_for_load_state("domcontentloaded")
        return self._page.url
    
    def Verify_Vendors_page_loads(self):
        self.profileButton.click()
        self.superadmin_button.click()
        self.vendorsMenuItem.click()
        self._page.wait_for_load_state("domcontentloaded")
        return self._page.url
    
    def Create_a_new_Organization(self):
        self.profileButton.click()
        self.superadmin_button.click()
        self.organizationMenuItem.click()
        self._page.wait_for_load_state("domcontentloaded")
        self.addOrganizations_button.click()
        user = helpers.generate_user_data()
        self.organizationName_input.fill(user["first_name"])
        self.subscriptionTypeDropdown.click()
        self.subscriptionType_Free.click()
        self.subscriptionEndDate_input.fill("03/09/2025")
        self.accountStatusDropdown.click()
        self.accountStatus_Active.click()
        self.tierDropdown.click()
        self.tier_public.click()
        self.accessTypeDropdown.click()
        self.accessType_customer.click()

        self.save_button.click()  
        #self.Organization_added_success_popup.wait_for(state="visible", timeout=10000)
        #return self.Organization_added_success_popup.is_visible()
        
        try:
            self.Organization_added_success_popup.wait_for(state="visible", timeout=10000)
            print(f"✅ Organization created successfully: {user["first_name"]}")
            return user["first_name"] # ← Only return name if creation succeeded
        
        except Exception as e:
            print(f"❌ Organization creation failed: {e}")
            return False

    
    def edit_organization(self, org_name):
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
        self.subscriptionEndDate_input.scroll_into_view_if_needed()
        self.subscriptionEndDate_input.fill("03/10/2025")
        self.save_button.click()

        self.Organization_added_success_popup.wait_for(state="visible", timeout=10000)
        return self.Organization_added_success_popup.is_visible()

    def delete_organization(self, org_name):
        org_cell = self._page.locator(f"//div[text()='{org_name}']")

        org_cell.scroll_into_view_if_needed()
        row = org_cell.locator("..")

        more_action_button = row.locator("button[aria-label='More action']")
    
        if more_action_button.count() == 0:
            raise Exception(f"More action button not found for {org_name}")

        # Click to open the dropdown menu
        more_action_button.click()

        self._page.wait_for_selector("//li[@role='menuitem']", timeout=5000)

        delete_option = self._page.locator("//li[@role='menuitem']")
        delete_option.click()
        self.delete_confirm_popup.click()
        self.org_delete_confirm_popup.wait_for(state="visible", timeout=10000)
        return self.org_delete_confirm_popup.is_visible()
    
    def Create_model(self):
        self.profileButton.click()
        self.superadmin_button.click()
        self.modelMenuItem.click()
        self._page.wait_for_load_state("domcontentloaded")
        self.addModel_Button.click()
        user = helpers.generate_user_data()
        self.modelCode_input.fill(user["first_name"])
        self.modelName_input.fill(user["first_name"])
        self.details_input.fill(user["first_name"])
        self.save_button.click()
        
        # ✅ WAIT FOR SUCCESS POPUP TO APPEAR (CRITICAL VALIDATION)
        try:
            self.model_added_success_popup.wait_for(state="visible", timeout=10000)
            self.cancel_popup.click()
            print(f"✅ Model created successfully: {user["first_name"]}")
            return user["first_name"] # ← Only return name if creation succeeded
        
        except Exception as e:
            print(f"❌ Model creation failed: {e}")
            return False  # ← Explicitly indicate failure
    
    def edit_model(self, model_name):
        dropdown = self._page.locator("select")
        dropdown.wait_for(state="visible", timeout=10000)
        dropdown.scroll_into_view_if_needed()
        dropdown.select_option(value="All")
        dropdown.evaluate("el => el.value")
        org_cell = self._page.locator(f"(//div[text()='{model_name}'])[1]")
        org_cell.scroll_into_view_if_needed()
        row = org_cell.locator("..")
        edit_button = row.locator("button[aria-label='Edit']")

        if edit_button.count() == 0:
            raise Exception(f"Edit button not found for {model_name}")

        edit_button.click()

        # Optional: Wait for modal
        self._page.wait_for_timeout(1000)
        self.details_input.fill("Edited_This entry was created by our automated testing system to safely validate functionality without affecting real user data.")
        self.save_button.click()
        self.model_edit_success_popup.wait_for(state="visible", timeout=10000)
        return self.model_edit_success_popup.is_visible()
    
    def delete_model(self, model_name):
        org_cell = self._page.locator(f"(//div[text()='{model_name}'])[1]")
        org_cell.scroll_into_view_if_needed()
        row = org_cell.locator("..")
        delete_button = row.locator("button[aria-label='Delete']")

        if delete_button.count() == 0:
            raise Exception(f"Edit button not found for {model_name}")

        delete_button.click() 
        self.delete_confirm_popup.click()
        self.model_deleted_success_popup.wait_for(state="visible", timeout=10000)
        return self.model_deleted_success_popup.is_visible()
    
    def create_vendors(self):
        self.profileButton.click()
        self.superadmin_button.click()
        self.vendorsMenuItem.click()
        self._page.wait_for_load_state("domcontentloaded")
        self.addModel_Button.click()
        user = helpers.generate_user_data()
        self.vendorCode_input.fill(user["first_name"])
        self.vendorName_input.fill(user["first_name"])
        self.details_input.fill(user["first_name"])
        self.save_button.click()
        
        # ✅ WAIT FOR SUCCESS POPUP TO APPEAR (CRITICAL VALIDATION)
        try:
            self.vendor_added_success_popup.wait_for(state="visible", timeout=10000)
            self.cancel_popup.click()
            print(f"✅ Vendor created successfully: {user["first_name"]}")
            return user["first_name"]  # ← Only return name if creation succeeded
        
        except Exception as e:
            print(f"❌ Model creation failed: {e}")
            return False  
        
    def edit_vendors(self, vendor_name):
        dropdown = self._page.locator("select")
        dropdown.wait_for(state="visible", timeout=10000)
        dropdown.scroll_into_view_if_needed()
        dropdown.select_option(value="All")
        dropdown.evaluate("el => el.value")
        org_cell = self._page.locator(f"(//div[text()='{vendor_name}'])[1]")
        org_cell.scroll_into_view_if_needed()
        row = org_cell.locator("..")
        edit_button = row.locator("button[aria-label='Edit']")

        if edit_button.count() == 0:
            raise Exception(f"Edit button not found for {vendor_name}")

        edit_button.click()

        # Optional: Wait for modal
        self._page.wait_for_timeout(1000)
        self.details_input.fill("Edited_This entry was created by our automated testing system to safely validate functionality without affecting real user data.")
        self.save_button.click()
        self.vendor_edited_success_popup.wait_for(state="visible", timeout=10000)
        return self.vendor_edited_success_popup.is_visible()    
    
    
    def delete_vendors(self, vendor_name):
        org_cell = self._page.locator(f"(//div[text()='{vendor_name}'])[1]")
        org_cell.scroll_into_view_if_needed()
        row = org_cell.locator("..")
        delete_button = row.locator("button[aria-label='Delete']")

        if delete_button.count() == 0:
            raise Exception(f"Edit button not found for {vendor_name}")

        delete_button.click() 
        self.delete_confirm_popup.click()
        self.vendor_deleted_success_popup.wait_for(state="visible", timeout=10000)
        return self.vendor_deleted_success_popup.is_visible()
    
    # Profile TC-023
    def verify_model_search_functionality(self, model_name):
        self.models_search_input.fill(model_name)
        model_cell = self._page.locator(f"//div[text()='{model_name}']")
        model_cell.wait_for(state="visible", timeout=10000)
        actual_text = model_cell.inner_text()
        print(f"🔍 Search result found: '{actual_text}'")
        return actual_text
    
    # Profile TC-031
    def click_on_user_icon_from_Ororganization(self,org_name):
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
        user_button = row.locator("button[aria-label='Users']")

                    # Step 5: Validate and click
        if user_button.count() == 0:
            raise Exception(f"Edit button not found for {org_name}")

        user_button.click()

    def get_user_table_headers(self):
        """
        Fetches and returns the text of all column headers from the MUI DataGrid table.
        Returns: ['Name', 'Email', 'Primary User', 'Subscription Type', ...]
        """
        # ✅ WAIT FOR THE TABLE CONTAINER TO BE LOADED (this ensures headers will appear)
        self._page.wait_for_selector("div.MuiDataGrid-root", state="visible", timeout=10000)

        # ✅ LOCATE ALL HEADER TITLES — NO .wait_for() ON THIS!
        headers_locator = self._page.locator("div.MuiDataGrid-columnHeaderTitleContainerContent")

        # ✅ SAFELY EXTRACT ALL TEXT CONTENTS — .all_text_contents() handles multiple elements
        headers_text = [
            text.strip()
            for text in headers_locator.all_text_contents()
            if text.strip()
        ]

        # ✅ LOG EACH HEADER INDIVIDUALLY (your request!)
        print(f"🔍 Found {len(headers_text)} column headers:")
        for i, header in enumerate(headers_text, start=1):
            print(f"   [{i}] → '{header}'")

        return headers_text  

    # Profile TC-032
    def add_user_from_action_tab_from_organization(self):
        self.add_uesr_button.click()
        user = helpers.generate_user_data()
        self.User_mail_input.fill(user["email"])
        self.User_firstName_input.fill(user["first_name"])
        self.User_LastName_input.fill(user["last_name"])
        self.Primary_user_dropdown.click()
        self.Primary_user_yes.click()
        self.subscriptionEndDate_input.fill("03/09/2025")
        self.accountStatusDropdown.click()
        self.accountStatus_Active.click()
        self.accessTypeDropdown.click()
        self.accessType_general_user.click()
        self.tierDropdown.click()
        self.tier_public.click()
        self.save_button.click()
        # self.user_added_success_popup.is_visible()
        # self.user_added_success_popup.wait_for(state="visible", timeout=10000)
        #return self.user_added_success_popup.is_visible()
    

        try:
            self.user_added_success_popup.wait_for(state="visible", timeout=10000)
            print(f"✅ User created successfully: {user["first_name"]}")
            return user["first_name"]  # ← Only return name if creation succeeded
        
        except Exception as e:
            print(f"❌ Model creation failed: {e}")
            return False
    
    
    

    # Profile TC-033
    def edit_user(self, user_name):
        dropdown = self._page.locator("select")
        dropdown.wait_for(state="visible", timeout=10000)
        dropdown.scroll_into_view_if_needed()
        dropdown.select_option(value="All")
        dropdown.evaluate("el => el.value")
        #org_cell = self._page.get_by_role("gridcell", name=user_name).first
        #org_cell.wait_for(state="visible", timeout=10000)
        #org_cell.scroll_into_view_if_needed()
        #row = org_cell.locator("..")
        #edit_button = row.locator("button[aria-label='Edit']")
        edit_button = self._page.locator("button[aria-label='Edit']")

        if edit_button.count() == 0:
            raise Exception(f"Edit button not found for {user_name}")

        edit_button.click()

        # Optional: Wait for modal
        self._page.wait_for_timeout(1000)
        self.user_role_input.fill("Edited_UserRole.")
        self.save_button.click()
        self.user_edited_success_popup.wait_for(state="visible", timeout=10000)
        return self.user_edited_success_popup.is_visible()  
    

    def delete_user(self):
        delete_button = self._page.locator("button[aria-label='Delete']")
        delete_button.wait_for(state="visible", timeout=10000)
        delete_button.click() 
        self.delete_confirm_popup.click()
        self.user_deleted_success_popup.wait_for(state="visible", timeout=10000)
        return self.user_deleted_success_popup.is_visible()
    

    
    


    
    
    

