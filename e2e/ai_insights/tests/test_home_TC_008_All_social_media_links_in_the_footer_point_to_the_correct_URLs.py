from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_All_social_media_links_in_the_footer_point_to_the_correct_URLs(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_008", data_tcid="TC_008_01")

    home_page.go_to_footer()

    # verify LatticeFlow linkedin URL
    actual_linkedin_url = home_page.verify_linkedin()
    expected_linkedin_url = test_data["latticeflow_lindedin_URL"]

    check.equal(actual_linkedin_url, expected_linkedin_url, f"URL mismatch: Expected '{expected_linkedin_url}', but got '{actual_linkedin_url}'")
    print(f"➡️ Validating URL: Expected='{expected_linkedin_url}', Actual='{actual_linkedin_url}'")

    # verify LatticeFlow youtube URL
    actual_youtube_url = home_page.verify_youtube()
    expected_youtube_url = test_data["latticeflow_youtube_URL"]

    check.equal(actual_youtube_url, expected_youtube_url, f"URL mismatch: Expected '{expected_youtube_url}', but got '{actual_youtube_url}'")
    print(f"➡️ Validating URL: Expected='{expected_youtube_url}', Actual='{actual_youtube_url}'")

    # verify LatticeFlow youtube URL
    actual_x_url = home_page.verify_X()
    expected_x_url = test_data["latticeflow_X_URL"]

    check.equal(actual_x_url, expected_x_url, f"URL mismatch: Expected '{expected_x_url}', but got '{actual_x_url}'")
    print(f"➡️ Validating URL: Expected='{expected_x_url}', Actual='{actual_x_url}'")

    # print(f"Linkedin url: '{actual_linkedin_url}'")
    # print(f"Linkedin url: '{actual_youtube_url}'")
    # print(f"Linkedin url: '{actual_x_url}'")