from playwright.sync_api import sync_playwright, expect


def test_check_user_agreement():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://automationexercise.com/")

        user_agreement = page.locator(selector="#fc-focus-trap-post-div")
        user_agreement.wait_for(timeout=15000, state="attached")
        page.locator(selector=".fc-cta-consent.fc-primary-button").click(timeout=15000)
        login_button = page.locator(selector="li a[href='/login']")
        expect(user_agreement).to_be_hidden(timeout=15000)
        expect(login_button).to_be_visible(timeout=15000)
        expect(login_button).to_have_attribute("href", "/login")

