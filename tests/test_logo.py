import allure
from pages.logo_page import LogoPage
from data import Urls

@allure.suite('Тестирование переходов с логотипа')
class TestRedirects:

    @allure.title('Проверка перехода по логотипу Самоката')
    def test_redirect_scooter_logo(self, driver):
        logo_page = LogoPage(driver)
        current_url = logo_page.click_scooter_logo()
        assert Urls.main_page in current_url, "Не произошел переход на главную страницу Самоката"

    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_redirect_yandex_logo(self, driver):
        logo_page = LogoPage(driver)
        current_url = logo_page.click_yandex_logo()
        
        assert Urls.dzen_page in current_url, f"Ожидался URL содержащий '{Urls.dzen_page}', получен: '{current_url}'"
        assert logo_page.is_dzen_logo_visible(), "Логотип Дзена не отображается на странице"
