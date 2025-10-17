from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from pytest_check import check



def test_Verify_Wiki_content_is_accessible_via_frontend(user):
     home_page = Homepage(user._page)
     modelReport_page = ModelReportpage(user._page)

     home_page.go_to_modelReport()

     is_loaded_status = modelReport_page.selected_article_loads_with_content()

     check.equal(is_loaded_status, True, f"failed to scroll: Expected '{"True"}', but got '{is_loaded_status}'")
     print(f"➡️ is Wiki content is accessible: Expected='{"True"}', Actual='{is_loaded_status}'")