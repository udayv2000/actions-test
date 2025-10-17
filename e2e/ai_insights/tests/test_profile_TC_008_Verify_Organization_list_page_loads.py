from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data





def test_Verify_Organization_list_page_loads(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)

    test_data = read_test_data(sheet_name="ProfilePage", parent_tcid="TC_008", data_tcid="TC_008_01")
    expected_OrganizationPage_URL = test_data["OrganizationPage_URL"]
    actual_OrganizationPage_URL = profile_page.Verify_Organization_list_page_loads()

    check.equal(actual_OrganizationPage_URL, expected_OrganizationPage_URL, f"URL mismatch: Expected '{expected_OrganizationPage_URL}', but got '{actual_OrganizationPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_OrganizationPage_URL}', Actual='{actual_OrganizationPage_URL}'") 