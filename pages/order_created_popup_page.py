import allure
from locators import OrderCreatedLocators
from pages.base_page import BasePage

class OrderCreatedPage(BasePage):
    @allure.step("Закрытие попап с инфо о создании заказа")
    def close_order_popup(self):
        self.wait_elem_visible(OrderCreatedLocators.CLOSE_BUTTON)
        self.click_element(OrderCreatedLocators.CLOSE_BUTTON)

    @allure.step("Номер заказа правильный, а не 9999")
    def order_number_accurate(self):
        try:
            self.wait_elem_invisible(OrderCreatedLocators.INCORRECT_NUMBER)
        except:
            elements = self.find_elements(OrderCreatedLocators.INCORRECT_NUMBER)
            assert len(elements) == 0

    @allure.step("Получаем номер созданного заказа")
    def get_order_number(self):
        just_created = self.wait_elem_visible(OrderCreatedLocators.CREATED_ORDER)
        return int(just_created.text)