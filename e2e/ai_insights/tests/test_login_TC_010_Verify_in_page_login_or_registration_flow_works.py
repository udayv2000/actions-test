from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_in_page_login_or_registration_flow_works(guest_user):
    home_page = Homepage(guest_user._page)
    ModelReport_page=ModelReportpage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")

    mail = test_data["EMAIL"].strip()
    password = test_data["PASSWORD"].strip()

    home_page.go_to_modelReport()

    actual_login_status = ModelReport_page.verify_signin_or_signup_from_the_modelReport(mail,password)

    check.equal(actual_login_status, True, f"URL mismatch: Expected '{"True"}', but got '{actual_login_status}'")
    print(f"➡️ is Login success : Expected='{"True"}', Actual='{actual_login_status}'")
    
