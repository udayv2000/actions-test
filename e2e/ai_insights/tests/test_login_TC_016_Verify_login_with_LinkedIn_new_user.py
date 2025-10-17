from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_login_with_LinkedIn_new_user(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginPage", parent_tcid="TC_016", data_tcid="TC_016_01")

    expected_homepage_URL= test_data["HomePage_URL"].strip()
    expected_mail= test_data["Linkedin_Mail"].strip()
    expected_password= test_data["Linkedin_Password"].strip()


    # Click on login button
    home_page.open_login()  

    actual_latticeflow_url = login_page.verify_login_with_linkedin(expected_mail,expected_password,expected_homepage_URL)
    check.equal(actual_latticeflow_url, expected_homepage_URL, f"URL mismatch: Expected '{expected_homepage_URL}', but got '{actual_latticeflow_url}'")
    print(f"➡️ Validating URL: Expected='{expected_homepage_URL}', Actual='{actual_latticeflow_url}'")