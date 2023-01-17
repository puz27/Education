import requests
import random
from classes import *
import json
import os

def json_load_data(file_name: str) -> dict:
    '''
    load data from local file
    '''
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = random.choice(json.load(file))
    file.close()
    return data


def load_random_word(remote_data: str, local_data: str) -> BasicWord:
    '''
    load data and create instance of BasicWord class
    if problems with connection - use local data
    '''
    requests.urllib3.disable_warnings()
    response = requests.get(remote_data, verify=False)

    if response.status_code is 200:
        data = random.choice(response.json())
    else:
        print('Не удается получить доступ к внешним данным, используем локальные данные.')
        data = json_load_data(local_data)

    user_word = BasicWord((data['word']), data['subwords'])
    return user_word


def print_greetings(user: Player, load_word: BasicWord) -> None:
    '''
    print initial information for user
    '''
    print('Привет, {}!'.format(user.name))
    print('Составьте {} слов из слова {}'.format(load_word.check_count_subwords(), load_word.word.upper()))
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop(стоп)"')
    print('Поехали, ваше первое слово?')


def print_statistic(user: Player) -> None:
    print('{}\nКоличество угаданных слов: {}'.format(repr(user), len(user.used_words)))