from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check
from utils.excel_reader import read_test_data




def test_Verify_login_with_Gmail_works_with_gated_content(guest_user):
    home_page = Homepage(guest_user._page)
    ModelReport_page=ModelReportpage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Login_with_Google")

    mail = test_data["EMAIL"].strip()
    password = test_data["PASSWORD"].strip()

    home_page.go_to_modelReport()

    actual_login_status = ModelReport_page.verify_Gmail_login_to_view_report_from_Model_report(mail,password)

    check.equal(actual_login_status, True, f"URL mismatch: Expected '{"True"}', but got '{actual_login_status}'")
    print(f"➡️ is Login success : Expected='{"True"}', Actual='{actual_login_status}'")