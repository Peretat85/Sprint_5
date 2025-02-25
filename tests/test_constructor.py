import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
#from helper import Helper
from locators import Locators

# переход В ЛК для авторизованного пользователя
class TestConstructor:
    def test_constructor(self, driver):
        # Переход на страницу авторизации (Входа)
        driver.get(Data.STELLAR)

       # нажатие на кнопку Начинки
        enter_button = driver.find_element(*Locators.STELLAR_FILLINGS)
        enter_button.click()

        # ожидаем перехода на раздел Начинок
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.text_to_be_present_in_element(Locators.STELLAR_FILLINGS_SECTION,'Начинки'))

        # нажатие на кнопку СОУСЫ
        enter_button = driver.find_element(*Locators.STELLAR_SOUS)
        enter_button.click()

        # ожидаем перехода на раздел Соусов
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_SOUS_SECTION))

        # нажатие на кнопку Булки
        enter_button = driver.find_element(*Locators.STELLAR_BUNS)
        enter_button.click()

        # ожидаем перехода на раздел Булки
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_BUNS_SECTION))
