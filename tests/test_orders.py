import allure
import pytest
from data import OrderData
from pages.order_details_page import OrderPage
from conftest import browser


class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_first_button', OrderData.FIRST_ORDER),
                                                           ('click_second_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, browser, data_order, button_method):
        page = OrderPage()

        # Открытие браузера
        page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке лендинга и в центре лендинга через параметр button_method
        getattr(page, button_method)(browser)
        # Заполнение полей для заказа, через параметр data_order
        page.user_rent_order(browser, **data_order)
        # Проверка окна подтверждения по тексту "Заказ оформлен
        page.confirmation_window(browser)
