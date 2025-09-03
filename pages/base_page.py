import allure   
from locators.logo_locators import LogoLocators  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, locator):
        with allure.step(f'Клик по элементу с локатором: {locator}'):
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(locator))
            element.click()

    def get_text_from_element(self, locator):
        with allure.step(f'Получение текста из элемента'
                         f' с локатором: {locator}'):
            element = self.wait_for_element_visible(locator)
            return element.text

    # Метод, который форматирует локаторы
    @staticmethod
    def format_locators(locator_template, num):
        method, locator = locator_template
        locator = locator.format(num)
        return method, locator

    @property
    def current_url(self):
        return self.driver.current_url

    @allure.step('Заполняем поле значением')
    def fill(self, locator, value):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located
                                            (locator)).send_keys(value)

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        try:
            self.click_to_element(LogoLocators.COOKIE_BUTTON)
        except Exception as e:
            print(f"Cookie button not found or not clickable: {str(e)}")

    @allure.step('Скролл до элемента с локатором {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)

    @allure.step('Ждём и ищем элемент')
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент с локатором {locator} не "
                    f"стал видимым в течение {timeout} секунд."
        )

    @allure.step('Ждём и ищем элементы')
    def find_elements_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Элементы с локатором {locator} не "
                    f"стали видимыми в течение {timeout} секунд."
        )

    @allure.step('Скроллим в самый низ')
    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo("
                                   "0, document.body.scrollHeight);")

    @allure.step('Переключение на вкладку')
    def switch_to_tab(self, tab_index):
        try:
            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[tab_index])
        except Exception as e:
            print(f"Ошибка при переключении на вкладку {tab_index}: {str(e)}")

    @allure.step('Ищем элемент по тегу и кликаем')
    def click_by_tag_name(self, tag_name):
        with allure.step(f'Клик по элементу по тегу: {tag_name}'):
            element = self.driver.find_element(By.TAG_NAME, tag_name)
            element.click()