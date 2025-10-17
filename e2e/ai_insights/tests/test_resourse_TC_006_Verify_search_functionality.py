from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.modelReportpage import ModelReportpage
from latticeflow.e2e.pages.educationpage import educationpage
from utils.excel_reader import read_test_data

def test_Verify_search_functionality(guest_user):
    home_page = Homepage(guest_user._page)
    ModelReport_page=ModelReportpage(guest_user._page)
    education_page= educationpage(guest_user._page)
    

    home_page.go_to_modelReport()

    test_data = read_test_data(sheet_name="ResoursePage", parent_tcid="TC_006", data_tcid="TC_006_01")
    expected_text = test_data["card_text"]
    #expected_text ="DeepSeek R1 AI Model Risk Report"
    actual_text  = ModelReport_page.verify_model_report_search_field(expected_text)

    # Print both expected and actual for debugging
    print(f"\nExpected text: '{expected_text}'")
    print(f"Actual text:   '{actual_text}'")
    
    # Verify the text matches (case-sensitive exact match)
    assert actual_text == expected_text, \
        f"Text mismatch.\nExpected: '{expected_text}'\nActual: '{actual_text}'"
    
    home_page.go_to_education()
    expected_text1=test_data["education_card_text"]
    #expected_text1="Compl AI"
    actual_text1=education_page.verify_education_report_search_field(expected_text1)

    # Print both expected and actual for debugging
    print(f"\nExpected text: '{expected_text1}'")
    print(f"Actual text:   '{actual_text1}'")
    
    # Verify the text matches (case-sensitive exact match)
    assert actual_text1 == expected_text1, \
        f"Text mismatch.\nExpected: '{expected_text1}'\nActual: '{actual_text1}'"
    
