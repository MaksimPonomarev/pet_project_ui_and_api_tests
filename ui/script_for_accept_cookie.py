from pydoc import pager

from playwright.sync_api import sync_playwright

from ui.pages.locators import BasePageLocators


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://automationexercise.com")
    page.locator(BasePageLocators.COOKIE_BANNER).wait_for(state="visible")
    page.locator(BasePageLocators.ACCEPT_COOKIE_BANNER_BTN).click()

    context.storage_state(path="storage_state.json")  # сохраняем куки
