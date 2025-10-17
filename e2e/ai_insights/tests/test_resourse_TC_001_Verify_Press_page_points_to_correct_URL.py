from latticeflow.e2e.pages.homepage import Homepage
from utils.excel_reader import read_test_data

def test_Verify_Press_page_points_to_correct_URL_guest(guest_user):
    # Create homepage object with the guest user's page
    home_page = Homepage(guest_user._page)
    
    # Navigate to Press page
    home_page.go_to_press()

    # Get current URL
    current_url = guest_user._page.url
    print(f"Current URL: {current_url}")  # Debugging

    # Expected URL
    test_data = read_test_data(sheet_name="ResoursePage", parent_tcid="TC_001", data_tcid="TC_001_01")
    expected_url = test_data["homePage_url"]
    print(f"Expected URL: {expected_url}")

    # Assertion
    assert current_url == expected_url, \
        f"Expected Press page URL '{expected_url}', but got '{current_url}'"
