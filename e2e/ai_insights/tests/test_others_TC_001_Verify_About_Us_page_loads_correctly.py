from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_others_Verify_About_Us_page_loads_correctly(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_005", data_tcid="TC_005_01")

    # AboutPage URL validation
    home_page.go_to_about()
    actual_aboutPage_url=home_page.get_current_url()
    expected_aboutPage_url=test_data["AboutPage_URL"]

    check.equal(actual_aboutPage_url, expected_aboutPage_url, f"Text mismatch: Expected '{expected_aboutPage_url}', but got '{actual_aboutPage_url}'")
    print(f"➡️ Validating URL: Expected='{expected_aboutPage_url}', Actual='{actual_aboutPage_url}'")