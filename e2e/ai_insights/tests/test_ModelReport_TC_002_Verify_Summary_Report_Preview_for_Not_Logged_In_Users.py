from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check


def test_Verify_Summary_Report_Preview_for_Not_Logged_In_Users(guest_user):
     home_page = Homepage(guest_user._page)
     modelReport_page = ModelReportpage(guest_user._page)

     home_page.go_to_modelReport()

     is_loaded_status = modelReport_page.verify_Login_prompt_shown_Model_Report()

     check.equal(is_loaded_status, True, f"failed to scroll: Expected '{"True"}', but got '{is_loaded_status}'")
     print(f"➡️ is Wiki content is accessible: Expected='{"True"}', Actual='{is_loaded_status}'")