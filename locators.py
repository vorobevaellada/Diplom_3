from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, "input[type='text'][name='name']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

class MainPageLocators:
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button[class*='button_button_type_primary']")
    FLUOR_BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_PLACE = (By.CSS_SELECTOR, ".constructor-element_pos_top")
    FLUOR_BUN_COUNTER = (By.CSS_SELECTOR, "[href*='/61c0c5a71d1f82001bdaaa6d'] [class*='counter_counter__num']")
    
class OrderFeedLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[contains(.,'Конструктор')]")
    FEED_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")
    FIRST_ORDER = (By.CSS_SELECTOR, ".OrderHistory_listItem")
    TOTAL = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_TOTAL = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")

class IngredientPopupLocators:
    INGREDIENT_HEADER = (By.XPATH, ".//h2[contains(.,'Детали ингредиента')]")
    POPUP_CLOSE_BUTTON = (By.XPATH, ".//h2[text()='Детали ингредиента']/parent::* /following-sibling::button")

class OrderCreatedLocators:
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    INCORRECT_NUMBER = (By.XPATH, ".//h2[contains(.,'9999')]")
    CREATED_ORDER = (By.XPATH, ".//h2[contains(@class,'digits-large mb-8')]")
    WAITING_FOR = (By.XPATH, ".//li[@class='text text_type_digits-default mb-2'][contains(.,'%s')]")

class OrderHistoryLocators:
    ORDER_NUMBER = (By.XPATH, ".//p[@class='text text_type_digits-default'][contains(.,'#')]")
