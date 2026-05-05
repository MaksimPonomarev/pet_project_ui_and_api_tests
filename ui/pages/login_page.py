import time
from tkinter.font import names

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

    def go_to_signup(self, email=None, name=None):
        email = email or fake.email()
        name = name or fake.name()
        self.enter_data(selector=LoginPageLocators.SIGNUP_EMAIL_AREA, text=email)
        self.enter_data(selector=LoginPageLocators.SIGNUP_NAME_AREA, text=name)
        self.click(selector=LoginPageLocators.SIGNUP_BTN)
        return {"email": email, "name": name}


    def login(self, email, password):
        self.enter_data(selector=LoginPageLocators.LOGIN_EMAIL_AREA, text=email)
        self.enter_data(selector=LoginPageLocators.LOGIN_PASSWORD_AREA, text=password)
        self.click(selector=LoginPageLocators.LOGIN_BTN)

    def should_be_incorrect_login_error(self):
        expect(self.page.get_by_text(LoginPageLocators.INCORRECT_LOGIN_ERROR)).to_be_visible()

    def should_be_incorrect_signup_error(self):
        expect(self.page.get_by_text(LoginPageLocators.INCORRECT_SIGNUP_ERROR)).to_be_visible()