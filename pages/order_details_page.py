from .base_page import BasePage
from locators.order_locators import OrderLocators
import allure

class OrderPage(BasePage):
    @allure.step("Создать заказ через верхнюю кнопку")
    def create_order_from_header(self, order_data):
        self._fill_order_form(order_data)
        self.click_to_element(OrderLocators.HEADER_ORDER_BUTTON)
        self._wait_for_order_processing()

    @allure.step("Создать заказ через нижнюю кнопку")
    def create_order_from_bottom(self, order_data):
        self.scroll_to_element(OrderLocators.FOOTER_ORDER_BUTTON)
        self._fill_order_form(order_data)
        self.click_to_element(OrderLocators.FOOTER_ORDER_BUTTON)
        self._wait_for_order_processing()

    @allure.step("Проверить окно статуса заказа")
    def check_order_status_window(self):
        return self.is_element_visible(
            OrderLocators.ORDER_CONFIRMATION_MODAL,
            timeout=20
        )

    def _fill_order_form(self, order_data):
        self.fill_field(OrderLocators.NAME_INPUT, order_data.name)
        self.fill_field(OrderLocators.PHONE_INPUT, order_data.phone)
        self.fill_field(OrderLocators.ADDRESS_INPUT, order_data.address)
        self._select_delivery_date(order_data.delivery_date)

    def _select_delivery_date(self, date):
        self.click_to_element(OrderLocators.DATE_PICKER)
        self.select_dropdown_option(
            OrderLocators.DATE_DROPDOWN,
            visible_text=date
        )

    def _wait_for_order_processing(self):
        self.wait_for_element_visible(
            OrderLocators.PROCESSING_INDICATOR,
            timeout=15
        )
        self.wait_for_element_invisible(
            OrderLocators.PROCESSING_INDICATOR,
            timeout=30
        )
