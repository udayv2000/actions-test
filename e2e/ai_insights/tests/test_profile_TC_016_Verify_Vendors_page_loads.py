from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_Vendors_page_loads(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)

    test_data = read_test_data(sheet_name="ProfilePage", parent_tcid="TC_016", data_tcid="TC_016_01")
    expected_VendorsPage_URL = test_data["VendorsPage_URL"]
    actual_VendorsPage_URL = profile_page.test_Verify_Vendors_page_loads()

    check.equal(actual_VendorsPage_URL, expected_VendorsPage_URL, f"URL mismatch: Expected '{expected_VendorsPage_URL}', but got '{actual_VendorsPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_VendorsPage_URL}', Actual='{actual_VendorsPage_URL}'")