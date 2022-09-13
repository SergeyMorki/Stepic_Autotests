from .base_page import BasePage
from .locators import BasketLocators

class Basket(BasePage):
    def should_be_empty_busket(self):
        self.is_element_present(*BasketLocators.TEXT_EMPTY_BASKET)
        empty_basket = self.browser.find_element(*BasketLocators.TEXT_EMPTY_BASKET)
        print(empty_basket.text)
        assert empty_basket.text == 'Your basket is empty. Continue shopping', 'Basket is not empty'