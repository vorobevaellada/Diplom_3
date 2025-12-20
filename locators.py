from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL = (By.CSS_SELECTOR, "input.input")
    EMAIL_ACTIVE = (By.XPATH, "//input[contains(@class,'input__textfield')]")

class LoginPageLocators:
    EMAIL_NOT_ACTIVE = (By.XPATH, "//div[contains(.,'Email')]")
    EMAIL_ACTIVE = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")
    PASSWORD_FIELD_NOT_ACTIVE = (By.XPATH, "//label[contains(.,'Пароль')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")

class MainPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(.,'Лента Заказов')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")
    FLUOR_BUN = (By.XPATH, "//p[normalize-space()='Флюоресцентная булка R2-D3']")
    INGREDIENT_PLACE = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")
    FLUOR_BUN_COUNTER = (By.XPATH, "//div[1]/p[@class='counter_counter__num__3nue1' and text()='2']")

class OrderFeedLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(.,'Конструктор')]")
    FEED_HEADER = (By.XPATH, "//h1[contains(.,'Лента заказов')]")
    FIRST_ORDER = (By.XPATH, "(//h2[contains(@class,'main-medium mb-2')])[1]")
    TOTAL = (By.XPATH, "(//p[contains(@class,'digits-large')])[1]")
    TODAY_TOTAL = (By.XPATH, "(//p[contains(@class,'digits-large')])[2]")

class IngredientPopupLocators:
    INGREDIENT_HEADER = (By.XPATH, "//h2[contains(.,'Детали ингредиента')]")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//button[@type='button'][1]")

class OrderCreatedLocators:
    CLOSE_BUTTON = (By.XPATH, "//button[@type='button']")
    INCORRECT_NUMBER = (By.XPATH, "//h2[contains(.,'9999')]")
    CREATED_ORDER = (By.XPATH, "//h2[contains(@class,'digits-large mb-8')]")
    WAITING_FOR = (By.XPATH, "//li[@class='text text_type_digits-default mb-2'][contains(.,'%s')]")

class OrderHistoryLocators:
    ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default'][contains(.,'#')]")
