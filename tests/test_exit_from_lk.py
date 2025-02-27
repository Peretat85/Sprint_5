from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
#from helper import Helper
from locators import Locators

# переход В ЛК для авторизованного пользователя
class TestExit:
    def test_lk_exit(self, driver):
        # Переход на страницу авторизации (Входа)
        driver.get(Data.STELLAR_LOGIN)

        # заполняем поля входа
        # почта
        email_input = driver.find_element(*Locators.STELLAR_EMAIL_INPUT)
        email_input.send_keys(Data.STELLAR_EMAIL)

        # пароль
        password_input = driver.find_element(*Locators.STELLAR_PASSWORD_INPUT)
        password_input.send_keys(Data.STELLAR_PASSWORD)

        # нажатие на кнопку Войти
        enter_button = driver.find_element(*Locators.STELLAR_LOGIN_IN)
        enter_button.click()

        # главная страница
        WebDriverWait(driver, 10).until(EC.url_contains("stellarburgers.nomoreparties.site"))

        # нажатие на кнопку Личный кабинет
        enter_button = driver.find_element(*Locators.STELLAR_LOGIN_BUTTON_LKK)
        enter_button.click()

        # ожидание перехода на страницу профиля https://stellarburgers.nomoreparties.site/account/profile
        WebDriverWait(driver,Data.WAIT_TIME).until(EC.url_contains("profile"))

        # переход по кнопке Выход
        # нажатие на кнопку Войти
        enter_button = driver.find_element(*Locators.STELLAR_EXIT)
        enter_button.click()

        # главная страница
        WebDriverWait(driver, 10).until(EC.url_contains("login"))
        element_profile = driver.find_element(*Locators.STELLAR_LOGIN_IN)

        assert element_profile.is_displayed()