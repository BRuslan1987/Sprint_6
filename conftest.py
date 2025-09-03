import allure
import pytest

from selenium import webdriver
from data import Urls



@pytest.fixture()
@allure.title("Подготовка драйвера")
def driver():
    firefox_options = webdriver.FirefoxOptions()  # создали объект для опций
    firefox_options.add_argument('--width=1920')
    firefox_options.add_argument('--height=1200')
    driver = webdriver.Firefox(options=firefox_options)  # инициализируем драйвер
    driver.get(Urls.main_page)  # переходим на основной url
    yield driver  # передаём драйвер в тесты
    driver.quit()  # закрываем драйвер