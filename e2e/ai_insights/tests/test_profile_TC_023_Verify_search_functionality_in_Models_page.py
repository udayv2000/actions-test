from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.profilepage import ProfilePage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_search_functionality_in_Models_page(guest_user):
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


    # Model search
    actual_model_appeared = profile_page.verify_model_search_functionality(created_model_name)

    check.equal(actual_model_appeared, created_model_name, f"Model mismatch: Expected '{created_model_name}', but got '{actual_model_appeared}'")
    print(f"➡️ Validating model: Expected='{created_model_name}', Actual='{actual_model_appeared}'")

    # Delete Model
    actual_model_delete_status = profile_page.delete_model(created_model_name)

    check.equal(actual_model_delete_status, True, f"failed to delete model: Expected '{"True"}', but got '{actual_model_delete_status}'")
    print(f"➡️ is new Model Deleted : Expected='{"True"}', Actual='{actual_model_delete_status}'")