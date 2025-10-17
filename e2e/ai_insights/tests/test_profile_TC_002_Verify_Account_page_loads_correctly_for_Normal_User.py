from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_profile_TC_002_Verify_Account_page_loads_correctly_for_Normal_User(user):
    home_page = Homepage(user._page)

    actual_status = home_page.verify_Account_Page_Loads_For_Normal_User()

    check.equal(actual_status, True, f"URL mismatch: Expected '{"True"}', but got '{actual_status}'")
    print(f"➡️ is account Page loads correctly : Expected='{"True"}', Actual='{actual_status}'")