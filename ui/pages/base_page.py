import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from ui.pages.locators import BasePageLocators, LoginPageLocators

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class BasePage:
    ENDPOINT = ""
    def __init__(self, page):
        self.page = page

    def should_be_logged_in(self):
        self.elem_must_be_visible(selector=BasePageLocators.LOGOUT_LINK)
        self.elem_must_be_visible(selector=BasePageLocators.DELETE_ACCOUNT_LINK)
        expect(self.page.get_by_text("Logged in")).to_be_visible()


    def enter_data(self, selector, text):
        self.page.locator(selector=selector).fill(value=text)
        return text

    def check_url(self, endpoint=None):
        expected_url = f"{BASE_URL}{endpoint or self.ENDPOINT}"
        expect(self.page).to_have_url(expected_url)

    def click(self, selector):
        el = self.page.locator(selector=selector)
        expect(el).to_be_enabled()
        el.click()

    def elem_must_be_visible(self, selector):
        elem = self.page.locator(selector=selector)
        expect(elem).to_be_visible()
        return elem

    def should_be_logged_out(self):
        expect(self.page.locator(BasePageLocators.LOGIN_LINK)).to_be_visible()

    def logout(self):
        self.click(selector=BasePageLocators.LOGOUT_LINK)

    def select_elem_in_dropdown(self, selector, value):
        self.page.locator(selector=selector).select_option(value=value)

    def open(self):
        self.page.goto(f"{BASE_URL}{self.ENDPOINT}", timeout=30000)

    def go_to_home(self):
        self.page.locator(selector=BasePageLocators.HOME_LINK).click()

    def go_to_products(self):
        self.page.locator(selector=BasePageLocators.PRODUCTS_LINK).click()

    def go_to_cart(self):
        self.page.locator(selector=BasePageLocators.CART_LINK).click()

    def go_to_login(self):
        self.page.locator(selector=BasePageLocators.LOGIN_LINK).click()

    def go_to_test_cases(self):
        self.page.locator(selector=BasePageLocators.TEST_CASES_LINK).click()

    def go_to_api_list(self):
        self.page.locator(selector=BasePageLocators.API_LIST_LINK).click()

    def go_to_video_tutorials(self):
        self.page.locator(selector=BasePageLocators.VIDEO_TUTORIALS_LINK).click()

    def go_to_contact_us(self):
        self.page.locator(selector=BasePageLocators.CONTACT_US_LINK).click()