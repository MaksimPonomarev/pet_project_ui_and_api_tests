import os
import time

from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.locators import SignupPageLocators, BasePageLocators, LeftSidebarLocators
from ui.test_data.data import CategoryGroup, Brands
from ui.tools.faker import fake

load_dotenv()


class LeftSidebarComponent:
    def __init__(self, base_page):
        self.base_page = base_page

    @staticmethod
    def endpoint_category(category):
        return f"/category_products/{category}"

    @staticmethod
    def title_category(category):
        return f"{category} Products"


    def open_category_group(self, category):
        self.base_page.click(selector=LeftSidebarLocators.category_group(category.value))

    def should_be_category_group_opened(self, subcategory):
        for elem in subcategory:
            self.base_page.elem_should_be_visible(selector=LeftSidebarLocators.subcategory(subcategory=elem.id))

    def open_subcategory_page(self, subcategory):
        self.base_page.click(selector=LeftSidebarLocators.subcategory(subcategory.id))


    def should_be_subcategory_products_page(self, subcategory):
        self.base_page.check_url(endpoint=self.endpoint_category(subcategory.id))
        self.base_page.should_be_visible_with_text(selector=BasePageLocators.TITLE, text=self.title_category(subcategory.title), exact=True)
        self.base_page.check_product_card()




    def open_brand_page(self, brand):
        self.base_page.click(selector=LeftSidebarLocators.brand_item(brand.value))

    def should_be_brand_products_page(self, brand):
        self.base_page.check_url(endpoint=brand.url)
        self.base_page.should_be_visible_with_text(selector=BasePageLocators.TITLE, text=brand.title_brand, exact=True)
        self.base_page.check_product_card()

    def should_be_brands_on_left_sidebar(self):
        self.base_page.elem_should_be_visible(selector=LeftSidebarLocators.BRANDS)
        for elem in Brands:
            self.base_page.elem_should_be_visible(selector=LeftSidebarLocators.brand_item(elem.value))