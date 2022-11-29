from selenium.webdriver.common.by import By


class AuthLocators:
    Auth_Login = (By.ID, 'username')
    Auth_Login_Button =(By.ID, 't-btn-tab-login')
    Auth_Personal_account = (By.ID, 'username')
    Auth_Personal_account_Button = (By.ID, 't-btn-tab-ls')
    Auth_Phone = (By.ID, 'username')
    Auth_EMAIL = (By.ID, 'username')
    Auth_EMAIL_Button = (By.ID, 't-btn-tab-mail')
    Auth_Password = (By.ID, 'password')
    Auth_Button = (By.XPATH, '//button[@type="submit"]')

class RegLocators:
    Reg_Name = (By.NAME, 'firstName')
    Reg_Surname = (By.NAME, 'lastName')
    Reg_Email = (By.ID, 'address')
    Reg_Password = (By.ID, 'password')
    Reg_Password_confirmation = (By.ID, 'password-confirm')
    Reg_Phone = (By.ID, 'address')
    Reg_Button = (By.XPATH, '//button[@type="submit"]')
    Reg_Registration_Button = (By.ID, 'kc-register')
