import requests
import random
from classes import *
import json


def get_data(address: str) -> list:

    requests.urllib3.disable_warnings()
    response = requests.get(address, verify = False)
    data = response.json()
    return data


def load_random_word(address: str) -> BasicWord:
    data = random.choice(get_data(address))
    user_word = BasicWord((data['word']), data['subwords'])
    return user_word




