import allure

from data import Urls
from locators.order_locators import OrderLocators
from locators.logo_locators import LogoLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as eс


class LogoPage:

    @allure.step("Открытие браузера")
    def open_browser(self, browser):
        browser.get(Urls.MAIN_PAGE_URL)
        return self

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_order_button(self, browser):
        browser.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()
        return self

    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_button(self, browser):
        browser.find_element(*LogoLocators.SCOOTER_BUTTON).click()
        return self

    @allure.step("Клик по лого 'Дзен'")
    def click_dzen_button(self, browser):
        browser.find_element(*LogoLocators.YANDEX_BUTTON).click()
        return self

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self, browser):
        browser.switch_to.window(browser.window_handles[1])
        return self

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self, browser):
        WebDriverWait(browser, 10).until(
            eс.url_to_be(Urls.DZEN_URL))
        return self

    @allure.step("Проверка URL вкладки 'Дзен'")
    def should_dzen_url(self, browser):
        assert browser.current_url == Urls.DZEN_URL
        return self

    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def should_main_page_url(self, browser):
        assert browser.current_url == Urls.MAIN_PAGE_URL
        return self
