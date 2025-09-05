import allure
from data import OrderData
from pages.order_details_page import OrderPage

@allure.suite('Тестирование страницы заказа')
class TestOrderPage:
    @allure.title('Создание заказа через верхнюю кнопку')
    def test_create_order_from_header(self, driver):
        order_page = OrderPage(driver)
        order_page.create_order_from_header(OrderData.FIRST_ORDER)
        assert order_page.check_order_status_window(), (
            "Окно подтверждения заказа не отображается"
        )

    @allure.title('Создание заказа через нижнюю кнопку')
    def test_create_order_from_bottom(self, driver):
        order_page = OrderPage(driver)
        order_page.create_order_from_bottom(OrderData.SECOND_ORDER)
        assert order_page.check_order_status_window(), (
            "Окно подтверждения заказа не отображается"
        )
