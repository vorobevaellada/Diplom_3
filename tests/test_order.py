import allure
from data import *
from locators import OrderCreatedLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_created_popup_page import OrderCreatedPage

class TestOrderFeed:
    @allure.title("При создании заказа Выполнено за всё время счётчик увеличивается")
    def test_alltime(self, driver, registration):
        """Проверяется увеличение общего количества выполненных заказов после создания нового заказа."""
        login_page = LoginPage(driver)
        login_page.get_url(Urls.LOGIN_PAGE)
        login_page.email_input(registration['email'])
        login_page.password_input(registration['password'])
        login_page.click_enter()
        main_page = MainPage(driver)
        main_page.check_order_button()
        assert driver.current_url == Urls.MAIN_PAGE
        main_page.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_header()
        result = order_feed.wait_head()
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.check_order_button()
        main.ingredient_drag_and_drop()
        main.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.order_number_accurate()
        popup.close_order_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed_return = OrderFeedPage(driver)
        assert order_feed_return.wait_head() == result + 1

    @allure.title("При создании нового заказа Выполнено за сегодня счётчик увеличивается")
    def test_today(self, driver, registration):
        """Проверяется увеличение количества выполненных заказов за сегодняшний день после создания нового заказа."""
        login_page = LoginPage(driver)
        login_page.get_url(Urls.LOGIN_PAGE)
        login_page.email_input(registration['email'])
        login_page.password_input(registration['password'])
        login_page.click_enter()
        main_page = MainPage(driver)
        main_page.check_order_button()
        assert driver.current_url == Urls.MAIN_PAGE
        main_page.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_header()
        order_feed.scroll_today_count()
        number = order_feed.get_today_orders_count()
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.check_order_button()
        main.ingredient_drag_and_drop()
        main.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.order_number_accurate()
        popup.close_order_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed_return = OrderFeedPage(driver)
        order_feed_return.scroll_today_count()
        assert order_feed_return.get_today_orders_count() == number + 1

    @allure.title("Проверяем отображение созданного заказа в разделе В работе")
    def test_in_work(self, driver, registration):
        """Проверяется отображение недавно созданного заказа в секции заказов 'В работе'."""
        login_page = LoginPage(driver)
        login_page.get_url(Urls.LOGIN_PAGE)
        login_page.email_input(registration['email'])
        login_page.password_input(registration['password'])
        login_page.click_enter()
        main_page = MainPage(driver)
        main_page.check_order_button()
        assert driver.current_url == Urls.MAIN_PAGE
        main_page.ingredient_drag_and_drop()
        main_page.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.order_number_accurate()
        number = popup.get_order_number()
        popup.close_order_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_header()
        specific_locator = (OrderCreatedLocators.WAITING_FOR[0],
                            OrderCreatedLocators.WAITING_FOR[1] % number)
        element = order_feed.wait_elem_visible(specific_locator)
        assert element.is_displayed()