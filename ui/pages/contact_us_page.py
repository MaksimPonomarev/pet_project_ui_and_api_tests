import time
from ui.pages.base_page import BasePage, BASE_URL
import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from ui.pages.base_page import BasePage
from ui.pages.locators import LoginPageLocators, SignupPageLocators, BasePageLocators, ContactUsPageLocators
from ui.pages.main_page import MainPage
from ui.tools.faker import fake

load_dotenv()


class ContactUsPage(BasePage):
    ENDPOINT = os.getenv("CONTACT_US_ENDPOINT")

    def should_be_contact_us_form(self):
        expect(self.page.get_by_text(ContactUsPageLocators.GET_IN_TOUCH_TITLE)).to_be_visible()

    def should_be_success_message_send_feedback(self):
        expect(self.page.elem_must_be_visible(ContactUsPageLocators.SUCCESS_MESSAGE_LOCATOR)).to_be_visible()
        expect(self.page.get_by_text(ContactUsPageLocators.SUCCESS_MESSAGE_TEXT)).to_be_visible()

    def filling_out_the_form(self):
