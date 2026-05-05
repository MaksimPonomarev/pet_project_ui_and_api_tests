


def test_logout(base_page, create_account):
    base_page.should_be_logged_in()
    base_page.logout()
    base_page.should_be_logged_out()