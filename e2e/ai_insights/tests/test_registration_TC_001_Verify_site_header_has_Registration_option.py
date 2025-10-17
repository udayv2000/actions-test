from latticeflow.e2e.pages.registrationpage import RegistrationPage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_site_header_has_Registration_option(guest_user):
    registration_page = RegistrationPage(guest_user._page)

    test_data = read_test_data(sheet_name="RegistrationPage", parent_tcid="TC_001", data_tcid="TC_001_01")

    registration_page.click_on_signup()
    expected_url = test_data["RegistrationPage_URL"]
    actual_url= registration_page.verify_header_has_registration_option()

    check.equal(actual_url, expected_url, f"URL mismatch: Expected '{expected_url}', but got '{actual_url}'")
    print(f"➡️ Validating URL: Expected='{expected_url}', Actual='{actual_url}'")
