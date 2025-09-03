import allure
from selenium.webdriver.common.by import By
from locators.faq_locators import FaqLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Создание заказа по кнопке в верхней части страницы')
    def create_order_from_header(self, order_dict):
        self.accept_cookies()
        self.scroll_to_element(FaqLocators.ORDER_BUTTON_HEADER)
        self.click_to_element(FaqLocators.ORDER_BUTTON_HEADER)
        self.fill_first_form(order_dict)
        self.next()
        self.fill_second_form(order_dict)
        self.submit_order()

    @allure.step('Создание заказа по кнопке в нижней части страницы')
    def create_order_from_bottom(self, order_dict):
        self.accept_cookies()
        self.scroll_page_down()
        self.scroll_to_element(OrderLocators.ORDER_BUTTON_BOTTOM)
        self.click_to_element(OrderLocators.ORDER_BUTTON_BOTTOM)
        self.fill_first_form(order_dict)
        self.next()
        self.fill_second_form(order_dict)
        self.submit_order()

    @allure.step('Переход к следующей форме')
    def next(self):
        self.scroll_to_element(OrderLocators.NEXT_BUTTON)
        self.click_to_element(OrderLocators.NEXT_BUTTON)

    @allure.step('Подтверждение заказа')
    def submit_order(self):
        self.scroll_to_element(OrderLocators.MAKE_ORDER_BUTTON)
        self.click_to_element(OrderLocators.MAKE_ORDER_BUTTON)
        self.scroll_to_element(OrderLocators.YES_BUTTON)
        self.click_to_element(OrderLocators.YES_BUTTON)

    @allure.step('Заполняем первую форму заказа "Для кого самокат"')
    def fill_first_form(self, order_dict):
        self.fill(OrderLocators.NAME_INPUT, order_dict.get('name'))
        self.fill(OrderLocators.LAST_NAME_INPUT, order_dict.get('last_name'))
        self.fill(OrderLocators.ADDRESS_INPUT, order_dict.get('address'))
        self.click_to_element(OrderLocators.METRO_INPUT)
        station_locator = OrderLocators.METRO_STATION_VISIBLE
        self.select_visible_station(station_locator, order_dict['metro'])
        self.fill(OrderLocators.PHONE_INPUT, order_dict.get('number'))

    @allure.step('Заполняем вторую форму заказа "Про аренду"')
    def fill_second_form(self, order_dict):
        self.fill_date(order_dict.get('date'))
        self.select_rental_duration(order_dict.get('duration'))
        color_locator = (OrderLocators.COLOR_BLACK_CHECKBOX
                         if order_dict.get('color') == 'black' else
                         OrderLocators.COLOR_GREY_CHECKBOX)
        self.click_to_element(color_locator)
        self.fill(OrderLocators.COMMENT_INPUT, order_dict.get('comment'))

    @allure.step('Установить дату проката')
    def fill_date(self, date_string):
        self.fill(OrderLocators.DATE_INPUT, date_string)
        self.click_by_tag_name('body')

    @allure.step('Выбор срока аренды')
    def select_rental_duration(self, duration):
        self.scroll_to_element(OrderLocators.RENTAL_DURATION_DROPDOWN)
        self.click_to_element(OrderLocators.RENTAL_DURATION_DROPDOWN)
        duration_option_locator = (
            By.XPATH,
            OrderLocators.RENTAL_DURATION_OPTION[1].format(duration)
        )
        self.scroll_to_element(duration_option_locator)
        self.click_to_element(duration_option_locator)

    @allure.step('Проверяем наличие окна с информацией о заказе')
    def check_order_status_window(self):
        return self.wait_for_element_visible(OrderLocators.STATUS_WINDOW)

    @allure.step('Выбираем станцию метро')
    def select_visible_station(self, locator, station_name):
        self.wait_for_element_visible(locator)
        stations = self.find_elements_with_wait(locator)
        for station in stations:
            if station.text.strip() == station_name:
                station.click()
                break