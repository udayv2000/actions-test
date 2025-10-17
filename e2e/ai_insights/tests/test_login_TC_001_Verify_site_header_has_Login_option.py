from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_site_header_has_Login_option(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginPage", parent_tcid="TC_001", data_tcid="TC_001_01")

    # Loginpage URL validation
    home_page.open_login()
    actual_loginpage_URL = login_page.get_current_url()
    expected_loginpage_URL= test_data["LoginPage_URL"]
    check.equal(actual_loginpage_URL, expected_loginpage_URL, f"URL mismatch: Expected '{expected_loginpage_URL}', but got '{actual_loginpage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_loginpage_URL}', Actual='{actual_loginpage_URL}'")


    # Loginpage title validation
    actual_loginpage_title = login_page.get_page_tittle()
    expected_loginpage_title= test_data["LoginPage_title"]
    check.equal(actual_loginpage_title, expected_loginpage_title, f"URL mismatch: Expected '{expected_loginpage_title}', but got '{actual_loginpage_title}'")
    print(f"➡️ Validating URL: Expected='{expected_loginpage_title}', Actual='{actual_loginpage_title}'")
    