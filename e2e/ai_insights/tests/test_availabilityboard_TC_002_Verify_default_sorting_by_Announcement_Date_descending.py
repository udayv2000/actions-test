from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.availabilityboardpage import AvailabilityBoardPage
from pytest_check import check


def test_Verify_default_sorting_by_Announcement_Date_descending(guest_user):
    home_page = Homepage(guest_user._page)
    availabilityboard_Page = AvailabilityBoardPage(guest_user._page)

    home_page.go_to_modelReports()

    is_sorted_correctly = availabilityboard_Page.verify_sorting_by_announced_date_descending()
    check.is_true(
        is_sorted_correctly,
        "Model Reports are not sorted by Announced Date in descending order."
    )
    print("✅ Test Passed: Reports sorted by Announced Date (newest first)")