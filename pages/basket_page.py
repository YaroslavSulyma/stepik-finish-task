from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_clear_basket()
        self.should_be_message_about_clear_basket()

    def should_be_clear_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BUSKET_ITEM), "Busket is not clear!"

    def should_not_be_clear_basket(self):
        assert self.is_element_present(*BasketPageLocators.BUSKET_ITEM), "Busket is clear!"
    
    def should_be_message_about_clear_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_CLEAR_BUSKET), "No massage about clear basket!"
    
    def should_net_be_message_about_clear_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_ABOUT_CLEAR_BUSKET), "Message about cleat basket!"