import random
from utils import *
from classes import *

# загрузка информации из json
questions_information = json_load_data("questions.json")

# создаем список с экземплярами вопросов и нужной информации для обработки этих вопросов
questions_information_list = []
for question in questions_information:
    questions_information_list.append(Question(question['q'], question['d'], question['a']))

# проверка заданы ли все вопросы
while all(check_question_status(questions_information_list)) is False:

    # рандомно тянем экземпляр из списка для обработки
    current_question = random.choice(questions_information_list)

    # задаем вопрос, если он еще не был задан
    if current_question.is_question_asked is False:
        print("Вопрос: {} {}\nСложность: {}/5".format(current_question.user_question, current_question.right_answer, current_question.question_difficult))
        current_question.user_answer = input()
        print(current_question.build_feedback())

# вывод статистики
print(load_user_statistic(questions_information_list))







