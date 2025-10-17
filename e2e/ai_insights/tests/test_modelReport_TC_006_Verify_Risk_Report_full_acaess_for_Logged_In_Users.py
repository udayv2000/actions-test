from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_Risk_Report_full_acaess_for_Logged_In_Users(user):
    home_page = Homepage(user._page)
    modelReport_page = ModelReportpage(user._page)

    home_page.go_to_modelReport()

    test_data = read_test_data(sheet_name="ModelReportPage", parent_tcid="TC_005", data_tcid="TC_005_01")
    reportname = test_data["Risk Report"]
    modelReport_page.search_report(reportname)
   # modelReport_page.verify_Login_prompt_shown_Model_Report()

    is_header_appered =modelReport_page.selected_article_loads_with_content()

    check.equal(is_header_appered, True, f"failed to access full risk report: Expected '{"True"}', but got '{is_header_appered}'")
    print(f"➡️ is risk report fully accessable  : Expected='{"True"}', Actual='{is_header_appered}'")
    