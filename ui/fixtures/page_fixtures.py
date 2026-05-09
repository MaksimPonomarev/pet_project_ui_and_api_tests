import pytest

from ui.pages.api_page import ApiListPage
from ui.pages.base_page import BasePage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage
from ui.pages.contact_us_page import ContactUsPage
from ui.pages.delete_account_page import DeleteAccountPage
from ui.pages.detail_product_page import DetailProductsPage
from ui.pages.locators import CartPageLocators
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.payment_done_page import PaymentDonePage
from ui.pages.payment_page import PaymentPage
from ui.pages.products_page import ProductsPage
from ui.pages.signup_page import SignupPage
from ui.pages.testcases_page import TestCasesPage


@pytest.fixture
#создает готовую главную страницу
def main_page(get_page_with_context):
    page = MainPage(get_page_with_context)
    return page


@pytest.fixture
#создает готовую главную страницу с куки баннером
def main_page_without_context(get_page_without_context):
    page = MainPage(get_page_without_context)
    return page


@pytest.fixture
def signup_page(get_page_with_context):
    page = SignupPage(get_page_with_context)
    return page

@pytest.fixture
def login_page(get_page_with_context):
    page = LoginPage(get_page_with_context)
    return page


@pytest.fixture
def contact_us_page(get_page_with_context):
    page = ContactUsPage(get_page_with_context)
    return page

@pytest.fixture
def test_cases_page(get_page_with_context):
    page = TestCasesPage(get_page_with_context)
    return page

@pytest.fixture
def products_page(get_page_with_context):
    page = ProductsPage(get_page_with_context)
    return page

@pytest.fixture
def detail_products_page(get_page_with_context):
    page = DetailProductsPage(get_page_with_context)
    return page

@pytest.fixture
def cart_page(get_page_with_context):
    page = CartPage(get_page_with_context)
    return page

@pytest.fixture
def filled_cart_page(get_page_with_context):
    page = CartPage(get_page_with_context)
    return page

@pytest.fixture
def api_list_page(get_page_with_context):
    page = ApiListPage(get_page_with_context)
    return page

@pytest.fixture
def checkout_page(get_page_with_context):
    page = CheckoutPage(get_page_with_context)
    return page

@pytest.fixture
def payment_page(get_page_with_context):
    page = PaymentPage(get_page_with_context)
    return page


@pytest.fixture
def payment_done_page(get_page_with_context):
    page = PaymentDonePage(get_page_with_context)
    return page

@pytest.fixture
def deleted_account_page(get_page_with_context):
    page = DeleteAccountPage(get_page_with_context)
    return page