from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_Change_Password_button_flow(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    login_page.click_login_btn()
    home_page.login_user(mail, pwd)

    actual_status =home_page.change_Password_with_valid_credentials(pwd,pwd, pwd)

    check.equal(actual_status, True, f"is Password updated: Expected '{"True"}', but got '{actual_status}'")
    print(f"➡️ is Password updated : Expected='{"True"}', Actual='{actual_status}'")