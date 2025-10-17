from contextlib import contextmanager
from typing import Generator

import pytest
from playwright.sync_api import BrowserContext, Page
from latticeflow.e2e.actions.user import User

# 🔹 Import your data reader
from utils.excel_reader import read_test_data

# 🔹 Increase timeout to 30 seconds globally if needed
DEFAULT_TIMEOUT = 60*1000



# 🔹 Base URL
#AI_INSIGHTS_URL = test_data["AI_INSIGHTS_URL"].strip()



def _configure_page(page: Page) -> Page:
    """Apply default Playwright settings to a page."""
    page.set_default_timeout(DEFAULT_TIMEOUT)
    # Optional: set viewport if needed
    # page.set_viewport_size({"width": 1200, "height": 800})
    return page


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    """Base Playwright page fixture."""
    return _configure_page(context.new_page())


# ----------------- TEST FIXTURES -----------------

@pytest.fixture()
def guest_user(page: Page) -> User:
    """Guest user — stays on landing page without login."""
    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")
    AI_INSIGHTS_URL = test_data["URL"].strip()
    page.goto(AI_INSIGHTS_URL, wait_until="domcontentloaded")
    return User(page)
    


@pytest.fixture()
def user(page: Page) -> Generator[User, None, None]:
    """Authenticated user — login before test, logout after."""
    with _login_user(page) as u:
        yield u
        
# @pytest.fixture()
# def logged_in_user(page: Page) -> Generator[User, None, None]:
#     """Authenticated user — login before test, logout after."""
#     with _login_user(page) as u:
#         yield u

# ----------------- INTERNAL HELPERS -----------------

@contextmanager
def _login_user(page: Page) -> Generator[User, None, None]:
    """Context manager to handle login + logout."""
    test_data = read_test_data(sheet_name="LoginData", parent_tcid="ENVIRONMENT", data_tcid="Test")
    usermail=test_data["EMAIL"].strip()
    userpwd=test_data["PASSWORD"].strip()
    AI_INSIGHTS_URL=test_data["URL"].strip()
    email = usermail
    password = userpwd
    user = User(page)

    # Go to landing page
    page.goto(AI_INSIGHTS_URL, timeout=DEFAULT_TIMEOUT, wait_until="domcontentloaded")

    # Perform login
    user.login(email, password)

    yield user

    # Perform logout
    user.logout()
