from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url==LoginPageLocators.LOGIN_LINK, "Login link is invalid"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
    
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(str(email))
        password_input = self.browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(str(password))
        confirm_password_input = self.browser.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(str(password))
        register_button = self.browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()