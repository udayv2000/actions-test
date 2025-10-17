from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.termsofservicepage import TermsofServicePage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_verify_Terms_of_Service_content(guest_user):
    home_page = Homepage(guest_user._page)
    TermsofService_Page = TermsofServicePage(guest_user._page)

    # Terms of Service Page URL validation from footer
    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_007", data_tcid="TC_007_01")

    home_page.go_to_footer()
    home_page.click_terms_of_service_from_footer()
    actual_TermsofService_URL = home_page.get_current_url()
    expected_TermsofService_URL = test_data["Footer_terms-of-service_URL"]
    check.equal(actual_TermsofService_URL, expected_TermsofService_URL, f"URL mismatch: Expected '{expected_TermsofService_URL}', but got '{actual_TermsofService_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_TermsofService_URL}', Actual='{actual_TermsofService_URL}'")

    

    # validate communication mails
    is_present  = TermsofService_Page.validate_communication_mails()
    check.equal(is_present, True, f"URL mismatch: Expected '{True}', but got '{is_present}'")
    print(f"➡️ Validating communication mails: Expected='{True}', Actual='{is_present}'")

    # validate securityIssuesReporting mail
    is_present_01 = TermsofService_Page.validate_securityIssuesReporting_mail()
    check.equal(is_present_01, True, f"URL mismatch: Expected '{True}', but got '{is_present_01}'")
    print(f"➡️ Validating securityIssuesReporting mail: Expected='{True}', Actual='{is_present_01}'")

