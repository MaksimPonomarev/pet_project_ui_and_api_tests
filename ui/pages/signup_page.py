import os
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import SignupPageLocators
from ui.tools.faker import fake

load_dotenv()


class SignupPage(BasePage):
    ENDPOINT = os.getenv("signup_endpoint")

    def create_user(self):
        data = fake.date_of_birth()

        self.click(selector=SignupPageLocators.TITLE_MR if fake.title() == 1 else SignupPageLocators.TITLE_MRS)
        self.enter_data(selector=SignupPageLocators.NAME, text=fake.name())
        password = self.enter_data(selector=SignupPageLocators.PASSWORD, text=fake.password())
        self.select_elem_in_dropdown(selector=SignupPageLocators.DAYS, value=data["day"])
        self.select_elem_in_dropdown(selector=SignupPageLocators.MONTHS, value=data["month"])
        self.select_elem_in_dropdown(selector=SignupPageLocators.YEAR, value=data["year"])
        self.enter_data(selector=SignupPageLocators.FIRST_NAME, text=fake.first_name())
        self.enter_data(selector=SignupPageLocators.LAST_NAME, text=fake.last_name())
        self.enter_data(selector=SignupPageLocators.COMPANY, text=fake.company())
        self.enter_data(selector=SignupPageLocators.ADDRESS, text=fake.address())
        self.enter_data(selector=SignupPageLocators.ADDRESS2, text=fake.address2())
        self.select_elem_in_dropdown(selector=SignupPageLocators.COUNTRY, value=fake.country())
        self.enter_data(selector=SignupPageLocators.STATE, text=fake.state())
        self.enter_data(selector=SignupPageLocators.CITY, text=fake.city())
        self.enter_data(selector=SignupPageLocators.ZIPCODE, text=fake.zipcode())
        self.enter_data(selector=SignupPageLocators.MOBILE_NUMBER, text=fake.mobile_number())
        self.click(selector=SignupPageLocators.CREATE_ACCOUNT_BTN)
        return {"password": password}

    def checking_successful_account_creation(self):
        self.check_url(endpoint="/account_created")
        self.elem_must_be_visible(selector=SignupPageLocators.ACCOUNT_CREATED_MESSAGE)

    def click_continue(self):
        self.click(selector=SignupPageLocators.CONTINUE_BTN)



