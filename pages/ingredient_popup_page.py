import allure
from locators import IngredientPopupLocators
from pages.base_page import BasePage

class IngredientPopup(BasePage):

    @allure.step("Проверяем отображение заголовка окна деталей ингредиента")
    def wait_until_popup_header_visible(self):
        self.wait_elem_visible(IngredientPopupLocators.INGREDIENT_HEADER)

    @allure.step("Закрываем окно, нажимая на кнопку-крестик")
    def close_popup(self):
        self.click_element(IngredientPopupLocators.POPUP_CLOSE_BUTTON)

    @allure.step("Подтверждаем закрытие окна (до момента исчезновения)")
    def wait_until_popup_invisible(self):
        self.wait_elem_invisible(IngredientPopupLocators.INGREDIENT_HEADER)