from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check


def test_Verify_search_functionality(guest_user):
    home_page = Homepage(guest_user._page)
    availabilityboard_Page = AvailabilityBoardPage(guest_user._page)
    

    home_page.go_to_modelReports()
    availabilityboard_Page.verify_search_functionality("Gemini 2.5 Pro")