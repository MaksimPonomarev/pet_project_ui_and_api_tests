import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def get_page_with_context(request):
    #фикстура для создания браузера с контекстом
    with sync_playwright() as p:
        headless = request.config.getoption("--headless")
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(storage_state="./ui/storage_state.json")
        page = context.new_page()
        page.set_default_timeout(15000)
        try:
            yield page
        finally:
            page.close()
            context.close()
            browser.close()


@pytest.fixture
def get_page_without_context(request):
    #фикстура для создания браузера без контекста
    with sync_playwright() as p:
        headless = request.config.getoption("--headless")
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(15000)
        try:
            yield page
        finally:
            page.close()
            context.close()
            browser.close()
