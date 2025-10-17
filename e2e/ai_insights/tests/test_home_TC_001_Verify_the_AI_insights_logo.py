from latticeflow.e2e.pages.homepage import Homepage
#from utils.excel_reader import read_test_data

def test_Verify_logo(guest_user):
    home_page = Homepage(guest_user._page)

    is_logo_present = home_page.verify_logo()

    assert is_logo_present, "AI Insights logo is NOT visible on the homepage"
    
    print(f"AI Insights Logo is present on the HomePage: {is_logo_present}")