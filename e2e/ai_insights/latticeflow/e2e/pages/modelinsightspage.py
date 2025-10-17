from playwright.sync_api import Page

class ModelInsightspage:
    def __init__(self, page: Page) -> None:
        self._page = page    

        self.registerORLogin_prompt = self._page.locator("//h2[text()='Register or Login']")


        # Evaluation Results Verification  TC-004
                        # Use src to find iframe
        self.iframe = page.frame_locator("iframe[src='https://superset-stage.aviaenterprises.in/embedded/8cdd90ba-e5bb-4aba-b188-3497ed98b300?uiConfig=9&expand_filters=false']")

                        # Define chart locators (inside iframe)
        self.chart_technical_robustness = self.iframe.locator("text=Technical Robustness and Safety")
        self.chart_privacy_governance = self.iframe.locator("text=Privacy & Data Governance")
        self.chart_transparency = self.iframe.locator("text=Transparency")
        self.chart_social_wellbeing = self.iframe.locator("text=Social & Environment Well-being")
        self.chart_accountability = self.iframe.locator("text=Diversity, Non-discrimination & Fairness")


    def is_login_or_register_prompt_visible(self): 
        self._page.wait_for_load_state("domcontentloaded")
        return self.registerORLogin_prompt.is_visible()  

    # Evaluation Results Verification  TC-004
    def wait_for_dashboard_to_load(self, timeout=10000):
        """Wait for key charts to appear inside iframe"""
        self.chart_technical_robustness.wait_for(state="visible", timeout=timeout)
        # Optionally wait for others — or just one is enough to confirm load  
         