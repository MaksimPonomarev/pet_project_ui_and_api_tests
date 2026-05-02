import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def get_page_with_context():
    #фикстура для создания браузера с контекстом
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="./ui/storage_state.json")
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()


@pytest.fixture
def get_page_without_context():
    #фикстура для создания браузера без контекста
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()

