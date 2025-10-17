from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelinsightspage import ModelInsightspage
from pytest_check import check

def test_verify_modelinsights_dashboards_loads_correctly_when_logged_in(user):
    home_page = Homepage(user._page)
    modelInsights_page = ModelInsightspage(user._page)

    home_page.go_to_modelInsights()

    # ✅ Wait for dashboard to load
    modelInsights_page.wait_for_dashboard_to_load()


    # ✅ SOFT ASSERTIONS — check all charts
    check.is_true(
        modelInsights_page.chart_technical_robustness.is_visible(),
        "Chart 'Technical Robustness and Safety' is not visible"
    )

    check.is_true(
        modelInsights_page.chart_privacy_governance.is_visible(),
        "Chart 'Privacy & Data Governance' is not visible"
    )

    check.is_true(
        modelInsights_page.chart_transparency.is_visible(),
        "Chart 'Transparency' is not visible"
    )

    check.is_true(
        modelInsights_page.chart_social_wellbeing.is_visible(),
        "Chart 'Social & Environment Well-being' is not visible"
    )

    check.is_true(
        modelInsights_page.chart_accountability.is_visible(),
        "Chart 'Accountability' is not visible"
    )

    print("✅ All dashboard charts verified (soft assertions).")


# def test_verify_aiInsightsLeaderboard_dashboards_loads_correctly_when_logged_in(user):
#     home_page = Homepage(user._page)
#     #modelInsights_page = ModelInsightspage(user._page)

#     home_page.go_to_AIinsightsLeaderboard()    

#     print("✅ All dashboard charts verified (soft assertions).")


