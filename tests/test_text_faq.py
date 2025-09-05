import allure
import pytest
from data import QuestionsAndAnswers
from pages.faq_page import FaqPage

@allure.suite('Проверяем FAQ')
class TestMainPage:
    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize("question_data", 
    QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST,
    ids=lambda data: f"Вопрос {data[0]}: {data[1]}")
    def test_questions_and_answers(self, driver, question_data):
        faq_page = FaqPage(driver)
 
    with allure.step('Инициализация теста'):
        faq_page.accept_cookies()
 
    question_number, question_text, expected_answer = question_data
 
    with allure.step(f'Проверка вопроса #{question_number}'):
        actual_answer = faq_page.get_answer_text(question_number)
 
    assert actual_answer == expected_answer, (
    f'Ошибка в вопросе "{question_text}":\n'
    f'Ожидалось: "{expected_answer}"\n'
    f'Получено: "{actual_answer}"'
)
