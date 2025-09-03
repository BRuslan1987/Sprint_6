import allure

from pages.logo_page import LogoPage
from data import Urls
from selenium.webdriver.support.ui import WebDriverWait

@allure.suite('Тестирование переходов с логотипа')
class TestRedirects:

    @allure.title('Проверка перехода по логотипу Самоката')
    @allure.description('Переход на главную страницу Самоката '
                        'при клике на слово Самокат в логотипе')
    def test_redirect_scooter_logo(self, driver):
        logo_page = LogoPage(driver)
        current_url = logo_page.click_scooter_logo()
        assert Urls.main_page in current_url, (
            "Переход на главную страницу Самоката не выполнен")

    @allure.title('Проверка перехода по логотипу Яндекса')
    @allure.description('Переход на главную страницу Дзена'
                        ' при клике на слово Яндекс в логотипе')
    def test_redirect_yandex_logo(self, driver):
        logo_page = LogoPage(driver)
        original_window = driver.current_window_handle
        logo_page.go_to_yandex_from_logo()
        WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
        )
        new_window = [window for window in driver.window_handles if window != original_window][0]
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 15).until(
        lambda d: d.current_url != 'about:blank'
        )
        current_url = driver.current_url
        assert Urls.dzen_page in current_url, (
        f"Ожидался URL содержащий '{Urls.dzen_page}', получено: '{current_url}'"
        )
        assert logo_page.is_dzen_logo_displayed(), "Логотип Дзена не отображается"
