from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.educationpage import educationpage


def test_Public_Education_Article_Without_Login(guest_user):
    home_page = Homepage(guest_user._page)
    education_page= educationpage(guest_user._page)

    home_page.go_to_education()
    education_page.verify_Public_Education_Article_Without_Login()