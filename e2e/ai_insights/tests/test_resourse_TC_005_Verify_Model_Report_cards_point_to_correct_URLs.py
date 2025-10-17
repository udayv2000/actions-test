from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
import pytest


#@pytest.mark.xfail(reason="Bug not fixed yet")
@pytest.mark.skip(reason="Bug not fixed yet, test is invalid until then")
def test_Verify_Model_Report_cards_point_to_correct_URLs(guest_user):
    home_page = Homepage(guest_user._page)
    ModelReport_page=ModelReportpage(guest_user._page)

    home_page.go_to_modelReport()
    ModelReport_page.verify_cards_open_correct_page()