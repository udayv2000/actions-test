from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.aboutpage import Aboutpage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_others_Verify_Privacy_Policy_link_navigates_to_correct_URL(guest_user):
    home_page = Homepage(guest_user._page)
    about_page = Aboutpage(guest_user._page)

    test_data = read_test_data(sheet_name="AboutPage", parent_tcid="TC_003", data_tcid="TC_003_01")

    home_page.go_to_footer()

    actual_privacy_policy_url = about_page.verify_privacy_policy()
    expected_privacy_policy_url = test_data["Privacy-Policy_URL"]
    check.is_in(expected_privacy_policy_url, actual_privacy_policy_url, f"URL mismatch: Expected '{expected_privacy_policy_url}', but got '{actual_privacy_policy_url}'")
    print(f"➡️ Validating URL: Expected='{expected_privacy_policy_url}', Actual='{actual_privacy_policy_url}'")