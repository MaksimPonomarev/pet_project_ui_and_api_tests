import time

import pytest


@pytest.fixture
def create_account(login_page, signup_page, created_account_page):
    login_page.open()
    get_signup_data = login_page.go_to_signup()
    get_create_account_data = signup_page.create_user(signup_data=get_signup_data)
    created_account_page.click_continue()
    return get_create_account_data


@pytest.fixture
def create_account_and_logout(create_account, main_page, login_page):
    main_page.logout()
    login_page.go_to_home()
    return create_account

