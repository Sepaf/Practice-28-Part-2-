from .base_page import BasePage
from .locators import AuthLocators
import time,os

class AuthPage(BasePage):

    def __init__(self,driver,timeout=10):
        super().__init__(driver,timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru"
        driver.get(url)
        self.email = driver.find_element(*AuthLocators.Auth_EMAIL)
        self.password = driver.find_element(*AuthLocators.Auth_Password)
        self.button = driver.find_element(*AuthLocators.Auth_Button)
        self.phone = driver.find_element(*AuthLocators.Auth_Phone)
        self.login = driver.find_element(*AuthLocators.Auth_Login)
        self.personal_account = driver.find_element(*AuthLocators.Auth_Personal_account)
        self.login_button = driver.find_element(*AuthLocators.Auth_Login_Button)
        self.personal_account_button = driver.find_element(*AuthLocators.Auth_Personal_account_Button)
        self.auth_email_button = driver.find_element(*AuthLocators.Auth_EMAIL_Button)
        time.sleep(5)

    def enter_email(self,value):
        self.email.send_keys(value)

    def enter_password(self,value):
        self.password.send_keys(value)

    def enter_phone(self, value):
        self.phone.send_keys(value)

    def enter_login(self, value):
        self.login.send_keys(value)

    def enter_login_button(self):
        self.login_button.click()

    def enter_personal_account(self, value):
        self.personal_account.send_keys(value)

    def enter_personal_account_button(self):
        self.personal_account_button.click()

    def button_click(self):
        self.button.click()

    def auth_email_button_click(self):
        self.auth_email_button.click()


