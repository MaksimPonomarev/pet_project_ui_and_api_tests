import os
from dotenv import load_dotenv

from ui.pages.locators import BasePageLocators

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class BasePage:
    ENDPOINT = ""
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(f"{BASE_URL}{self.ENDPOINT}")

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