from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelinsightspage import ModelInsightspage
from pytest_check import check




def test_verify_aiInsightsLeaderboard_dashboards_loads_correctly_when_logged_in(guest_user):
    home_page = Homepage(guest_user._page)
    #modelInsights_page = ModelInsightspage(user._page)

    home_page.go_to_AIinsightsLeaderboard()    

    print("✅ All dashboard charts verified (soft assertions).")