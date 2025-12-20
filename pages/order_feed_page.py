import allure
from data import Urls
from locators import OrderFeedLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):

    @allure.step("Клик на Конструктор")
    def click_constructor_button(self):
        self.click_element(OrderFeedLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Изменение url на Ленту заказов")
    def wait_exchange_url(self):
        self.wait_url_change(Urls.ORDER_FEED_PAGE)

    @allure.step("Отображение заголовка Ленты заказов")
    def wait_header(self):
        self.wait_elem_visible(OrderFeedLocators.FEED_HEADER)

    @allure.step("Клик на заказ в ленте")
    def click_order(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER)

    @allure.step("Полное количество заказов")
    def wait_head(self):
        element = self.wait_elem_visible(OrderFeedLocators.TOTAL)
        return int(element.text)

    @allure.step("Количество заказов за текущий день")
    def get_today_orders_count(self):
        element = self.wait_elem_visible(OrderFeedLocators.TODAY_TOTAL)
        return int(element.text)

    @allure.step("Скролл до кноки Заказать")
    def scroll_today_count(self):
        button = self.find_element(OrderFeedLocators.TODAY_TOTAL)
        self.scroll_to_bottom(button)
