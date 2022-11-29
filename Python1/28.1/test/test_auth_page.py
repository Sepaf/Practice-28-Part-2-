# Python -m pytest -v --driver Chrome --driver-path C:/Python1/28.1/chromedriver.exe
from pages.auth_page import AuthPage
import time

# некорректные данные неправильно указан мобильный телефон
def test_auth_page1(selenium):
    page = AuthPage(selenium)

    page.enter_phone("8 911 345 56 ")
    page.enter_password("Asderfdcvncjfjhgyuy5")
    page.button_click()
    time.sleep(5)

    assert page.get_relative_link() != '/lk.rt.ru ', "Phone Error"
    time.sleep(5)

# Некорректный адрес электронной почты
def test_auth_page2(selenium):
    page = AuthPage(selenium)

    page.auth_email_button_click()
    page.enter_email("USeruser@mil.ru ")
    page.enter_password("Asderfdcvncjfjhgyuy5")
    page.button_click()
    time.sleep(5)

    assert page.get_relative_link() != '/lk.rt.ru ', "Неверный логин или пароль"
    time.sleep(5)

# Некорректный логин пользователя
def test_auth_page3(selenium):
    page = AuthPage(selenium)

    page.login_button.click()
    page.enter_login("!№;:*?:;№Ээ")
    page.enter_password("Asderfdcvncjfjhgyuy5")
    page.button_click()
    time.sleep(5)

    assert page.get_relative_link() != '/lk.rt.ru ', "Неверный логин или пароль"
    time.sleep(5)

# Некорректный лицевой счет пользователя
def test_auth_page4(selenium):
    page = AuthPage(selenium)

    page.personal_account_button.click()
    time.sleep(5)
    page.personal_account("1233445654322345")
    page.enter_password("Asderfdcvncjfjhgyuy5")
    page.button_click()
    time.sleep(5)

    assert page.get_relative_link() != '/lk.rt.ru ', "Неверный номер лицевого счета или пароль"
    time.sleep(5)