from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_the_Resources_drop_down_and_links_redirects_to_appropriate_urls(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_003", data_tcid="TC_003_01")

    
    home_page.go_to_education()
    actual_educationPageurl = home_page.get_current_url()
    expected_educationPageurl = test_data["EducationPage_URL"]
    check.equal(actual_educationPageurl, expected_educationPageurl, f"URL mismatch: Expected '{expected_educationPageurl}', but got '{actual_educationPageurl}'")
    print(f"➡️ Validating URL: Expected='{expected_educationPageurl}', Actual='{actual_educationPageurl}'")

    home_page.go_to_modelReport()
    actual_modelReportPageurl = home_page.get_current_url()
    expected_modelReportPageurl = test_data["ModelReportsPage_URL"]
    check.equal(actual_modelReportPageurl, expected_modelReportPageurl, f"URL mismatch: Expected '{expected_modelReportPageurl}', but got '{actual_modelReportPageurl}'")
    print(f"➡️ Validating URL: Expected='{expected_modelReportPageurl}', Actual='{actual_modelReportPageurl}'")

    home_page.go_to_press()
    # Now get URL from the NEW tab
    new_tab = home_page._current_popup_page
    actual_press_url = new_tab.url  # <-- This is the new tab's URL
    expected_pressPageurl=test_data["PressPage_URL"]
    check.is_in(expected_pressPageurl, actual_press_url, f"URL mismatch: Expected '{expected_pressPageurl}', but got '{actual_press_url}'")
    print(f"➡️ Validating URL: Expected='{expected_pressPageurl}', Actual='{actual_press_url}'")
    
    

