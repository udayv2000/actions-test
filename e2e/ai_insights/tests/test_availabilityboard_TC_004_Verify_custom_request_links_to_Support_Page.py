from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check

def test_availabilityboard_Verify_custom_request_links_to_Support_Page(guest_user):
    home_page = Homepage(guest_user._page)
    availabilityboard_Page = AvailabilityBoardPage(guest_user._page)

    home_page.go_to_modelReports()
    availabilityboard_Page.verify_search_functionality("Gemini 2.5 Pro")

    actual_text = availabilityboard_Page.Verify_custom_request_links_to_Support_Page()
    print(f"   Custom Request text: {actual_text}")

    check.equal(actual_text, "Custom Request", f"Text mismatch: Expected '{"Custom Request"}', but got '{actual_text}'")
    print(f"➡️  Support Page Opened  : Expected='{"Custom Request"}', Actual='{actual_text}'")