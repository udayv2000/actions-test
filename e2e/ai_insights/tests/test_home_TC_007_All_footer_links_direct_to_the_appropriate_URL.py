from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_All_footer_links_direct_to_the_appropriate_URL(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_007", data_tcid="TC_007_01")

    home_page.go_to_footer()

    # Modelinsights URL validation from footer
    home_page.click_modelinsights_link_from_footer()
    actual_modelinsightsPage_URL=home_page.get_current_url()
    expected_modelinsightsPage_URL= test_data["Footer_ModelinsightsPage_URL"]
    check.equal(actual_modelinsightsPage_URL, expected_modelinsightsPage_URL, f"URL mismatch: Expected '{expected_modelinsightsPage_URL}', but got '{actual_modelinsightsPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_modelinsightsPage_URL}', Actual='{actual_modelinsightsPage_URL}'")
    home_page.cancel_register_or_Login_popup_from_model_insightsPage()

    # Leaderboard URL validation from footer
    home_page.go_to_footer()
    home_page.click_Leaderboard_link_from_footer()
    actual_leaderboardPage_URL = home_page.get_current_url()
    expected_leaderboardPage_URL = test_data["Footer_LeaderboardPage_URL"]
    check.equal(actual_leaderboardPage_URL, expected_leaderboardPage_URL, f"URL mismatch: Expected '{expected_leaderboardPage_URL}', but got '{actual_leaderboardPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_leaderboardPage_URL}', Actual='{actual_leaderboardPage_URL}'")

    # Education URL validation from footer
    home_page.go_to_footer()
    home_page.click_Education_link_from_footer()
    actual_educationPage_URL = home_page.get_current_url()
    expected_educationPage_URL = test_data["Footer_EducationPage_URL"]
    check.equal(actual_educationPage_URL, expected_educationPage_URL, f"URL mismatch: Expected '{expected_educationPage_URL}', but got '{actual_educationPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_educationPage_URL}', Actual='{actual_educationPage_URL}'")

    # Model Reports URL validation from footer
    home_page.go_to_footer()
    home_page.click_ModelReports_link_from_footer()
    actual_modelReportPage_URL = home_page.get_current_url()
    expected_modelReportPage_URL = test_data["Footer_ModelReport_URL"]
    check.equal(actual_modelReportPage_URL, expected_modelReportPage_URL, f"URL mismatch: Expected '{expected_modelReportPage_URL}', but got '{actual_modelReportPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_modelReportPage_URL}', Actual='{actual_modelReportPage_URL}'")

    # About URL validation from footer
    home_page.go_to_footer()
    home_page.click_about_link_from_footer()
    actual_aboutPage_URL = home_page.get_current_url()
    expected_aboutPage_URL = test_data["Footer_AboutPage_URL"]
    check.equal(actual_aboutPage_URL, expected_aboutPage_URL, f"URL mismatch: Expected '{expected_aboutPage_URL}', but got '{actual_aboutPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_aboutPage_URL}', Actual='{actual_aboutPage_URL}'")

    # Terms of Service Page URL validation from footer
    home_page.go_to_footer()
    home_page.click_terms_of_service_from_footer()
    actual_TermsofService_URL = home_page.get_current_url()
    expected_TermsofService_URL = test_data["Footer_terms-of-service_URL"]
    check.equal(actual_TermsofService_URL, expected_TermsofService_URL, f"URL mismatch: Expected '{expected_TermsofService_URL}', but got '{actual_TermsofService_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_TermsofService_URL}', Actual='{actual_TermsofService_URL}'")
