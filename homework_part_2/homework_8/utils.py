import os
import json
import random
from classes import *


def json_load_data(file_name):
    '''
    Считываем данные из файла
    '''
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


def load_user_statistic(questions_information_list):
    '''
    Считывает данные экземпляров из списка и выводит информацию об ответах и баллах
    '''
    score_count = 0
    count_answers = 0
    for question in questions_information_list:
        score_count += question.user_counts
        if question.user_answer is True:
            count_answers += 1
    return "Вот и всё!\nОтвечено на {} вопроса из {}\nНабрано баллов: {}".format(count_answers, len(questions_information_list), score_count)

def check_question_status(questions_information_list):
    '''
    Проверяем количество заданных вопросов
    Все значения списка будут True, когда заданы все вопросы
    '''
    data = []
    for i in questions_information_list:
        data.append(i.is_question_asked)
    return data


def main():
    '''
    Основная обработка взаимодействия с пользователем
    '''
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
            print("Вопрос: {}\nСложность: {}/5".format(current_question.user_question,
                                                       current_question.question_difficult))
            current_question.user_answer = input()
            print(current_question.build_feedback())

    # вывод статистики
    print(load_user_statistic(questions_information_list))







