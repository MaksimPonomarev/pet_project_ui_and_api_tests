import os
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import ProductsPageLocators, LeftSidebarLocators

load_dotenv()


class ProductsPage(BasePage):
    ENDPOINT = os.getenv("PRODUCTS_ENDPOINT")

    def should_be_product_page(self):
        self.elem_should_be_visible(selector=ProductsPageLocators.ADVERTISEMENT)
        self.elem_should_be_visible(selector=ProductsPageLocators.SEARCH_PRODUCT)
        self.elem_should_be_visible(selector=LeftSidebarLocators.LEFT_SIDEBAR)
        self.first_elem_should_be_visible(selector=ProductsPageLocators.CARD_OF_ITEM)
        self.check_url()


    def check_all_results_search_product(self, name_of_product):
        cards = self.page.locator(selector=ProductsPageLocators.CARD_OF_ITEM)
        for i in range(cards.count()):
            card = cards.nth(i)
            self.should_be_visible_with_text(selector=ProductsPageLocators.ITEM_NAME, text=name_of_product, root=card)


    def search_product(self, name_of_product):
        self.enter_data(selector=ProductsPageLocators.SEARCH_PRODUCT, text=name_of_product)
        self.click(selector=ProductsPageLocators.SUBMIT_SEARCH_BTN)
        self.check_product_card()
