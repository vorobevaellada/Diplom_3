from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from seletools.actions import drag_and_drop

class BasePage:

    @allure.step("Инициализация браузера")
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver_wait = WebDriverWait(self.driver, 60)

    @allure.step("Переход на указанный URL")
    def get_url(self, url):
        self.driver.get(url)

    @allure.step("Поиск нужного элемента на странице")
    def find_element(self, locator):
        return self.driver_wait.until(EC.presence_of_element_located(locator))

    @allure.step("Нажатие на найденный элемент")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Ввод текста в поле ввода")
    def text_input(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Ожидание видимости элемента на экране")
    def wait_elem_visible(self, locator):
        return self.driver_wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание исчезновения элемента с экрана")
    def wait_elem_invisible(self, locator):
        return self.driver_wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетаскивание элемента на целевой объект")
    def drag_and_drop(self, source_object, target_object):
        # Исправление проблемы стандартного метода перетаскивания Selenium
        drag_and_drop(self.driver, source_object, target_object)

    @allure.step("Ожидание готовности элемента к нажатию")
    def wait_elem_click(self, locator):
        return self.driver_wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Проверяем изменение текущего URL страницы")
    def wait_url_change(self, expected_url):
        return self.driver_wait.until(EC.url_to_be(expected_url))
    
    @allure.step("Прокрутка страницы до указанного элемента")
    def scroll_to_bottom(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)