from ui.pages.helpers.main_page_helper import should_be_cookie_banner, accept_cookie_banner, should_be_login_link_enable
from ui.pages.main_page import MainPage


def test_check_accept_cookie_banner(get_page):
    main_page = MainPage(get_page)
    main_page.open()

    should_be_cookie_banner(get_page)
    accept_cookie_banner(get_page)
    should_be_login_link_enable(get_page)




