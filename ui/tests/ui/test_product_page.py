import time

import pytest

from ui.test_data.data import SearchData


def test_check_product_page(products_page):
    products_page.open()
    products_page.should_be_product_page()
    products_page.check_product_card()



@pytest.mark.parametrize("name", SearchData.VALID_PRODUCTS)
def test_check_search_product(products_page, name):
    products_page.open()
    products_page.should_be_product_page()
    products_page.search_product(name_of_product=name)
    products_page.check_all_results_search_product(name_of_product=name)