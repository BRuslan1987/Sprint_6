import allure
import pytest

from data import QuestionsAndAnswers
from pages.faq_page import FaqPage

@allure.suite('Проверяем FAQ')
class TestMainPage:

    @allure.title("Проверка ответов на вопросы")
    @allure.description("Принимаем куки, скроллим страницу в самый низ, "
                        "кликаем поочерёдно на каждый вопрос и "
                        "сравниваем полученный ответ с ответом из словаря")
    @pytest.mark.parametrize("question_data", 
                            QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST,
                            ids=lambda data: f"Вопрос {data[0]}: {data[1]}")  # Читаемые имена тестов
    def test_questions_and_answers(self, driver, question_data):
        faq_page = FaqPage(driver)
        
        with allure.step('Принимаем куки'):
            faq_page.accept_cookies()

        # Распаковываем кортеж на составляющие
        question_number, question_text, expected_answer = question_data  # Фикс 1

        with allure.step(f'Кликаем на вопрос "{question_text}" и проверяем ответ'):
            # Получаем текст ответа по номеру вопроса
            actual_answer = faq_page.get_answer_text(question_number)  # Фикс 2
        
            # Проверяем соответствие ответа
            assert actual_answer == expected_answer, (  # Фикс 3
                f'Для вопроса "{question_text}":\n'
                f'Ожидался ответ: "{expected_answer}"\n'
                f'Фактический ответ: "{actual_answer}"'
            )

