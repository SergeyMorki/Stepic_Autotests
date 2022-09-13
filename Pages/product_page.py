from .base_page import BasePage
from .locators import ProductPageLocators

class Catalogue(BasePage):
    def add_in_basket(self):
        add_in_basket = self.browser.find_element(*ProductPageLocators.ADD_IN_BUSKET)
        add_in_basket.click()

    def should_be_added(self):
        addtext = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT)
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert addtext.text == f"{product.text} has been added to your basket.", 'Name of added product is other'

    def should_be_price(self):
        pricetext = self.browser.find_element(*ProductPageLocators.PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text == pricetext.text, 'Prices are different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
