from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators

# тест перехода в раздел Начинок
class TestConstructor:
    def test_constructor_fillings(self, driver):
        # Переход на страницу авторизации (Входа)
        driver.get(Data.STELLAR)

       # нажатие на кнопку Начинки
        enter_button = driver.find_element(*Locators.STELLAR_FILLINGS)
        enter_button.click()

        # ожидаем перехода на раздел Начинок
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_FILLINGS_SECTION))

        fillings_view = driver.find_element(*Locators.STELLAR_FILLINGS_SECTION)
        assert fillings_view.is_displayed()

# тест перехода в раздел Соусы
    def test_constructor_sous(self,driver):
        # Переход на страницу авторизации (Входа)
        driver.get(Data.STELLAR)

        # нажатие на кнопку СОУСЫ
        enter_button = driver.find_element(*Locators.STELLAR_SOUS)
        enter_button.click()

        # ожидаем перехода на раздел Соусов
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_SOUS_SECTION))

        sous_view = driver.find_element(*Locators.STELLAR_SOUS_SECTION)
        assert sous_view.is_displayed()

# тест перехода в раздел Булки
    def test_constructor_buns(self,driver):
        # Переход на страницу авторизации (Входа)
        driver.get(Data.STELLAR)

        # скроллинг вниз, чтобы скрыть раздел Булки
        # нажатие на кнопку Начинки
        enter_button = driver.find_element(*Locators.STELLAR_FILLINGS)
        enter_button.click()
        # ожидаем перехода на раздел Начинок
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_FILLINGS_SECTION))

        # нажатие на кнопку Булки
        enter_button = driver.find_element(*Locators.STELLAR_BUNS)
        enter_button.click()

        # ожидаем перехода на раздел Булки
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_BUNS_SECTION))

        buns_view = driver.find_element(*Locators.STELLAR_BUNS_SECTION)
        assert buns_view.is_displayed()