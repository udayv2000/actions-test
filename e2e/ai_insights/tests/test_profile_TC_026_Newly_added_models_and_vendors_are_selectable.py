from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check
from utils.excel_reader import read_test_data



def test_Newly_added_models_and_vendors_are_selectable(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)
    modelReport_page = ModelReportpage(guest_user._page)
    

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)  


    # Create Vendor
    created_vendor_name = profile_page.create_vendors()

    check.is_true(
        created_vendor_name is not False,
        f"Vendor creation failed. Expected a Vendor name, got: {created_vendor_name}"
    )
    print(f"➡️ Vendor created successfully: '{created_vendor_name}'")



    # Create Model
    created_model_name = profile_page.Create_model()

    check.is_true(
        created_model_name is not False,
        f"Model creation failed. Expected a model name, got: {created_model_name}"
    )
    print(f"➡️ Model created successfully: '{created_model_name}'")


    home_page.go_to_modelReports()
    modelReport_page.click_add_model_report_button()
    

    success = modelReport_page.select_option_from_dropdown(modelReport_page.selectVendor, created_vendor_name)
    check.is_true(success, f"Failed to select vendor '{created_vendor_name}' from dropdown.")

    success = modelReport_page.select_option_from_dropdown(modelReport_page.selectModel, created_model_name)
    check.is_true(success, f"Failed to select model '{created_model_name}' from dropdown.")