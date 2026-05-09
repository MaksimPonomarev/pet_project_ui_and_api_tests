import os
import time

from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import LoginPageLocators, PaymentPageLocators, PaymentDonePageLocators, BasePageLocators
from ui.test_data.data import ErrorMessageText, SuccessMessageText
from ui.tools.faker import fake

load_dotenv()


class PaymentDonePage(BasePage):
    ENDPOINT = os.getenv("PAYMENT_DONE")

    def should_be_payment_done_page(self):
        self.check_url()
        self.should_be_success_message(selector=PaymentDonePageLocators.ORDER_PLACED, text=SuccessMessageText.PLACE_ORDER)
        self.elem_should_be_visible(selector=PaymentDonePageLocators.DOWNLOAD_INVOICE_BTN)
        self.elem_should_be_visible(selector=BasePageLocators.CONTINUE_BTN)

    def click_download_invoice(self):
        self.click(selector=PaymentDonePageLocators.DOWNLOAD_INVOICE_BTN)

    def click_continue(self):
        self.click(selector=PaymentDonePageLocators.DOWNLOAD_INVOICE_BTN)