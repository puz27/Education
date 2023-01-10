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


