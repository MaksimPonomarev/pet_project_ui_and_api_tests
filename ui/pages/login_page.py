import time

from ui.pages.base_page import BasePage, BASE_URL
import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from ui.pages.base_page import BasePage
from ui.pages.locators import LoginPageLocators, SignupPageLocators, BasePageLocators
from ui.pages.main_page import MainPage
from ui.tools.faker import fake

load_dotenv()


class LoginPage(BasePage):
    ENDPOINT = os.getenv("LOGIN_ENDPOINT")

    def should_be_login_and_forms(self):
        expect(self.page.locator(LoginPageLocators.SIGNUP_FORM)).to_be_visible(timeout=15000)

    def go_to_signup(self):
        email = fake.email()
        self.enter_data(selector=LoginPageLocators.SIGNUP_EMAIL_AREA, text=email)
        self.enter_data(selector=LoginPageLocators.SIGNUP_NAME_AREA, text=fake.name())
        self.click(selector=LoginPageLocators.SIGNUP_BTN)
        return {"email": email}
    
    def logout(self):
        self.click(selector=BasePageLocators.LOGOUT_LINK)

    def login(self, email, password):
        self.enter_data(selector=LoginPageLocators.LOGIN_EMAIL_AREA, text=email)
        self.enter_data(selector=LoginPageLocators.LOGIN_PASSWORD_AREA, text=password)
        self.click(selector=LoginPageLocators.LOGIN_BTN)
