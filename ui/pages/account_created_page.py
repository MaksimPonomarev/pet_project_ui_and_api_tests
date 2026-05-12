import os
import time

from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import SignupPageLocators, BasePageLocators, CreatedAccountPageLocators
from ui.test_data.data import SuccessMessageText, Titles
from ui.tools.faker import fake

load_dotenv()


class CreatedAccountPage(BasePage):
    ENDPOINT = os.getenv("ACCOUNT_CREATED")

    def should_be_success_created_account(self):
        self.check_url()
        self.should_be_visible_with_text(selector=CreatedAccountPageLocators.ACCOUNT_CREATED_TITLE, text=Titles.CREATED_ACCOUNT)
        self.should_be_visible_inner_text(text=SuccessMessageText.CREATED_ACCOUNT)

    def click_continue(self):
        self.click(selector=CreatedAccountPageLocators.CONTINUE_BTN)

