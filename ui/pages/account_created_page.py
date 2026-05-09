import os
import time

from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import SignupPageLocators, BasePageLocators
from ui.tools.faker import fake

load_dotenv()


class CreatedAccountPage(BasePage):
    ENDPOINT = os.getenv("ACCOUNT_CREATED")

    def should_be_success_created_account(self):
        self.check_url(endpoint="/account_created")
        self.elem_should_be_visible(selector=SignupPageLocators.ACCOUNT_CREATED_MESSAGE)


    def click_continue(self):
        self.click(selector=BasePageLocators.CONTINUE_BTN)