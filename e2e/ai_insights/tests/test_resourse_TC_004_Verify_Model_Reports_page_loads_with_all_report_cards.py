from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage

def test_Verify_Model_Reports_page_loads_with_all_report_cards(guest_user):
    home_page = Homepage(guest_user._page)
    ModelReport_page=ModelReportpage(guest_user._page)

    home_page.go_to_modelReport()
    ModelReport_page.verify_all_model_cards_are_displayed()