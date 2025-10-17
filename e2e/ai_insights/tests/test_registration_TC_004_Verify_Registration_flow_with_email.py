from latticeflow.e2e.pages.registrationpage import RegistrationPage
from pytest_check import check
from utils.excel_reader import read_test_data

def test_Verify_Registration_flow_with_email(guest_user):
    registration_page = RegistrationPage(guest_user._page)

    registration_status = registration_page.user_registration(fill_job_title=True, fill_company=True, check_tos=True, check_marketing=True)

    print("User registration data:", registration_status)

    # 🔍 Soft assertion: don't stop here if it fails
    with check:
        assert registration_status["success"] is True, \
            f"Registration failed: {registration_status['message']}"