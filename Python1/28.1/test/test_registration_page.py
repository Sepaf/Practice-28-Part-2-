# Python -m pytest -v --driver Chrome --driver-path C:/Python1/28.1/chromedriver.exe

from pages.reg_page import RegPage
import time

def test_registration_page1(selenium):
    page = RegPage(selenium)

    page.reg_registration_button_click()
    time.sleep(15)
    page.name("Сергей")
    page.surname("Иванов")
    page.email("Vhalyaminn@mail.ru")
    page.password("Asderfdcvncjfjhgyuy5")
    page.reg_password_confirmation("Asderfdcvncjfjhgyuy5")
    page.button_click()
    time.sleep(5)

    assert page.get_relative_link() != '/lk.rt.ru ', "Login Error"
    time.sleep(5)
