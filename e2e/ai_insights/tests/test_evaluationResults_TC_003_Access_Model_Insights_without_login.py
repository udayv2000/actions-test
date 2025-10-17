from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelinsightspage import ModelInsightspage
from pytest_check import check

def test_Access_Model_Insights_without_login(guest_user):
    home_page = Homepage(guest_user._page)
    modelInsights_page = ModelInsightspage(guest_user._page)

    home_page.go_to_modelInsights()
    actual_status = modelInsights_page.is_login_or_register_prompt_visible()

    check.equal(actual_status, True, f"is Register or Login Card visible: Expected '{"True"}', but got '{actual_status}'")
    print(f"➡️ is Register or Login Card visible : Expected='{"True"}', Actual='{actual_status}'")