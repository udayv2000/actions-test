from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Create_a_Model_Report_with_Model_and_Vendor(guest_user):
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

    actual_model_created_status = modelReport_page.add_new_model(created_vendor_name, created_model_name)

    check.equal(actual_model_created_status, True, f"failed to add model: Expected '{"True"}', but got '{actual_model_created_status}'")
    print(f"➡️ is model Added success popup appered: Expected='{"True"}', Actual='{actual_model_created_status}'")