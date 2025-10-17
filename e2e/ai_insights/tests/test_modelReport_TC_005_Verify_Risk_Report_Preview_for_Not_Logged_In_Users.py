from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_Risk_Report_Preview_for_Not_Logged_In_Users(guest_user):
    home_page = Homepage(guest_user._page)
    modelReport_page = ModelReportpage(guest_user._page)

    home_page.go_to_modelReport()

    test_data = read_test_data(sheet_name="ModelReportPage", parent_tcid="TC_005", data_tcid="TC_005_01")
    reportname = test_data["Risk Report"]
    modelReport_page.search_report(reportname)
    modelReport_page.open_report()
    modelReport_page.scroll_to_Login_prompt()

    is_popup_appered = modelReport_page.scroll_to_Login_prompt()

    check.equal(is_popup_appered, True, f"failed to show Login prompt: Expected '{"True"}', but got '{is_popup_appered}'")
    print(f"➡️ is Login prompt visible : Expected='{"True"}', Actual='{is_popup_appered}'")