from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check
from utils.excel_reader import read_test_data
from utils import helpers

def test_Verify_all_summary_and_risk_report_links(guest_user):
    home_page = Homepage(guest_user._page)
    availabilityboard_Page = AvailabilityBoardPage(guest_user._page)

    test_data = read_test_data(sheet_name="AvailabilityBoardPage", parent_tcid="TC_003", data_tcid="TC_003_01")
    modelName = test_data["Search_model"]
    summary_text = test_data["text1"]
    risk_text = test_data["text2"]


    home_page.go_to_modelReports()

    availabilityboard_Page.verify_search_functionality(modelName)

    summaryreport_actual_status = availabilityboard_Page.verify_summaryreportpage_opened_or_not()
    check.equal(summaryreport_actual_status, True, f"is Summary report header visible: Expected '{"True"}', but got '{summaryreport_actual_status}'")
    print(f"➡️ is Summary report header visible : Expected='{"True"}', Actual='{summaryreport_actual_status}'")



    



