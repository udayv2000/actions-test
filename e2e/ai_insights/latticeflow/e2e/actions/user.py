from __future__ import annotations

from playwright.sync_api import Page

from latticeflow.e2e.pages.homepage import Homepage
from latticeflow.e2e.pages.login import LoginPage
from latticeflow.e2e.pages.logout import LogoutPage



class User:
    def __init__(self, page: Page) -> None:
        self._page = page
        self._homepage = Homepage(page)
        self._login_page = LoginPage(self._page)
        self._logout_page = LogoutPage(self._page)

    def login(self, email: str, password: str) -> None:
        self._homepage.open_login()
        self._login_page.login_user(email=email, password=password)

    def verify_login_successful(self) -> None:
        self._homepage.verify_user_logged_in()

    def logout(self) -> None:
        self._logout_page.logout_user()
