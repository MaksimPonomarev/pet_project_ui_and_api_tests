import os
import time
from ui.pages.main_page import MainPage


def test_check_accept_cookie_banner(main_page_without_context):
    main_page_without_context.open()
    main_page_without_context.should_be_cookie_banner()
    main_page_without_context.accept_cookie_banner()
    main_page_without_context.should_be_login_link_enable()


def test_check_site_header(main_page):
    main_page.open()
    main_page.should_be_head_of_site()


def test_guest_can_go_to_login(main_page, login_page):
    main_page.open()
    main_page.go_to_login()
    login_page.should_be_logged_out()
    login_page.check_url()