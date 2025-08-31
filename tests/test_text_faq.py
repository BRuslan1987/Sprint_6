import allure
import pytest
from conftest import browser
from pages.faq_page import QuestionsPage
from data import QuestionsAndAnswers


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, browser, index, question, answer):
        page = QuestionsPage()
        page.open_browser(browser)
        page.scroll_to_faq(browser)
        question_text = page.get_question(browser, index)
        answer_text = page.get_answers(browser, index)
        # Проверяем, что текст вопроса соответствует ожидаемому
        assert question_text == question
        # Проверяем, что текст ответа соответствует ожидаемому
        assert answer_text == answer
