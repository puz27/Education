import os
import json


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