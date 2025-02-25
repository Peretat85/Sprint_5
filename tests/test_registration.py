#from selenium.webdriver.ie.webdriver import WebDriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from helper import Helper
from locators import Locators

class TestLogin:
    def test_password_until_6(self,driver):
        # переход на страницу регистрации
        driver.get(Data.STELLAR_REG)
        # заполняем регистрационные поля
        # имя
        name_input = driver.find_element(*Locators.STELLAR_NAME_INPUT)
        name_input.send_keys(Data.STELLAR_NAME)

        # почта (для регистрации случайная из helper)
        email_input = driver.find_element(*Locators.STELLAR_EMAIL_INPUT)
        email_input.send_keys(Helper.generate_email())

        # пароль
        password_input = driver.find_element(*Locators.STELLAR_PASSWORD_INPUT)
        password_input.send_keys(Data.STELLAR_PASSWORD_UNT_6)

        # нажатие на кнопку Зарегистрироваться
        enter_button = driver.find_element(*Locators.STELLAR_LOGIN_BUTTON)
        enter_button.click()

        # абсолютное ожидание
        WebDriverWait(driver,Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_ENTRANCE_REG))
        entrance = driver.find_element(*Locators.STELLAR_ENTRANCE_REG)

        assert entrance.is_displayed()

    def test_login(self,driver):
        # переход на страницу регистрации
        driver.get(Data.STELLAR_REG)

        # заполняем регистрационные поля
        # имя
        name_input = driver.find_element(*Locators.STELLAR_NAME_INPUT)
        name_input.send_keys(Data.STELLAR_NAME)

        # почта (для регистрации случайная из helper)
        email_input = driver.find_element(*Locators.STELLAR_EMAIL_INPUT)
        email_input.send_keys(Helper.generate_email())

        # пароль
        password_input = driver.find_element(*Locators.STELLAR_PASSWORD_INPUT)
        password_input.send_keys(Data.STELLAR_PASSWORD)

        # нажатие на кнопку Зарегистрироваться
        enter_button = driver.find_element(*Locators.STELLAR_LOGIN_BUTTON)
        enter_button.click()

        # абсолютное ожидание
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.url_contains("login") ) # Проверяем, что URL содержит "login")
        entrance = driver.find_element(*Locators.STELLAR_LOGIN_IN)

        assert entrance.is_displayed()


