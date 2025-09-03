import allure

from data import OrderData
from pages.order_details_page import OrderPage
import sys
sys.path.insert(0, '/Users/Ruslan/Sprint_6')


@allure.suite('Тестирование страницы заказа')
class TestOrderPage:

    @allure.title('Тест создания заказа: Первый сценарий')
    @allure.description('Позитивный сценарий создания заказа'
                        ' через верхнюю кнопку')
    def test_create_order_from_header(self, driver):
        order_page = OrderPage(driver)
        order_info = OrderData.FIRST_ORDER
        order_page.create_order_from_header(order_info)
        assert order_page.check_order_status_window(), (
            "Окно с информацией о заказе не появилось")

    @allure.title('Тест создания заказа: Второй сценарий')
    @allure.description('Позитивный сценарий создания заказа'
                        ' через нижнюю кнопку')
    def test_create_order_from_bottom(self, driver):
        order_page = OrderPage(driver)
        order_info = OrderData.SECOND_ORDER
        order_page.create_order_from_bottom(order_info)

        assert order_page.check_order_status_window(), (
            "Окно с информацией о заказе не появилось")
