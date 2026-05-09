import os
import time

from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import LoginPageLocators, PaymentPageLocators, PaymentDonePageLocators, \
    DeleteAccountPageLocators, BasePageLocators
from ui.test_data.data import ErrorMessageText, SuccessMessageText, Titles
from ui.tools.faker import fake

load_dotenv()


class DeleteAccountPage(BasePage):
    ENDPOINT = os.getenv("DELETE_ACCOUNT")

    def should_be_deleted_account_page(self):
        self.check_url()
        self.should_be_visible_with_text(selector=DeleteAccountPageLocators.ACCOUNT_DELETED_BLOCK, text=Titles.DELETED_ACCOUNT)
        self.should_be_visible_with_text(selector=DeleteAccountPageLocators.ACCOUNT_DELETED_BLOCK, text=SuccessMessageText.DELETED_ACCOUNT)
        self.should_be_logged_out()


    def click_continue(self):
        self.click(selector=BasePageLocators.CONTINUE_BTN)
