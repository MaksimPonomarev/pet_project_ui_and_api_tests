import re
import pytest
from playwright.sync_api import expect


def test_check_site_header(main_page):
    main_page.open()
    main_page.should_be_head_of_site()


def test_logout(main_page, create_account):
    main_page.should_be_logged_in()
    main_page.logout()
    main_page.should_be_logged_out()


def test_go_to_products_page(main_page, products_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_products()
    products_page.should_be_product_page()


def test_go_to_cart_page(main_page, cart_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_cart()
    cart_page.should_be_empty_cart()


def test_go_to_filled_cart_page(filled_cart, main_page,filled_cart_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_cart()
    filled_cart_page.should_be_filled_cart()


def test_go_to_login_page(main_page, login_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_login()
    login_page.should_be_login_page()


def test_go_to_test_cases_page(main_page, test_cases_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_test_cases()
    test_cases_page.should_be_test_cases_page()


def test_go_to_api_page(main_page, api_list_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_api_list()
    api_list_page.should_be_api_list_page()


def test_go_to_contact_us(main_page, contact_us_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_contact_us()
    contact_us_page.should_be_contact_us_page()


def test_go_to_video_tutorials(main_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_video_tutorials()
    expect(main_page.page).to_have_url(re.compile("youtube"))

def test_go_to_details_product_from_product_page(products_page, detail_products_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.open_product_card_detail()
    detail_products_page.should_be_product_detail_page()

def test_go_to_details_product_from_main_page(main_page, detail_products_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.open_product_card_detail()
    detail_products_page.should_be_product_detail_page()

@pytest.mark.parametrize("page_fixture", ["main_page", "cart_page"])
def test_check_footer(page_fixture, request):
    page = request.getfixturevalue(page_fixture)
    page.open()
    page.should_be_footer()
    page.check_subscribe_in_footer()
    page.should_be_footer_subscribe_success()
