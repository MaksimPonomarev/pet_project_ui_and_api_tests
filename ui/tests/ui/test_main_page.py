import time


def test_check_accept_cookie_banner(main_page_without_context):
    main_page_without_context.open()
    main_page_without_context.should_be_cookie_banner()
    main_page_without_context.accept_cookie_banner()
    main_page_without_context.should_be_main_page()



def test_add_recommended_product(main_page, cart_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.add_recommended_product()
    main_page.header.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=main_page.cart_items)