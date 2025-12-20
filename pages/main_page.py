import allure
from data import Urls
from locators import MainPageLocators
from pages.base_page import BasePage
import time

class MainPage(BasePage):

    @allure.step("Проверяем отображение кнопки Оформить заказ")
    def check_order_button(self):
        self.wait_elem_visible(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверяем смену URL на главную страницу")
    def check_exchange_url(self):
        self.wait_url_change(Urls.MAIN_PAGE)

    @allure.step("Переходим в раздел Лента заказов")
    def click_order_feed_button(self):
        time.sleep(3)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Выбираем ингредиент Флюоресцентная булка")
    def click_bun(self):
        self.click_element(MainPageLocators.FLUOR_BUN)

    @allure.step("Проверяем наличие карточки ингредиента Флюоресцентная булка")
    def wait_bun(self):
        self.wait_elem_click(MainPageLocators.FLUOR_BUN)

    @allure.step("Перетаскиваем выбранный ингредиент в корзину")
    def ingredient_drag_and_drop(self):
        target_object = self.get_target_element()
        source_object = self.get_source_element()
        self.drag_and_drop(source_object, target_object)

    @allure.step("Проверяем появление счётчика выбранного ингредиента")
    def wait_counter_visible(self):
        self.wait_elem_visible(MainPageLocators.FLUOR_BUN_COUNTER)

    @allure.step("Инициируем оформление заказа")
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    def get_source_element(self):
        self.wait_elem_click(MainPageLocators.FLUOR_BUN)
        return self.driver.find_element(*MainPageLocators.FLUOR_BUN)

    def get_target_element(self):
        self.wait_elem_visible(MainPageLocators.INGREDIENT_PLACE)
        return self.driver.find_element(*MainPageLocators.INGREDIENT_PLACE)