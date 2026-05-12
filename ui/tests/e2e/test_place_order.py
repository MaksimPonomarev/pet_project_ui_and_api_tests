import time

from ui.fixtures.page_fixtures import created_account_page


def test_register_while_checkout(products_page, main_page, cart_page, login_page, signup_page, checkout_page, payment_page, payment_done_page, deleted_account_page, created_account_page):
    main_page.open()
    main_page.should_be_main_page()
    main_page.add_product_to_cart()
    main_page.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=main_page.cart_items)
    cart_page.go_to_login_page_from_checkout_form()

    login_page.should_be_login_page()

    signup_data = login_page.go_to_signup()
    signup_page.should_be_signup_page()

    user_account_info = signup_page.create_user(signup_data)
    created_account_page.should_be_success_created_account()

    created_account_page.click_continue()

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


def test_register_before_checkout(products_page, main_page, created_account_page, cart_page, login_page, signup_page, checkout_page, payment_page, payment_done_page, deleted_account_page):
    main_page.open()
    main_page.should_be_main_page()

    main_page.go_to_login()

    login_page.should_be_login_page()
    signup_data = login_page.go_to_signup()


    signup_page.should_be_signup_page()

    user_account_info = signup_page.create_user(signup_data)
    created_account_page.should_be_success_created_account()
    created_account_page.click_continue()

    main_page.should_be_main_page()
    main_page.should_be_logged_in()
    main_page.add_product_to_cart()
    main_page.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=main_page.cart_items)

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


def test_login_before_checkout(create_account_and_logout,  deleted_account_page, payment_done_page, payment_page, checkout_page, main_page, login_page, products_page, cart_page):
    user_data = create_account_and_logout

    main_page.should_be_main_page()
    main_page.go_to_login()

    login_page.should_be_login_page()
    login_page.login(
        email=user_data["credentials"]["email"],
        password=user_data["credentials"]["password"]
    )
    login_page.should_be_logged_in()
    login_page.go_to_products()

    products_page.should_be_product_page()
    products_page.add_product_to_cart()
    products_page.go_to_cart()

    cart_page.should_be_filled_cart()
    cart_page.should_be_added_products(cart_items=products_page.cart_items)
    cart_page.checkout_logged_in_user()

    checkout_page.should_be_checkout_page()
    checkout_page.check_orders_details(user_data["user_info"])
    checkout_page.fill_comment()
    checkout_page.click_place_order()

    payment_page.should_be_payment_page()
    payment_page.fill_payment_form()

    payment_done_page.should_be_payment_done_page()
    payment_done_page.delete_account()

    deleted_account_page.should_be_deleted_account_page()
    deleted_account_page.click_continue()

    main_page.should_be_main_page()

