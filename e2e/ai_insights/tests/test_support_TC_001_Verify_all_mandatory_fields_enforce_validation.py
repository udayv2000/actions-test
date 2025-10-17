from latticeflow.e2e.pages.homepage import Homepage

def test_Verify_all_mandatory_fields_enforce_validation(guest_user):
    home_page = Homepage(guest_user._page)

    home_page.go_to_support()
