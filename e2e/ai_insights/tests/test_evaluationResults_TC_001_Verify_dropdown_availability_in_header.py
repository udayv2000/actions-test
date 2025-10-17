from latticeflow.e2e.pages.homepage import Homepage
from pytest_check import check

def test_Verify_dropdown_availability_in_header(guest_user):
    home_page = Homepage(guest_user._page)

    # Get visibility status of all fields
    visibility = home_page.verify_evaluationResults_dropdown()

    # Separate into visible and not visible
    visible_fields = [field for field, is_visible in visibility.items() if is_visible]
    invisible_fields = [field for field, is_visible in visibility.items() if not is_visible]

    # Print detailed report (visible in console and HTML report)
    print("\n🔍 Evaluation Results Visibility Report:")
    print("✅ Visible fields:", visible_fields)
    print("❌ Not visible fields:", invisible_fields)

    # Soft assert each one with meaningful message
    for field_name, is_visible in visibility.items():
        check.is_true(is_visible, f"Field '{field_name}' is NOT visible!")