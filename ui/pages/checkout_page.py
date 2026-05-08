
import os
import time

from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import ContactUsPageLocators, CheckoutPageLocators
from ui.test_data.data import SuccessMessageText
from ui.tools.faker import fake
from config import settings


load_dotenv()


class CheckoutPage(BasePage):
    ENDPOINT = os.getenv("CHECKOUT")

    def should_be_checkout_page(self):
        self.check_url()
        self.elem_should_be_visible(selector=CheckoutPageLocators.ADDRESS_DELIVERY)
        self.elem_should_be_visible(selector=CheckoutPageLocators.ADDRESS_INVOICE)
        self.elem_should_be_visible(selector=CheckoutPageLocators.ORDER_ADD_INFO)
        self.elem_should_be_visible(selector=CheckoutPageLocators.PLACE_ORDER_BTN)


    def check_orders_details(self, user_data):
        address_delivery = self.page.locator(CheckoutPageLocators.ADDRESS_DELIVERY)
        address_invoice = self.page.locator(CheckoutPageLocators.ADDRESS_INVOICE)

        delivery_text = self.get_inner_text(root=address_delivery)
        invoice_text = self.get_inner_text(root=address_invoice)
        for value in user_data.values():
            assert value in delivery_text, f"value = {value}"
            assert value in invoice_text, f"value = {value}"