from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_Sign_Up_Link(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginPage", parent_tcid="TC_003", data_tcid="TC_003_01")

    home_page.open_login()

    actual_signupPage_url = login_page.verify_signup_link()
    expected_signupPage_url = test_data["SignupPage_URL"]
    check.equal(actual_signupPage_url, expected_signupPage_url, f"URL mismatch: Expected '{expected_signupPage_url}', but got '{actual_signupPage_url}'")
    print(f"➡️ Validating URL: Expected='{expected_signupPage_url}', Actual='{actual_signupPage_url}'")


def test_Verify_forgot_Password_Link(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginPage", parent_tcid="TC_003", data_tcid="TC_003_01")

    home_page.open_login()

    actual_forgotPasswordPage_url = login_page.verify_forgot_password_link()
    expected_forgotPasswordPage_url = test_data["ForgotPasswordPage_URL"]
    check.equal(actual_forgotPasswordPage_url, expected_forgotPasswordPage_url, f"URL mismatch: Expected '{expected_forgotPasswordPage_url}', but got '{actual_forgotPasswordPage_url}'")
    print(f"➡️ Validating URL: Expected='{expected_forgotPasswordPage_url}', Actual='{actual_forgotPasswordPage_url}'")