from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form") 

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span")

class BasketPageLocators():
    BUSKET_ITEM = (By.CSS_SELECTOR,"#basket_formset")
    MESSAGE_ABOUT_CLEAR_BUSKET = (By.CSS_SELECTOR,"#content_inner > p > a")