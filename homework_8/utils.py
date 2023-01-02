import os
import json


def json_load_data(file_name):
    '''Read data from json file'''
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data