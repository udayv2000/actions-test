from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data



def test_User_Management_page_loads_correctly(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)

    created_Organization_name = profile_page.Create_a_new_Organization()

    check.is_true(
        created_Organization_name is not False,
        f"Organization creation failed. Expected a Organization name, got: {created_Organization_name}"
    )
    print(f"➡️ Organization created successfully: '{created_Organization_name}'")


    profile_page.click_on_user_icon_from_Ororganization(created_Organization_name)
    table_headers = profile_page.get_user_table_headers()  # ← Now logs beautifully!
    check.equal(len(table_headers), 9, "Expected exactly 9 user table columns")