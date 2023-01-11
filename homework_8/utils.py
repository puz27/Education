import os
import json


def json_load_data(file_name):
    '''Read data from json file'''
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data

def load_user_statistic(questions_information_list):
    result_count = 0
    right_answers = 0
    pass

def show_statistic(questions_information_list):
    score_count = 0
    count_answers = 0
    for queation in questions_information_list:
        score_count += queation.user_counts
        if queation.user_answer is True:
            count_answers += 1
    return "Вот и всё!\nОтвечено на {} вопроса из {}\nНабрано баллов: {}".format(count_answers, len(questions_information_list), score_count)

def check_question_status(questions_information_list):
    data = []
    for i in questions_information_list:
        data.append(i.is_question_asked)
    return data