from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check

def test_Verify_Interested_action_after_login_records_interest(user):
    home_page = Homepage(user._page)
    availabilityboard_Page = AvailabilityBoardPage(user._page)

    home_page.go_to_modelReports()

    availabilityboard_Page.Click_Interested_icon_a_report_row()