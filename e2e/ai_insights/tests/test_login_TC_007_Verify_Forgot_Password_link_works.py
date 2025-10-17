
from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.logout import LogoutPage
from pytest_check import check
from utils.excel_reader import read_test_data



def test_Verify_Forgot_Password_link_works(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Login_with_Google")
    mail = test_data["EMAIL"]

    is_popup_appered = home_page.verify_forgot_password_functionality(mail)

    check.equal(is_popup_appered, True, f"failed to send forgot password link to mail: Expected '{"True"}', but got '{is_popup_appered}'")
    print(f"➡️ is forgot password link sent to mail : Expected='{"True"}', Actual='{is_popup_appered}'")