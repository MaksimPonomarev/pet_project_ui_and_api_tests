
import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from ui.pages.base_page import BasePage
from ui.pages.locators import BasePageLocators

load_dotenv()


class MainPage(BasePage):
    ENDPOINT = os.getenv("MAIN_ENDPOINT")


    def should_be_cookie_banner(self):
        cookie_banner = self.page.locator(BasePageLocators.COOKIE_BANNER)
        cookie_banner.wait_for(state="attached")

    def accept_cookie_banner(self):
        cookie_banner = self.page.locator(BasePageLocators.COOKIE_BANNER)
        cookie_banner.wait_for(state="visible")
        self.click(selector=BasePageLocators.ACCEPT_COOKIE_BANNER_BTN)
        expect(cookie_banner).to_be_hidden()

    def should_be_login_link_enable(self):
        login_button = self.elem_must_be_visible(BasePageLocators.LOGIN_LINK)
        expect(login_button).to_have_attribute("href", "/login")

    def should_be_head_of_site(self):
        expect(self.page.locator(BasePageLocators.PANEL_OF_TABS)).to_be_visible()

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
            expect(self.page.locator(selector=selector, has_text=text)).to_be_visible()


