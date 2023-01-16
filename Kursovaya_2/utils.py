import requests
import random
from classes import *
import json
import os

def json_load_data(file_name):
    '''
    Считываем данные из файла
    '''
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = random.choice(json.load(file))
    file.close()
    user_word = BasicWord((data['word']), data['subwords'])
    return user_word


def load_random_word(address: str) -> BasicWord:
    '''
    load data and create instance of BasicWord class
    '''
    requests.urllib3.disable_warnings()
    response = requests.get(address, verify=False)

    if response.status_code is 200:
        data = random.choice(response.json())
        user_word = BasicWord((data['word']), data['subwords'])
        return user_word
    else:
        print('Нет данных')
        exit()

def get_statistic(user_data):
    return '{}\nКоличество отгаданных слов: {}'.format(user_data.__str__(), user_data.get_count_used_words())




