from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Delete_User_functionality_works_as_expected(guest_user):
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

    created_User_name = profile_page.add_user_from_action_tab_from_organization()

    check.is_true(
        created_User_name is not False,
        f"User creation failed. Expected a User name, got: {created_User_name}"
    )
    print(f"➡️ User created successfully: '{created_User_name}'")


    # Delete User
    actual_deleted_status = profile_page.delete_user()

    check.equal(actual_deleted_status, True, f"User mismatch: Expected '{"True"}', but got '{actual_deleted_status}'")
    print(f"➡️ is new User deleted : Expected='{"True"}', Actual='{actual_deleted_status}'")