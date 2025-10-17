from latticeflow.e2e.pages.homepage import Homepage


def test_Verify_user_receives_confirmation_email(guest_user):
    home_page = Homepage(guest_user._page)

    home_page.go_to_support()