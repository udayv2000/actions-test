from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from utils.excel_reader import read_test_data

def test_Verify_the_Resources_drop_down_and_links_redirects_to_appropriate_urls(guest_user):

    home_page = Homepage(guest_user._page)
    ModelReport_page=ModelReportpage(guest_user._page)

    home_page.go_to_education()
    expeted_modelreportpage_tittle = "Model Reports | LatticeFlow AI Insights - Evaluate Foundation Model Readiness"
   
    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")
    print("📊 Test Data Loaded from Excel:")
    print(test_data)  # This will show all key-value pairs
    #actual_modelreportpage_tittle=ModelReport_page.verify_modelReportpage()
    #print(f"✅ Actual Model Reports page title: {actual_modelreportpage_tittle}")
    #print(f"✅ Expected Model Reports page title: {expeted_modelreportpage_tittle}")