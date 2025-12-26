from pages.base_page import *
from locators import *
import allure

class LoginPage(BasePage):

    @allure.step("Заполняем поле Email")
    def email_input(self, text):
        self.wait_elem_click(LoginPageLocators.EMAIL)
        self.click_element(LoginPageLocators.EMAIL)
        self.text_input(LoginPageLocators.EMAIL, text)

    @allure.step("Заполняем поле Пароля")
    def password_input(self, text):
        self.wait_elem_click(LoginPageLocators.PASSWORD)
        self.click_element(LoginPageLocators.PASSWORD)
        self.text_input(LoginPageLocators.PASSWORD, text)

    @allure.step("Нажимаем на кнопку Вход")
    def click_enter(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)