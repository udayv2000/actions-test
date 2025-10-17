from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_the_model_report_support_about_and_links_redirects_to_appropriate_pages(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_005", data_tcid="TC_005_01")

    # ModelReport URL validation
    home_page.go_to_modelReports()
    actual_modelReportsPageurl = home_page.get_current_url()
    expected_modelReportsPageurl=test_data["ModelReportsPage_URL"]

    check.equal(actual_modelReportsPageurl, expected_modelReportsPageurl, f"URL mismatch: Expected '{expected_modelReportsPageurl}', but got '{actual_modelReportsPageurl}'")
    print(f"➡️ Validating URL: Expected='{expected_modelReportsPageurl}', Actual='{actual_modelReportsPageurl}'")


    # AboutPage URL validation
    home_page.go_to_about()
    actual_aboutPage_url=home_page.get_current_url()
    expected_aboutPage_url=test_data["AboutPage_URL"]

    check.equal(actual_aboutPage_url, expected_aboutPage_url, f"Text mismatch: Expected '{expected_aboutPage_url}', but got '{actual_aboutPage_url}'")
    print(f"➡️ Validating URL: Expected='{expected_aboutPage_url}', Actual='{actual_aboutPage_url}'")

    # SupportPage validation
    home_page.go_to_support()
    actual_headerText=home_page.verify_supportPage_header()
    expected_headerText = test_data["SupportPage_header"]

    check.equal(actual_headerText, expected_headerText, f"Text mismatch: Expected '{expected_headerText}', but got '{actual_headerText}'")
    print(f"➡️ Validating Text: Expected='{expected_headerText}', Actual='{actual_headerText}'")