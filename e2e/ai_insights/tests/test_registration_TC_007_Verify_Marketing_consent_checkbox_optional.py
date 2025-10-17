from latticeflow.e2e.pages.registrationpage import RegistrationPage
from pytest_check import check

def test_Verify_Marketing_consent_checkbox_optional(guest_user):
    registration_page = RegistrationPage(guest_user._page)

    registration_status = registration_page.user_registration(fill_job_title=False, fill_company=False, check_tos=True, check_marketing=False)

    print("User registration data:", registration_status)

    # 🔍 Soft assertion: don't stop here if it fails
    with check:
        assert registration_status["success"] is True, \
            f"Registration failed: {registration_status['message']}"