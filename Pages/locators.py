from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_URL = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner.wicon")

class ProductPageLocators:
    ADD_IN_BUSKET = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    ADDED_PRODUCT = (By.CSS_SELECTOR, '.alertinner')
    PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success.fade')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators:
    BASKET = (By.CSS_SELECTOR, '.btn-group .btn.btn-default:nth-child(1)')
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')