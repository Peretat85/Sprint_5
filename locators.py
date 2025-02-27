from selenium.webdriver.common.by import By

class Locators:
    # поля регистрации/входа
    STELLAR_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # поле имени | test_registration
    STELLAR_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле майл | test_registration | test_entrance
    STELLAR_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # поле пароля | test_registration | test_entrance

    # кнопка Зарегистрироваться https://stellarburgers.nomoreparties.site/register
    STELLAR_LOGIN_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # test_registration

    # кнопка Личный кабинет вверху справа
    STELLAR_LOGIN_BUTTON_LKK = (By.LINK_TEXT, "Личный Кабинет") #test_entrance

    # Кнопка на главной
    STELLAR_BUTTON_ENTRANCE_GL = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка активна после авторизации
    STELLAR_BUTTON_ENTRANCE = (By.XPATH, "//button[text()='Оформить заказ']") #

    # кнопка Войти на странице https://stellarburgers.nomoreparties.site/login
    STELLAR_LOGIN_IN = (By.XPATH, "//button[text()='Войти']") # | test_registration

    # надпись Войти на других страницах
    STELLAR_LOGIN_IN_REG = (By.LINK_TEXT, "Войти")

    # кнопка выхода из ЛК
    STELLAR_EXIT = (By.XPATH, "//button[text()='Выход']")

    # сообщение о некорректном пароле
    STELLAR_ENTRANCE_REG = (By.XPATH, "//p[text()='Некорректный пароль']") # test_registration

    # надпись профиль на странице профиля
    STELLAR_PROFILE_TEXT = (By.XPATH, "//a[text()='Профиль']")

    # страница Конструктора
    STELLAR_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

    # страница с конструктором "Соберите бургер"
    STELLAR_CONSTRUCTOR_TEXT = (By.XPATH, "//p[text()='Конструктор']")

    # логотип
    STELLAR_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    # меню ингредиентов
    STELLAR_FILLINGS = (By.XPATH, "//span[text()='Начинки']")
    STELLAR_SOUS = (By.XPATH, "//span[text()='Соусы']")
    STELLAR_BUNS = (By.XPATH, "//span[text()='Булки']")

    # разделы ингредиентов
    STELLAR_FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    STELLAR_SOUS_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    STELLAR_BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")