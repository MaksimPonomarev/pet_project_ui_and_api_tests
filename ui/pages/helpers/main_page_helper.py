from playwright.sync_api import expect

from ui.pages.locators import BasePageLocators


def should_be_cookie_banner(page):
    cookie_banner = page.locator(selector=BasePageLocators.COOKIE_BANNER)
    cookie_banner.wait_for(timeout=15000, state="attached")


def accept_cookie_banner(page):
    accept_btn = page.locator(selector=BasePageLocators.ACCEPT_COOKIE_BANNER_BTN)
    cookie_banner = page.locator(selector=BasePageLocators.COOKIE_BANNER)
    cookie_banner.wait_for(timeout=15000, state="visible")
    accept_btn.click(timeout=15000)
    expect(cookie_banner).to_be_hidden(timeout=15000)




def should_be_login_link_enable(page):
    login_button = page.locator(selector=BasePageLocators.LOGIN_LINK)
    expect(login_button).to_be_visible(timeout=15000)
    expect(login_button).to_have_attribute("href", "/login")