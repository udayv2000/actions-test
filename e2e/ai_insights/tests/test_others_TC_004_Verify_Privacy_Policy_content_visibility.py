from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.aboutpage import Aboutpage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_Privacy_Policy_content_visibility(guest_user):
    home_page = Homepage(guest_user._page)
    about_page = Aboutpage(guest_user._page)

    test_data = read_test_data(sheet_name="AboutPage", parent_tcid="TC_004", data_tcid="TC_004_01")

    home_page.go_to_footer()
    home_page.click_privacyPolicy_link_footer()