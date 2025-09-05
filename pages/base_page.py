import allure
from locators.logo_locators import LogoLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click_to_element(self, locator):
        with allure.step(f'Клик по элементу с локатором: {locator}'):
            try:
                element = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(locator))
                element.click()
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
                self.logger.error(f"Ошибка клика по элементу: {str(e)}")
                raise

    def get_text_from_element(self, locator):
        with allure.step(f'Получение текста из элемента с локатором: {locator}'):
            try:
                element = self.wait_for_element_visible(locator)
                return element.text
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
                self.logger.error(f"Ошибка получения текста: {str(e)}")
                raise

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
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).send_keys(value)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            self.logger.error(f"Ошибка заполнения поля: {str(e)}")
            raise

    @allure.step('Скролл до элемента с локатором {locator}')
    def scroll_to_element(self, locator):
        try:
            element = self.wait_for_element_visible(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            self.logger.error(f"Ошибка скролла до элемента: {str(e)}")
            raise

    @allure.step('Ждём и ищем элемент')
    def wait_for_element_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator),
                message=f"Элемент с локатором {locator} не стал видимым в течение {timeout} секунд."
            )
        except TimeoutException as e:
            self.logger.error(f"Таймаут ожидания элемента: {str(e)}")
            raise
        except NoSuchElementException as e:
            self.logger.error(f"Элемент не найден: {str(e)}")
            raise

    @allure.step('Ждём и ищем элементы')
    def find_elements_with_wait(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator),
                message=f"Элементы с локатором {locator} не стали видимыми в течение {timeout} секунд."
            )
        except TimeoutException as e:
            self.logger.error(f"Таймаут ожидания элементов: {str(e)}")
            raise
        except NoSuchElementException as e:
            self.logger.error(f"Элементы не найдены: {str(e)}")
            raise

    @allure.step('Скроллим в самый низ')
    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Переключение на вкладку')
    def switch_to_tab(self, tab_index):
        try:
            window_handles = self.driver.window_handles
            if len(window_handles) > tab_index:
                self.driver.switch_to.window(window_handles[tab_index])
            else:
                raise ValueError(f"Вкладка с индексом {tab_index} не существует")
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            self.logger.error(f"Ошибка переключения на вкладку: {str(e)}")
            raise
        except IndexError as e:
            self.logger.critical(f"Попытка доступа к несуществующей вкладке: {str(e)}")
            raise

    @allure.step('Ищем элемент по тегу и кликаем')
    def click_by_tag_name(self, tag_name):
        with allure.step(f'Клик по элементу по тегу: {tag_name}'):
            try:
                element = self.driver.find_element(By.TAG_NAME, tag_name)
                element.click()
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
                self.logger.error(f"Ошибка клика по тегу: {str(e)}")
                raise
