from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_Change_Password_with_invalid_credentials(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    login_page.click_login_btn()
    home_page.login_user(mail, pwd)

    actual_error_status =home_page.change_Password_with_invalid_credentials()

    check.equal(actual_error_status, True, f"URL mismatch: Expected '{"True"}', but got '{actual_error_status}'")
    print(f"➡️ is Login success : Expected='{"True"}', Actual='{actual_error_status}'")