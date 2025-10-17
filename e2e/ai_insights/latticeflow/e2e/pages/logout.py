from playwright.sync_api import Page


class LogoutPage:
    def __init__(self, page: Page) -> None:
        self._page = page

        self._user_button = self._page.locator("xpath=(//*[name()='svg'][@role='presentation'])[13]")
        self._logout_button = self._page.locator("xpath=//span[normalize-space()='Logout']")

    def logout_user(self) -> None:
        #self._page.pause()
        self._page.wait_for_load_state("networkidle")
        self._user_button.click()
        self._logout_button.click()