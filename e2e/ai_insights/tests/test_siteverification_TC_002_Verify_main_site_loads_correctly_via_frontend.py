from playwright.sync_api import Page
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_main_site_loads_correctly_via_frontend(page: Page):
    
    test_data = read_test_data(sheet_name="SiteVerification", parent_tcid="TC_002", data_tcid="TC_002_01")
    prod_url = test_data["Prod URL"]

    # Navigate directly to the backend URL
    page.goto(prod_url, wait_until="domcontentloaded")

    assert prod_url in page.url, f"Expected URL {prod_url}, but got {page.url}"