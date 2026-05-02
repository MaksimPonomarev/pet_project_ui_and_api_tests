import pytest
from playwright.sync_api import sync_playwright
from ui.pages.main_page import MainPage


@pytest.fixture
#создает готовую главную страницу
def main_page(get_page_with_context):
    page = MainPage(get_page_with_context)
    page.open()
    return page


@pytest.fixture
#создает готовую главную страницу с куки баннером
def main_page_without_context(get_page_without_context):
    page = MainPage(get_page_without_context)
    page.open()
    return page


@pytest.fixture
def signup_page(get_page_with_context):

