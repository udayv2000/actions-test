from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_all_Reports_links_directs_to_appropriate_pages(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_009", data_tcid="TC_009_01")

    home_page.go_to_footer()

    # ModelReport URL validation from footer
    home_page.click_modelReport_link_from_footer()
    actual_modelReportPage_URL=home_page.get_current_url()
    expected_modelReportPage_URL= test_data["FooterModelReportsPage_URL"]
    check.equal(actual_modelReportPage_URL, expected_modelReportPage_URL, f"URL mismatch: Expected '{expected_modelReportPage_URL}', but got '{actual_modelReportPage_URL}'")
    print(f"➡️ Validating URL: Expected='{expected_modelReportPage_URL}', Actual='{actual_modelReportPage_URL}'")