import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def get_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    page.close()
    browser.close()
    playwright.stop()
