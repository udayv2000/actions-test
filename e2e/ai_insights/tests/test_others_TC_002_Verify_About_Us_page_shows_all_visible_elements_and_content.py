from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.aboutpage import Aboutpage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_others_Verify_About_Us_page_shows_all_visible_elements_and_content(guest_user):
    home_page = Homepage(guest_user._page)
    about_page = Aboutpage(guest_user._page)

    test_data = read_test_data(sheet_name="AboutPage", parent_tcid="TC_002", data_tcid="TC_002_01")

    home_page.go_to_footer()
    home_page.click_about_link_footer()

    # verify latticeFlow tagline
    actual_latticeFlow_tagline_text = about_page.get_latticeFlow_tagline_text()
    expected_latticeFlow_tagline_text = test_data["LatticeFlow_tagline"]

    check.equal(actual_latticeFlow_tagline_text, expected_latticeFlow_tagline_text, f"Text mismatch: Expected '{expected_latticeFlow_tagline_text}', but got '{actual_latticeFlow_tagline_text}'")
    print(f"➡️ Validating tagline: Expected='{expected_latticeFlow_tagline_text}', Actual='{actual_latticeFlow_tagline_text}'")

    # verify latticeFlow URL
    actual_link, latticeFlow_main_url = about_page.validate_link_functionality()
    expected_link = test_data["LatticeFlow_link"]
    
    check.equal(actual_link, expected_link, f"Text mismatch: Expected '{expected_link}', but got '{actual_link}'")
    print(f"➡️ Validating tagline: Expected='{expected_link}', Actual='{actual_link}'")

    check.is_in(expected_link, latticeFlow_main_url, f"URL mismatch: Expected '{expected_link}', but got '{latticeFlow_main_url}'")
    print(f"➡️ Validating URL: Expected='{expected_link}', Actual='{latticeFlow_main_url}'")