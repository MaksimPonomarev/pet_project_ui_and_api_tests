



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

    #если залогинен появится\изменятся
    LOGOUT_LINK = "li a[href='/logout']"
    DELETE_ACCOUNT_LINK = "li a[href='/delete_account']"


class LoginPageLocators:
    LOGIN_FORM = ".login-form"
    LOGIN_EMAIL_AREA= "[data-qa=login-email]"
    LOGIN_PASSWORD_AREA = "[data-qa=login-password]"
    LOGIN_BTN = "[data-qa=login-button]"

    SIGNUP_FORM = ".signup-form"
    SIGNUP_NAME_AREA = "[data-qa=signup-name]"
    SIGNUP_EMAIL_AREA = "[data-qa=signup-email]"
    SIGNUP_BTN = "[data-qa=signup-button]"


class SignupPageLocators:
    TITLE_MR = "[data-qa=title] #id_gender1"
    TITLE_MRS = "[data-qa=title] #id_gender2"
    NAME = "[data-qa=name]"
    PASSWORD = "[data-qa=password]"
    DAYS = "[data-qa=days]"
    MONTHS = "[data-qa=months]"
    YEAR = "[data-qa=years]"

    FIRST_NAME = "[data-qa=first_name]"
    LAST_NAME = "[data-qa=last_name]"
    COMPANY = "[data-qa=company]"
    ADDRESS = "[data-qa=address]"
    ADDRESS2 = "[data-qa=address2]"
    COUNTRY = "[data-qa=country]"
    STATE = "[data-qa=state]"
    CITY = "[data-qa=city]"
    ZIPCODE = "[data-qa=zipcode]"
    MOBILE_NUMBER = "[data-qa=mobile_number]"

    CREATE_ACCOUNT_BTN = "[data-qa=create-account]"
    ACCOUNT_CREATED_MESSAGE = "[data-qa=account-created]"
    CONTINUE_BTN = "[data-qa=continue-button]"