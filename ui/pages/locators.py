



class BasePageLocators:
    COOKIE_BANNER = "div.fc-dialog.fc-choice-dialog"
    ACCEPT_COOKIE_BANNER_BTN = ".fc-cta-consent.fc-primary-button"

    IMG_LOGO_SITE = "img[src='/static/images/home/logo.png']"
    PANEL_OF_TABS = ".shop-menu"

    HOME_LINK = "li a[href='/']"
    PRODUCTS_LINK = "li a[href='/products']"
    CART_LINK = "li a[href='/view_cart']"
    LOGIN_LINK = "li a[href='/login']"
    TEST_CASES_LINK = "li a[href='/test_cases']"
    API_LIST_LINK = "li a[href='/api_list']"
    VIDEO_TUTORIALS_LINK = "li a[href='https://www.youtube.com/c/AutomationExercise']"
    CONTACT_US_LINK = "li a[href='/contact_us']"


class LoginPageLocators:
    LOGIN_FORM = ".login-form"
    LOGIN_EMAIL_AREA= "[data-qa=login-email]"
    LOGIN_PASSWORD_AREA = "[data-qa=login-password]"
    LOGIN_BTN = "[data-qa=login-button]"

    SIGNUP_FORM = ".signup-form"
    SIGNUP_EMAIL_AREA = "[data-qa=signup-name]"
    SIGNUP_PASSWORD_AREA = "[data-qa=signup-password]"
    SIGNUP_BTN = "[data-qa=signup-button]"