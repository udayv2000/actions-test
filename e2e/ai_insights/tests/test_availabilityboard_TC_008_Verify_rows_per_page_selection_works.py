from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check


def test_Verify_rows_per_page_selection_works(user):
    home_page = Homepage(user._page)
    availabilityboard_Page = AvailabilityBoardPage(user._page)

    home_page.go_to_modelReports()