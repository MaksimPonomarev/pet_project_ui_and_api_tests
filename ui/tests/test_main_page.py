import time
from ui.pages.main_page import MainPage


def test_check_accept_cookie_banner(main_page_without_context):
    main_page_without_context.should_be_cookie_banner()
    main_page_without_context.accept_cookie_banner()
    main_page_without_context.should_be_login_link_enable()


def test_check_site_header(main_page):
    main_page.should_be_head_of_site()


def test_user_can_go_to_login(main_page):
    main_page.go_to_login()
    should