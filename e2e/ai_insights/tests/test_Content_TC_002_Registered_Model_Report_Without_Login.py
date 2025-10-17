from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check


def test_Model_Report_Without_Login(guest_user):
    home_page = Homepage(guest_user._page)
    modelReport_page = ModelReportpage(guest_user._page)

    home_page.go_to_modelReport()

    is_popup_appered =modelReport_page.verify_Login_prompt_shown_Model_Report()

    check.equal(is_popup_appered, True, f"failed to show Login prompt in Model Report: Expected '{"True"}', but got '{is_popup_appered}'")
    print(f"➡️ is Login prompt visible in model report  : Expected='{"True"}', Actual='{is_popup_appered}'")
