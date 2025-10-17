from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.educationpage import educationpage

def test_Verify_Education_page_loads_with_all_cards_by_default(guest_user):
    home_page = Homepage(guest_user._page)
    education_page= educationpage(guest_user._page)

    home_page.go_to_education()
    education_page.verify_cards_are_displayed()
    
