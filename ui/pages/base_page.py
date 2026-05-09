import os
import re

from dotenv import load_dotenv
from playwright.sync_api import expect

from config import settings
from ui.pages.locators import BasePageLocators, LoginPageLocators, ContactUsPageLocators
from ui.test_data.data import SuccessMessageText
from ui.tools.faker import fake

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class BasePage:
    ENDPOINT = ""
    def __init__(self, page):
        self.page = page
        self.cart_items = {}

    def should_be_visible_with_text(self, text, selector=None, root=None):
        locator = root or self.page
        if selector:
            expect(locator.locator(selector).filter(has_text=text)).to_be_visible()
        else:
            expect(locator.get_by_text(text)).to_be_visible()

    def get_inner_text(self, selector=None, root=None):
        locator = root or self.page
        if selector:
            return locator.locator(selector).inner_text()
        return locator.inner_text()


    def should_be_visible_inner_text(self, text, selector=None, root=None):
        locator = root or self.page
        if selector:
            expect(locator.locator(selector).filter(has_text=text)).to_be_visible()
        else:
            expect(locator.inner_text(text)).to_be_visible()

    def should_be_logged_in(self):
        self.elem_should_be_visible(selector=BasePageLocators.LOGOUT_LINK)
        self.elem_should_be_visible(selector=BasePageLocators.DELETE_ACCOUNT_LINK)
        expect(self.page.get_by_text("Logged in")).to_be_visible()

    def delete_account(self):
        self.click(selector=BasePageLocators.DELETE_ACCOUNT_LINK)

    def accept_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def dismiss_alert(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())

    def enter_data(self, selector, text):
        self.page.locator(selector=selector).fill(value=text)
        return text

    def enter_file(self, selector, path_to_file):
        self.page.locator(selector=selector).set_input_files(path_to_file)

    def check_url(self, endpoint=None):
        expected_url = f"{BASE_URL}{endpoint or self.ENDPOINT}"
        expect(self.page).to_have_url(re.compile(expected_url))

    def click(self, selector, root=None, num_of_card=1):
        locator = root or self.page
        el = locator.locator(selector).nth(num_of_card-1)
        expect(el).to_be_enabled()
        el.click()

    def elem_should_be_visible(self, selector):
        elem = self.page.locator(selector=selector)
        expect(elem).to_be_visible()
        return elem


    def first_elem_should_be_visible(self, selector, root=None):
        locator = root or self.page
        elem = locator.locator(selector).first
        expect(elem).to_be_visible()
        return elem

    def first_elem_should_be_attached(self, selector, root=None):
        locator = root or self.page
        elem = locator.locator(selector).first
        expect(elem).to_be_attached()
        return elem

    def should_be_login_link_enable(self):
        login_button = self.elem_should_be_visible(BasePageLocators.LOGIN_LINK)
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



    def should_be_logged_out(self):
        expect(self.page.locator(BasePageLocators.LOGIN_LINK)).to_be_visible()

    def logout(self):
        self.click(selector=BasePageLocators.LOGOUT_LINK)

    def select_elem_in_dropdown(self, selector, value):
        result = self.page.locator(selector=selector).select_option(value=value)
        return result[0] if result else None


    def open(self):
        self.page.goto(f"{BASE_URL}{self.ENDPOINT}", timeout=settings.navigation_timeout)

    def get_text_by_locator(self, selector, root=None):
        locator = root or self.page
        return locator.locator(selector).text_content()

    def get_text_by_attribute_for_locator(self, selector, attribute, root=None):
        locator = root or self.page
        return locator.locator(selector).get_attribute(attribute)


    def hover(self, selector, root=None):
        locator = root or self.page
        locator.locator(selector).hover()


    def add_product_to_cart(self, num_of_card=1):
        num_of_card -= 1
        card = self.page.locator(selector=BasePageLocators.CARD_OF_ITEM).nth(num_of_card)

        name = self.get_text_by_locator(selector=BasePageLocators.ITEM_NAME, root=card)
        price = self.get_text_by_locator(selector=BasePageLocators.ITEM_PRICE, root=card)
        card_id = self.get_text_by_attribute_for_locator(selector=BasePageLocators.ID_CARD_LOCATOR, root=card, attribute=BasePageLocators.ID_CARD_ATTRIBUTE)


        self.hover(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)
        self.click(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)

        self.click(selector=BasePageLocators.CONTINUE_SHOPPING_BTN)
        if card_id in self.cart_items:
            self.cart_items[card_id]["count"] += 1
        else:
            self.cart_items[card_id] = {"name": name, "price": price, "count": 1}

    def assert_equal(self, actual, expected):
        assert actual == expected, f"actual = {actual}, expected = {expected}, actual_type = {type(actual)}, expected = {type(expected)}"

    def check_product_card(self, index=0):
        card = self.page.locator(selector=BasePageLocators.CARD_OF_ITEM).nth(index)

        self.first_elem_should_be_visible(selector=BasePageLocators.IMAGE_OF_CARD, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ITEM_PRICE, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ITEM_NAME, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.VIEW_PRODUCT_DETAILS_BTN, root=card)

    def should_be_footer(self):
        self.elem_should_be_visible(BasePageLocators.FOOTER)
        self.elem_should_be_visible(BasePageLocators.FOOTER_TITLE)
        self.elem_should_be_visible(BasePageLocators.FOOTER_EMAIL)
        self.elem_should_be_visible(BasePageLocators.FOOTER_SUBSCRIBE_BTN)

    def check_subscribe_in_footer(self):
        self.enter_data(selector=BasePageLocators.FOOTER_EMAIL, text=fake.email())
        self.click(selector=BasePageLocators.FOOTER_SUBSCRIBE_BTN)

    def should_be_success_message(self, selector, text):
        self.should_be_visible_with_text(selector=selector, text=text)

    def should_be_footer_subscribe_success(self):
        self.should_be_success_message(BasePageLocators.FOOTER_SUCCESS_SUBSCRIBE_MESSAGE, text=SuccessMessageText.FOOTER_SUBSCRIBE)

    def open_product_card_detail(self, num_of_card=1):
        self.click(selector=BasePageLocators.VIEW_PRODUCT_DETAILS_BTN, num_of_card=num_of_card-1)


    def go_to_home(self):
        self.click(selector=BasePageLocators.HOME_LINK)

    def go_to_products(self):
        self.click(selector=BasePageLocators.PRODUCTS_LINK)

    def go_to_cart(self):
        self.click(selector=BasePageLocators.CART_LINK)

    def go_to_login(self):
        self.click(selector=BasePageLocators.LOGIN_LINK)

    def go_to_test_cases(self):
        self.click(selector=BasePageLocators.TEST_CASES_LINK)

    def go_to_api_list(self):
        self.click(selector=BasePageLocators.API_LIST_LINK)

    def go_to_video_tutorials(self):
        self.click(selector=BasePageLocators.VIDEO_TUTORIALS_LINK)

    def go_to_contact_us(self):
        self.click(selector=BasePageLocators.CONTACT_US_LINK)