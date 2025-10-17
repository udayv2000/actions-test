from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelinsightspage import ModelInsightspage
from latticeflow.e2e.pages.login import LoginPage
from pytest_check import check

def test_login_TC_013_Verify_gated_content_prompt_for_Superset_dashboard(guest_user):
    home_page = Homepage(guest_user._page)
    modelinsights_page = ModelInsightspage(guest_user._page)

    home_page.go_to_modelInsights()

    visibility = modelinsights_page.is_login_or_register_prompt_visible()

    check.equal(visibility, True, f"is Register or Login Card visible: Expected '{"True"}', but got '{visibility}'")
    print(f"➡️ is Register or Login Card visible : Expected='{"True"}', Actual='{visibility}'")