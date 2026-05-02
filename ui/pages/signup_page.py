from ui.pages.base_page import BasePage
import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from ui.pages.base_page import BasePage
from ui.pages.locators import BasePageLocators, LoginPageLocators

load_dotenv()


class SignupPage(BasePage):
    ENDPOINT = os.getenv("signup_endpoint")

    def should_be_login_and_signup_forms(self):
        expect(self.page.locator(LoginPageLocators.LOGIN_FORM)).to_be_visible(timeout=15000)
        expect(self.page.locator(LoginPageLocators.SIGNUP_FORM)).to_be_visible(timeout=15000)