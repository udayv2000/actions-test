from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_Account_page_loads_correctly_for_Super_Admin(guest_user):
    home_page = Homepage(guest_user._page)
    

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)
    
    visibility = home_page.verify_Account_Page_Loads_For_SuperAdmin()

    # Separate into visible and not visible
    visible_fields = [field for field, is_visible in visibility.items() if is_visible]
    invisible_fields = [field for field, is_visible in visibility.items() if not is_visible]

    # Print detailed report (visible in console and HTML report)
    print("\n🔍 Account Visibility Report:")
    print("✅ Visible fields:", visible_fields)
    print("❌ Not visible fields:", invisible_fields)

    # Soft assert each one with meaningful message
    for field_name, is_visible in visibility.items():
        check.is_true(is_visible, f"Field '{field_name}' is NOT visible!")