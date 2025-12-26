from data import *
from locators import IngredientPopupLocators, MainPageLocators
from pages.ingredient_popup_page import IngredientPopup
from pages.main_page import MainPage
from pages.order_feed_page import *

class TestMainFunctions:

    @allure.title("Переход на главную по клику на Конструктор")
    def test_constructor(self, driver):
        """Тест проверки перенаправления на главную страницу при клике на кнопку 'Конструктор'"""
        order_feed = OrderFeedPage(driver)
        order_feed.get_url(Urls.ORDER_FEED_PAGE)
        order_feed.wait_change_url(Urls.ORDER_FEED_PAGE)
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.check_exchange_url()
        assert main.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Переход на ленту заказов по клику на Лента заказов")
    def test_feed(self, driver):
        """Тест проверки перенаправления на страницу ленты заказов при клике на кнопку 'Лента заказов'"""
        main = MainPage(driver)
        main.get_url(Urls.MAIN_PAGE)
        main.wait_change_url(Urls.MAIN_PAGE)
        main.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_exchange_url()
        assert order_feed.get_current_url() == Urls.ORDER_FEED_PAGE

    @allure.title("Открытие и закрытие всплывающего окна с информацией об ингредиенте")
    def test_ingredient_popup(self, driver):
        """Тест проверки открытия и последующего закрытия всплывающего окна с подробностями об ингредиенте"""
        main = MainPage(driver)
        main.get_url(Urls.MAIN_PAGE)
        main.wait_change_url(Urls.MAIN_PAGE)
        main.wait_bun()
        main.click_bun()
        popup = IngredientPopup(driver)
        popup.wait_until_popup_header_visible()
        assert "ingredient" in popup.get_current_url()
        popup.close_popup()
        popup.wait_until_popup_invisible()
        assert not popup.popup_ingredient_is_active()

    @allure.title("Добавление ингредиента в заказ и изменение у него счетчика")
    def test_add_ingredient(self, driver):
        """Тест проверки добавления ингредиента в заказ и появления
        соответствующего счетчика на главной странице"""
        main = MainPage(driver)
        main.get_url(Urls.MAIN_PAGE)
        main.wait_change_url(Urls.MAIN_PAGE)
        main.ingredient_drag_and_drop()
        main.wait_counter_visible()
        assert main.fluor_bun_counter_is_active()