from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check


def test_Verify_Interested_action_prompts_login_when_not_logged_in(guest_user):
    home_page = Homepage(guest_user._page)
    availabilityboard_Page = AvailabilityBoardPage(guest_user._page)

    home_page.go_to_modelReports()

    availabilityboard_Page.Click_Interested_icon_a_report_row()
    actual_status = availabilityboard_Page.Verify_Register_or_Login_prompt()

    check.equal(actual_status, True, f"is Register or Login Card visible: Expected '{"True"}', but got '{actual_status}'")
    print(f"➡️ is Register or Login Card visible : Expected='{"True"}', Actual='{actual_status}'")