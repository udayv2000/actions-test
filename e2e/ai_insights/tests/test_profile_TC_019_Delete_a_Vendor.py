from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Delete_a_Vendor(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)  

    # Create Vendor
    created_vendor_name = profile_page.create_vendors()

    check.is_true(
        created_vendor_name is not False,
        f"Vendor creation failed. Expected a Vendor name, got: {created_vendor_name}"
    )
    print(f"➡️ Vendor created successfully: '{created_vendor_name}'")



    # Edit Vendor
    actual_edit_status = profile_page.edit_vendors(created_vendor_name)

    check.equal(actual_edit_status, True, f"failed to edit vendor: Expected '{"True"}', but got '{actual_edit_status}'")
    print(f"➡️ is new vendor Edited : Expected='{"True"}', Actual='{actual_edit_status}'")



    # Delete Model
    actual_vendor_delete_status = profile_page.delete_vendors(created_vendor_name)

    check.equal(actual_vendor_delete_status, True, f"failed to delete vendor: Expected '{"True"}', but got '{actual_vendor_delete_status}'")
    print(f"➡️ is new vendor Deleted : Expected='{"True"}', Actual='{actual_vendor_delete_status}'")