import pytest
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.signup_page import SignupPage


@pytest.fixture
#создает готовую главную страницу
def main_page(get_page_with_context):
    page = MainPage(get_page_with_context)
    return page


@pytest.fixture
#создает готовую главную страницу с куки баннером
def main_page_without_context(get_page_without_context):
    page = MainPage(get_page_without_context)
    return page


@pytest.fixture
def signup_page(get_page_with_context):
    page = SignupPage(get_page_with_context)
    return page

@pytest.fixture
def login_page(get_page_with_context):
    page = LoginPage(get_page_with_context)
    return page
