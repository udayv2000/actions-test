from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data


def test_Delete_a_Model(guest_user):
    home_page = Homepage(guest_user._page)
    profile_page = ProfilePage(guest_user._page)

    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Super_Admin")
    mail = test_data["EMAIL"]
    pwd = test_data["PASSWORD"]

    home_page.login_Super_Admin(mail, pwd)  

    # Create Model
    created_model_name = profile_page.Create_model()

    check.is_true(
        created_model_name is not False,
        f"Model creation failed. Expected a model name, got: {created_model_name}"
    )
    print(f"➡️ Model created successfully: '{created_model_name}'")



    # Edit Model
    actual_edit_status = profile_page.edit_model(created_model_name)

    check.equal(actual_edit_status, True, f"failed to edit model: Expected '{"True"}', but got '{actual_edit_status}'")
    print(f"➡️ is new Model Edited : Expected='{"True"}', Actual='{actual_edit_status}'")



    # Delete Model
    actual_model_delete_status = profile_page.delete_model(created_model_name)

    check.equal(actual_model_delete_status, True, f"failed to delete model: Expected '{"True"}', but got '{actual_model_delete_status}'")
    print(f"➡️ is new Model Deleted : Expected='{"True"}', Actual='{actual_model_delete_status}'")