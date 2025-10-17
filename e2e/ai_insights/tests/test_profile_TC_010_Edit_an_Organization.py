from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Edit_an_Organization(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)

    # Create new org
    created_Organization_name = profile_page.Create_a_new_Organization()

    check.is_true(
        created_Organization_name is not False,
        f"Organization creation failed. Expected a Organization name, got: {created_Organization_name}"
    )
    print(f"➡️ Organization created successfully: '{created_Organization_name}'")

    # Edit new org
    actual_edit_status=profile_page.edit_organization(created_Organization_name)

    check.equal(actual_edit_status, True, f"Organization mismatch: Expected '{"True"}', but got '{actual_edit_status}'")
    print(f"➡️ is Organization edited : Expected='{"True"}', Actual='{actual_edit_status}'")

    # Delete new org
    actual_deleted_status = profile_page.delete_organization(created_Organization_name)

    check.equal(actual_deleted_status, True, f"Organization mismatch: Expected '{"True"}', but got '{actual_deleted_status}'")
    print(f"➡️ is new Organization deleted : Expected='{"True"}', Actual='{actual_deleted_status}'")