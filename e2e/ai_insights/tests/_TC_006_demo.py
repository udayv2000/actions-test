# test_demo.py
from latticeflow.e2e.pages.landingpage import LandingPage

def test_validate_all_cards(user):  # `user` fixture triggers login/logout
    landing_page = LandingPage(user._page)  # assuming `User` class has `.page` or `_page`
    landing_page.click_all_cards()

