import pytest


@pytest.fixture
def create_account(login_page, signup_page):
    login_page.open()
    get_email = login_page.go_to_signup()
    get_password = signup_page.create_user()
    signup_page.click_continue()
    return {**get_email, **get_password}