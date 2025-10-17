from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check

def test_erify_social_login_buttons_are_visible(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    # Click on login button
    home_page.open_login()

    # Get visibility status of all social login buttons
    visibility = login_page.is_social_login_buttons_visible()

    # Separate into visible and not visible
    visible_fields = [field for field, is_visible in visibility.items() if is_visible]
    invisible_fields = [field for field, is_visible in visibility.items() if not is_visible]

    # Print detailed report (visible in console and HTML report)
    print("\n🔍 Registration Page Field Visibility Report:")
    print("✅ Visible fields:", visible_fields)
    print("❌ Not visible fields:", invisible_fields)

    # Soft assert each one with meaningful message
    for field_name, is_visible in visibility.items():
        check.is_true(is_visible, f"Field '{field_name}' is NOT visible!")