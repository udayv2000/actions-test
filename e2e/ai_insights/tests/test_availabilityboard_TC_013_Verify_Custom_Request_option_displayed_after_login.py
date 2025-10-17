from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_Custom_Request_option_displayed_after_login(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)
    availabilityboard_Page = AvailabilityBoardPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    login_page.click_login_btn()
    home_page.login_user(mail, pwd)

    home_page.go_to_modelReports()
    actual_text = availabilityboard_Page.Verify_Custom_Request_link_is_visible_and_navigates_to_Support_Page()
    print(f"   Custom Request text: {actual_text}")

    check.equal(actual_text, "Custom Request", f"Text mismatch: Expected '{"Custom Request"}', but got '{actual_text}'")
    print(f"➡️  Support Page Opened  : Expected='{"Custom Request"}', Actual='{actual_text}'")