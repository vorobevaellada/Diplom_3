from pages.base_page import *
from locators import *
import allure

class LoginPage(BasePage):

    @allure.step("Заполняем поле Email")
    def email_input(self, text):
        self.wait_elem_click(LoginPageLocators.EMAIL_NOT_ACTIVE)
        self.click_element(LoginPageLocators.EMAIL_NOT_ACTIVE)
        self.text_input(LoginPageLocators.EMAIL_ACTIVE, text)

    @allure.step("Заполняем поле Пароля")
    def password_input(self, text):
        self.wait_elem_click(LoginPageLocators.PASSWORD_FIELD_NOT_ACTIVE)
        self.click_element(LoginPageLocators.PASSWORD_FIELD_NOT_ACTIVE)
        self.text_input(LoginPageLocators.PASSWORD_FIELD_ACTIVE, text)

    @allure.step("Нажимаем на кнопку Вход")
    def click_enter(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)