from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.educationpage import educationpage


def test_Registered_Education_Article_After_Login(user):
    home_page = Homepage(user._page)
    education_page= educationpage(user._page)

    home_page.go_to_education()
    education_page.verify_Public_Education_Article_Without_Login()