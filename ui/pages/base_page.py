import os
import re
from dotenv import load_dotenv
from playwright.sync_api import expect

from config import settings
from ui.components.footer_component import FooterComponent
from ui.components.header_component import HeaderComponent
from ui.pages.locators import BasePageLocators, LeftSidebarLocators
from ui.test_data.data import HeaderSite, WomenSubcategory, MenSubcategory, KidsSubcategory

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class BasePage:
    ENDPOINT = ""
    def __init__(self, page):
        self.page = page
        self.header = HeaderComponent(self)
        self.footer = FooterComponent(self)
        self.cart_items = {}

    def should_be_visible_with_text(self, text, selector=None, root=None, exact=False):
        locator = root or self.page
        if selector:
            if exact:
                expect(locator.locator(selector)).to_have_text(text)
            else:
                expect(locator.locator(selector).filter(has_text=text)).to_be_visible()

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
            expect(locator.get_by_text(text)).to_be_visible()

    def should_be_logged_in(self):
        self.elem_should_be_visible(selector=BasePageLocators.LOGOUT_LINK)
        self.elem_should_be_visible(selector=BasePageLocators.DELETE_ACCOUNT_LINK)
        self.should_be_visible_with_text(selector=BasePageLocators.HEADER, text=HeaderSite.LOGGEN_IN_TEXT)

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

    def check_url(self, endpoint=None, timeout=None):
        expected_url = f"{BASE_URL}{endpoint or self.ENDPOINT}"
        expect(self.page).to_have_url(re.compile(rf"{re.escape(expected_url)}(?:#.*)?"),  timeout=timeout or settings.default_timeout)

    def not_to_have_url(self, endpoint=None, timeout=None):
        expected_url = f"{BASE_URL}{endpoint or self.ENDPOINT}"
        expect(self.page).not_to_have_url(re.compile(rf"{re.escape(expected_url)}(?:#.*)?"), timeout=timeout or settings.default_timeout)

    def click(self, selector, root=None, index=1):
        locator = root or self.page
        el = locator.locator(selector).nth(index-1)
        el.click()

    def wait_page_is_functional(self):
        self.page.wait_for_load_state("domcontentloaded", timeout=50000)


    def elem_should_be_visible(self, selector, timeout=None):
        elem = self.page.locator(selector=selector)
        expect(elem).to_be_visible(timeout=timeout or settings.default_timeout)
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


    def should_be_logged_out(self):
        expect(self.page.locator(BasePageLocators.LOGIN_LINK)).to_be_visible()

    def logout(self):
        self.click(selector=BasePageLocators.LOGOUT_LINK)

    def select_elem_in_dropdown(self, selector, value):
        result = self.page.locator(selector=selector).select_option(value=value)
        return result[0] if result else None

    def open(self):
        self.page.goto(f"{BASE_URL}{self.ENDPOINT}", timeout=settings.navigation_timeout, wait_until="commit")


    def get_text_by_locator(self, selector, root=None):
        locator = root or self.page
        return locator.locator(selector).text_content()

    def get_text_by_attribute_for_locator(self, selector, attribute, root=None):
        locator = root or self.page
        return locator.locator(selector).get_attribute(attribute)


    def hover(self, selector, root=None):
        locator = root or self.page
        locator.locator(selector).hover()


    def add_product_to_cart(self, index=0, selector=None):
        card = self.page.locator(selector=selector or BasePageLocators.CARD_OF_ITEM).nth(index)

        name = self.get_text_by_locator(selector=BasePageLocators.ITEM_NAME, root=card)
        price = self.get_text_by_locator(selector=BasePageLocators.ITEM_PRICE, root=card)
        card_id = self.get_text_by_attribute_for_locator(selector=BasePageLocators.ID_CARD_LOCATOR, root=card, attribute=BasePageLocators.ID_CARD_ATTRIBUTE)


        self.hover(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)
        self.click(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)

        self.click(selector=BasePageLocators.CONTINUE_SHOPPING_BTN)
        if card_id in self.cart_items:
            self.cart_items[card_id]["count"] += 1
        else:
            self.cart_items[card_id] = {"name": name, "price": price, "count": 1, "card_id": card_id}
        return card_id


    def get_product_id_from_card(self, index=0, selector=None):
        card = self.page.locator(selector=selector or BasePageLocators.CARD_OF_ITEM).nth(index)
        card_id = self.get_text_by_attribute_for_locator(selector=BasePageLocators.ID_CARD_LOCATOR, root=card, attribute=BasePageLocators.ID_CARD_ATTRIBUTE)
        return card_id


    def assert_equal(self, actual, expected):
        assert actual == expected, f"actual = {actual}, expected = {expected}, actual_type = {type(actual)}, expected = {type(expected)}"

    def should_not_be_visible(self, selector):
        expect(self.page.locator(selector)).to_have_count(0)

    def check_product_card(self, index=0):
        card = self.page.locator(selector=BasePageLocators.CARD_OF_ITEM).nth(index)

        self.first_elem_should_be_visible(selector=BasePageLocators.IMAGE_OF_CARD, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ITEM_PRICE, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ITEM_NAME, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.ADD_TO_CART_BTN, root=card)
        self.first_elem_should_be_visible(selector=BasePageLocators.VIEW_PRODUCT_DETAILS_BTN, root=card)



    def scroll_to_elem(self, selector):
        self.page.locator(selector).scroll_into_view_if_needed()


    def should_be_success_message(self, selector, text):
        self.should_be_visible_with_text(selector=selector, text=text)

    def open_product_card_detail(self, card_id):
        card = self.page.locator(BasePageLocators.CARD_OF_ITEM).filter(has=self.page.locator(BasePageLocators.select_card_by_id(card_id=card_id)))
        self.click(selector=BasePageLocators.VIEW_PRODUCT_DETAILS_BTN, root=card)

    def scroll_to_visible_elem(self, selector):
        self.page.locator(selector=selector).scroll_into_view_if_needed()

    def click_scroll_up_btn(self):
        self.click(selector=BasePageLocators.SCROLL_UP_BTN)


    def should_be_elem_in_viewport(self, selector, visible=True):
        locator = self.page.locator(selector)
        if visible:
            expect(locator).to_be_in_viewport()
        else:
            expect(locator).not_to_be_in_viewport()

    def click_with_retry(self, click_selector, wait_selector, timeout=2000):
        self.click(click_selector)
        try:
            self.elem_should_be_visible(wait_selector, timeout=timeout)
        except AssertionError:
            self.click(click_selector)
            self.elem_should_be_visible(wait_selector, timeout=timeout)

    def should_be_header_visible(self, visible=True):
        self.should_be_elem_in_viewport(selector=BasePageLocators.HEADER, visible=visible)


    # products methods (base_page, product_page)
    def should_be_visible_left_sidebar(self):
        self.elem_should_be_visible(selector=LeftSidebarLocators.LEFT_SIDEBAR)
        self.elem_should_be_visible(selector=LeftSidebarLocators.CATEGORY)
        self.elem_should_be_visible(selector=LeftSidebarLocators.BRANDS)

    def should_be_categories_on_left_sidebar(self):
        self.elem_should_be_visible(selector=LeftSidebarLocators.category_group(WomenSubcategory))
        self.elem_should_be_visible(selector=LeftSidebarLocators.category_group(MenSubcategory))
        self.elem_should_be_visible(selector=LeftSidebarLocators.category_group(KidsSubcategory))




