from Pages.main_page import MainPage, LoginPage
from Pages.product_page import Catalogue
from Pages.basket_page import Basket
from Pages.login_page import LoginPage
import time
import pytest


'''@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                               "?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])'''

@pytest.mark.user_add_to_busket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        self.email = str(time.time()) + "@fakemail.org"
        self.password = self.email
        login_page.register_new_user(self.email, self.password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = MainPage(browser, link)
        page.open()
        catalogue = Catalogue(browser, link)
        catalogue.add_in_basket()
        page.solve_quiz_and_get_code()
        catalogue.should_be_added()
        catalogue.should_be_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = MainPage(browser, link)
        page.open()
        catalogue = Catalogue(browser, link)
        catalogue.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    catalogue = Catalogue(browser, link)
    catalogue.add_in_basket()
    page.solve_quiz_and_get_code()
    catalogue.should_be_added()
    catalogue.should_be_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    catalogue = Catalogue(browser, link)
    catalogue.add_in_basket()
    catalogue.should_be_added()
    catalogue.should_be_price()
    catalogue.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = MainPage(browser, link)
    page.open()
    catalogue = Catalogue(browser, link)
    catalogue.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = MainPage(browser, link)
    page.open()
    catalogue = Catalogue(browser, link)
    catalogue.add_in_basket()
    catalogue.should_be_added()
    catalogue.should_be_price()
    catalogue.should_disappeared_success_message()

@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Catalogue(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    basket = Basket(browser, link)
    page.open()
    page.open_basket()
    basket.should_be_empty_busket()

