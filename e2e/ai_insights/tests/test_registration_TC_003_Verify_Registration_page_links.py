from latticeflow.e2e.pages.registrationpage import RegistrationPage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_Registration_page_links(guest_user):
    registration_page = RegistrationPage(guest_user._page)

    test_data = read_test_data(sheet_name="RegistrationPage", parent_tcid="TC_003", data_tcid="TC_003_01")

    registration_page.click_on_signup()
    actual_termsOfservice_URL = registration_page.verify_termsOfservice_links_on_registration_page()
    expected_TermsofService_URL = test_data["termsOfservice_URL"]

    check.is_in(expected_TermsofService_URL, actual_termsOfservice_URL, f"URL mismatch: Expected '{expected_TermsofService_URL}', but got '{actual_termsOfservice_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_TermsofService_URL}', Actual='{actual_termsOfservice_URL}'")
