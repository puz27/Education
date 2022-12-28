import os
import json


def json_load_data(file_name):
    '''Read data from json file'''
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


def get_student_by_pk(pk, dictionary):
    '''Find student by key'''
    for student in dictionary:
        if student['pk'] == pk:
            return student


def load_professions(title, dictionary):
    '''Find profession by title'''
    for profession in dictionary:
        if profession['title'] == title:
            return profession

def check_fitness(student_information, dictionary_needed_skills):
    '''Take information about student skills and compare it with needed skills for profession'''
    user_compare_information = {}

    diff_student = student_information
    diff_skills = dictionary_needed_skills

    skills_student = set(diff_student['skills'])
    skills_need = set(diff_skills['skills'])

    # student do not have this skills
    skills_not_known = skills_need.difference(skills_student)
    skills_known = skills_need.intersection(skills_student)
    # print("у пользователя:", skills_student, len(skills_student))
    # print("пользователь не знает:", skills_not_known, len(skills_not_known))
    # print("все что нужно знать:", skills_need, len(skills_need))

    # how much % of skills has student
    fit_percent = round(100 - ((100 / len(skills_need)) * len(skills_not_known)))

    # add information in dictionary
    user_compare_information['has'] = list(skills_known)
    user_compare_information['lacks'] = list(skills_not_known)
    user_compare_information['fit_percent'] = fit_percent

    return tuple(user_compare_information.values())
