from playwright.sync_api import Page
from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.logout import LogoutPage
from pytest_check import check
from utils.excel_reader import read_test_data





def test_verify_latticeflow_stg_environment_load_successfully(page: Page):
    home_page = Homepage(page)
    logout_page = LogoutPage(page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    url = test_data["URL"]
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]
    page.goto(url)
    home_page.login_Super_Admin(mail, pwd)
    home_page.logout_SuperAdmin()