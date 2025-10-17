from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_Normal_User_menu_shows_limited_options(guest_user):
    home_page = Homepage(guest_user._page)
    login_page = LoginPage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    login_page.click_login_btn()
    home_page.login_user(mail, pwd)

    visibility = home_page.verify_Limited_Menu_Options_For_Normal_User()

    # Separate into visible and not visible
    visible_fields = [field for field, is_visible in visibility.items() if is_visible]
    invisible_fields = [field for field, is_visible in visibility.items() if not is_visible]

    # Print detailed report (visible in console and HTML report)
    print("\n🔍 Account Field Visibility Report:")
    print("✅ Visible fields:", visible_fields)
    print("❌ Not visible fields:", invisible_fields)

    # Soft assert each one with meaningful message
    for field_name, is_visible in visibility.items():
        check.is_true(is_visible, f"Field '{field_name}' is NOT visible!")