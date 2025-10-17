from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_search_functionality_in_Organization_page(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)

    created_Organization_name = profile_page.Create_a_new_Organization()

    check.is_true(
        created_Organization_name is not False,
        f"Organization creation failed. Expected a Organization name, got: {created_Organization_name}"
    )
    print(f"➡️ Organization created successfully: '{created_Organization_name}'")


    # Organization search
    actual_model_appeared = profile_page.verify_model_search_functionality(created_Organization_name)

    check.equal(actual_model_appeared, created_Organization_name, f"Vendor mismatch: Expected '{created_Organization_name}', but got '{actual_model_appeared}'")
    print(f"➡️ Validating Vendor: Expected='{created_Organization_name}', Actual='{actual_model_appeared}'")