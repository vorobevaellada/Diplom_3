import allure
from locators import OrderCreatedLocators
from pages.base_page import BasePage
import time

class OrderCreatedPage(BasePage):

    @allure.step("Закрытие попап с инфо о создании заказа")
    def close_order_popup(self):
        time.sleep(3)
        self.wait_elem_visible(OrderCreatedLocators.CLOSE_BUTTON)
        self.click_element(OrderCreatedLocators.CLOSE_BUTTON)

    @allure.step("Номер заказа правильный, а не 9999")
    def order_number_accurate(self):
        self.wait_elem_invisible(OrderCreatedLocators.INCORRECT_NUMBER)

    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        just_created = self.wait_elem_visible(OrderCreatedLocators.CREATED_ORDER)
        return int(just_created.text)