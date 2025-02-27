from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators

class TestEntranse:
    def test_entrance_index(self,driver):
        # переход на страницу входа через кнопку Войти в аккаунт
        entrance = driver.find_element(*Locators.STELLAR_BUTTON_ENTRANCE_GL)
        entrance.click()

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

       # абсолютное ожидание - до перехода на главную страницу с кнопкой "Оформить заказ"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_BUTTON_ENTRANCE))
        entrance = driver.find_element(*Locators.STELLAR_BUTTON_ENTRANCE)

        assert entrance.is_displayed()


    def test_entrance_gl_lk(self,driver):
        # переход на страницу входа через Личный кабинет
        entrance = driver.find_element(*Locators.STELLAR_LOGIN_BUTTON_LKK)
        entrance.click()

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

        # абсолютное ожидание - до перехода на главную страницу с кнопкой "Оформить заказ"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_BUTTON_ENTRANCE))
        entrance = driver.find_element(*Locators.STELLAR_BUTTON_ENTRANCE)
        #
        assert entrance.is_displayed()


    def test_entranсe_reg(self,driver):
        # переход на страницу входа через кнопку в форме регистрации
        # переход на страницу регистрации
        driver.get(Data.STELLAR_REG)
        # переход по кнопке войти
        entrance = driver.find_element(*Locators.STELLAR_LOGIN_IN_REG)
        entrance.click()

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

        # абсолютное ожидание - до перехода на главную страницу с кнопкой "Оформить заказ"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_BUTTON_ENTRANCE))
        entrance = driver.find_element(*Locators.STELLAR_BUTTON_ENTRANCE)

        assert entrance.is_displayed()


    def test_entrance_forgot(self,driver):
        # переход на страницу входа со страницы восстановления пароля
        driver.get(Data.STELLAR_FORGOT)

        # переход по кнопке войти
        entrance = driver.find_element(*Locators.STELLAR_LOGIN_IN_REG)
        entrance.click()

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

        # абсолютное ожидание - до перехода на главную страницу с кнопкой "Оформить заказ"
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_BUTTON_ENTRANCE))
        entrance = driver.find_element(*Locators.STELLAR_BUTTON_ENTRANCE)
        #
        assert entrance.is_displayed()