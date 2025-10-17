from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check


def test_Verify_Model_Reports_tab_loads_correctly(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    home_page.go_to_modelReports()
    table_headers = profile_page.get_user_table_headers()  # ← Now logs beautifully!
    check.equal(len(table_headers), 8, "Expected exactly 8 availabilityBoard table columns")