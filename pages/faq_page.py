from.base_page import BasePage
from locators.faq_locators import FaqLocators
import allure

class FaqPage(BasePage):
    @allure.step("Принять куки")
    def accept_cookies(self):
        if self.is_element_visible(FaqLocators.COOKIE_BANNER):
            self.click_to_element(FaqLocators.ACCEPT_COOKIES_BTN)

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, question_number):
        question_locator = self._format_question_locator(question_number)
        self.scroll_to_element(question_locator)
        self.click_to_element(question_locator)
        return self.get_text_from_element(
        self._format_answer_locator(question_number)
)

    def _format_question_locator(self, num):
        return self.format_locator(FaqLocators.QUESTION_ITEM, num)

    def _format_answer_locator(self, num):
        return self.format_locator(FaqLocators.ANSWER_ITEM, num)
