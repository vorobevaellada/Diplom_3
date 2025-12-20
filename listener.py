import time
from selenium.webdriver.support.events import AbstractEventListener

class MyListener(AbstractEventListener):
    """Класс для того, чтобы поднимать паузу в начале открытия страницы,
    так как бывает ошибка из-за слишком быстрой попытки ввести email"""
    def after_navigate_to(self, url, driver):
        time.sleep(2)  # Глобальная пауза после открытия страницы
        print(f"Пауза после перехода на {url}")