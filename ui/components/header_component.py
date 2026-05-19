from playwright.sync_api import expect

from ui.pages.locators import BasePageLocators


class HeaderComponent:
    def __init__(self, base_page):
        self.base_page = base_page

    def should_be_head_of_site(self):
        self.base_page.elem_should_be_visible(BasePageLocators.HEADER)

        nav_items = [
            (BasePageLocators.HOME_LINK, "Home"),
            (BasePageLocators.PRODUCTS_LINK, "Products"),
            (BasePageLocators.CART_LINK, "Cart"),
            (BasePageLocators.LOGIN_LINK, "Signup / Login"),
            (BasePageLocators.TEST_CASES_LINK, "Test Cases"),
            (BasePageLocators.API_LIST_LINK, "API Testing"),
            (BasePageLocators.VIDEO_TUTORIALS_LINK, "Video Tutorials"),
            (BasePageLocators.CONTACT_US_LINK, "Contact us"),
        ]

        for selector, text in nav_items:
            self.base_page.should_be_visible_with_text(selector=selector, text=text)

    def go_to_home(self):
        self.base_page.click(selector=BasePageLocators.HOME_LINK)

    def go_to_products(self):
        self.base_page.click(selector=BasePageLocators.PRODUCTS_LINK)

    def go_to_cart(self):
        self.base_page.click(selector=BasePageLocators.CART_LINK)

    def go_to_login(self):
        self.base_page.click(selector=BasePageLocators.LOGIN_LINK)

    def go_to_test_cases(self):
        self.base_page.click(selector=BasePageLocators.TEST_CASES_LINK)

    def go_to_api_list(self):
        self.base_page.click(selector=BasePageLocators.API_LIST_LINK)

    def go_to_video_tutorials(self):
        self.base_page.click(selector=BasePageLocators.VIDEO_TUTORIALS_LINK)

    def go_to_contact_us(self):
        self.base_page.click(selector=BasePageLocators.CONTACT_US_LINK)