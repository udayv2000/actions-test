from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
import logging
from utils.excel_reader import read_test_data


#logger = logging.getLogger(__name__)
def test_Verify_Page_Loads_with_All_Elements_and_Correct_Content(guest_user):
    home_page = Homepage(guest_user._page)

    test_data = read_test_data(sheet_name="HomePage", parent_tcid="TC_002", data_tcid="TC_002_01")

    # URL validation
    expected_homePage_url = test_data["HomePage_URL"]
    actual_homePage_url = home_page.get_current_url()
    print(f"➡️ Validating URL: Expected='{expected_homePage_url}', Actual='{actual_homePage_url}'")
    check.equal(actual_homePage_url, expected_homePage_url, f"URL mismatch: Expected '{expected_homePage_url}', but got '{actual_homePage_url}'")

    
    # Homepage title validation
    actual_homepage_title = home_page.get_page_tittle()
    expected_homePage_title = test_data["HomePage_title"]
    print(f"➡️ Validating Homepage title: Expected='{expected_homePage_title}', Actual='{actual_homepage_title}'")
    check.equal(actual_homepage_title, expected_homePage_title, f"URL mismatch: Expected '{expected_homePage_title}', but got '{actual_homepage_title}'")
    

    # Logo validation
    is_logo_present = home_page.verify_logo()
    check.is_true(is_logo_present, "Logo not visible")
    print(f"➡️ AI Insights Logo is present on the HomePage: {is_logo_present}")

    # Verify Main Heading
    actual_main_heading_text = home_page.verify_Main_heading()
    expected_main_heading_text = test_data["Main_Heading"]
    print(f"➡️ Validating Homepage main heading: Expected='{expected_main_heading_text}', Actual='{actual_main_heading_text}'")
    check.equal(actual_main_heading_text, expected_main_heading_text, f"URL mismatch: Expected '{expected_main_heading_text}', but got '{actual_main_heading_text}'")


    

   