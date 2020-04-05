from .base_page import BasePage
from ui.locators.locators import AuthPageLocators
from selenium.webdriver.common.keys import Keys


class AuthPage(BasePage):

    locators = AuthPageLocators()

    def auth(self, email, password):
        self.click(self.locators.ENTER_BUTTON)
        email_field = self.find(self.locators.EMAIL)
        password_field = self.find(self.locators.PASSWORD)
        email_field.clear()
        password_field.clear()
        email_field.click()
        email_field.send_keys(email)
        password_field.click()
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
