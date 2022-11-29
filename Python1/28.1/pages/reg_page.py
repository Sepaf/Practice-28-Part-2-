from .base_page import BasePage
from .locators import RegLocators
import time, os


class RegPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver,timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru"
        driver.get(url)
        self.email = driver.find_element(*RegLocators.Reg_Email)
        self.password = driver.find_element(*RegLocators.Reg_Password)
        self.phone = driver.find_element(*RegLocators.Reg_Phone)
        self.button = driver.find_element(*RegLocators.Reg_Button)
        self.name = driver.find_element(*RegLocators.Reg_Name)
        self.surname = driver.find_element(*RegLocators.Reg_Surname)
        self.reg_password_confirmation = driver.find_element(*RegLocators.Reg_Password_confirmation)
        self.reg_registration_button = driver.find_element(*RegLocators.Reg_Registration_Button)
        time.sleep(5)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_phone(self, value):
        self.phone.send_keys(value)

    def enter_name(self, value):
        self.name.send_keys(value)

    def enter_surname(self, value):
        self.surname.send_keys(value)

    def button_click(self):
        self.button.click()

    def enter_password_confirmation(self, value):
        self.reg_password_confirmation.send_keys(value)

    def reg_registration_button_click(self):
        self.reg_registration_button.click()
