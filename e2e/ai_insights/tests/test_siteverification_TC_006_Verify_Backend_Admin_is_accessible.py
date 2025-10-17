from playwright.sync_api import Page
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Verify_Backend_Admin_is_accessible(page: Page):
    test_data = read_test_data(sheet_name="SiteVerification", parent_tcid="TC_006", data_tcid="TC_006_01")
    backend_url = test_data["Backend URL"]

    # Navigate directly to the backend URL
    page.goto(backend_url, wait_until="domcontentloaded")

    assert backend_url in page.url, f"Expected URL {backend_url}, but got {page.url}"
    