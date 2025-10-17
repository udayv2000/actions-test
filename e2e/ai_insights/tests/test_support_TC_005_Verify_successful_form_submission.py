from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.supportpage import SupportPage
from utils.excel_reader import read_test_data
from pytest_check import check

def test_Verify_successful_form_submission(guest_user):
    home_page = Homepage(guest_user._page)
    support_page = SupportPage(guest_user._page)

    home_page.go_to_support()

    test_data = read_test_data(sheet_name="SupportPage", parent_tcid="TC_005", data_tcid="TC_005_01")
    Email = test_data["Email"]
    Subject = test_data["Subject"]
    Message = test_data["Message"]

    

    is_confirm_popup_appered = support_page.Verify_successful_form_submission(Email, Subject, Message)

    check.equal(is_confirm_popup_appered, True, f"failed to send a request: Expected '{"True"}', but got '{is_confirm_popup_appered}'")
    print(f"➡️ is request sent sucessfully : Expected='{"True"}', Actual='{is_confirm_popup_appered}'")