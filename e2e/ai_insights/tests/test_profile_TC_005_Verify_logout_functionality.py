from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.logout import LogoutPage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_logout_functionality(guest_user):
    home_page = Homepage(guest_user._page)
    logout_page = LogoutPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)
    home_page.logout_SuperAdmin()

    print("Logout sucessful")

