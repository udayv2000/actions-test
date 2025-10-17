from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data



def test_Verify_the_Evaluation_Results_drop_down_and_links_redirects_to_appropriate_pages(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_004", data_tcid="TC_004_01")

    # Leaderboard URL validation
    home_page.go_to_AIinsightsLeaderboard()
    actual_LeaderboardPageurl = home_page.get_current_url()
    expected_LeaderboardPageurl= test_data["LeaderboardPageurl"]
    check.equal(actual_LeaderboardPageurl, expected_LeaderboardPageurl, f"URL mismatch: Expected '{expected_LeaderboardPageurl}', but got '{actual_LeaderboardPageurl}'")
    print(f"➡️ Validating URL: Expected='{expected_LeaderboardPageurl}', Actual='{actual_LeaderboardPageurl}'")

    # ModelInsights URL validation
    home_page.go_to_modelInsights()
    actual_modelInsightsPageurl = home_page.get_current_url()
    expected_modelInsightsPageurl= test_data["ModelinsightsPageurl"]
    check.equal(actual_modelInsightsPageurl, expected_modelInsightsPageurl, f"URL mismatch: Expected '{expected_modelInsightsPageurl}', but got '{actual_modelInsightsPageurl}'")
    print(f"➡️ Validating URL: Expected='{expected_modelInsightsPageurl}', Actual='{actual_modelInsightsPageurl}'")


