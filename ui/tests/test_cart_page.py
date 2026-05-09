import time


def test_add_product_in_cart(products_page, cart_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.add_product_to_cart(num_of_card=1)
    products_page.add_product_to_cart(num_of_card=2)
    products_page.go_to_cart()
    cart_page.check_added_products(cart_items=products_page.cart_items)

def test_add_same_product_twice(products_page, cart_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.add_product_to_cart(num_of_card=1)
    products_page.add_product_to_cart(num_of_card=1)
    products_page.go_to_cart()
    cart_page.check_added_products(cart_items=products_page.cart_items)


def test_check_product_quantity_in_cart(products_page, detail_products_page, cart_page):
    products_page.open()
    products_page.open_product_card_detail(num_of_card=3)
    detail_products_page.should_be_product_detail_page()
    detail_products_page.enter_quantity_for_product(quantity=4)
    item_id = detail_products_page.add_detail_product_to_cart()
    detail_products_page.go_to_cart()
    cart_page.should_be_filled_cart()
    cart_page.check_quantity(item_id=item_id, expect_quantity=4)


def test_register_while_checkout(main_page, cart_page, login_page, signup_page, checkout_page, payment_page, payment_done_page, deleted_account_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.add_product_to_cart()
    main_page.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.go_to_login_page_from_checkout_form()

    login_page.should_be_login_page()

    signup_data = login_page.go_to_signup()
    signup_page.should_be_signup_page()

    user_account_info = signup_page.create_user(signup_data)
    signup_page.checking_successful_account_creation()
    signup_page.click_continue()

    main_page.should_be_main_page()
    main_page.should_be_logged_in()
    main_page.go_to_cart()

    cart_page.checkout_logged_in_user()

    checkout_page.should_be_checkout_page()
    checkout_page.check_orders_details(user_account_info["user_info"])
    checkout_page.fill_comment()
    checkout_page.click_place_order()

    payment_page.should_be_payment_page()
    payment_page.fill_payment_form()

    payment_done_page.should_be_payment_done_page()
    payment_done_page.delete_account()

    deleted_account_page.should_be_deleted_account_page()
    deleted_account_page.click_continue()

    main_page.should_be_main_page()
