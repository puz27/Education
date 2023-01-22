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
        if str(profession['title']).lower() == title:
            return profession

def check_fitness(student_information, dictionary_needed_skills):
    '''Take information about student skills and compare it with needed skills for profession'''
    user_compare_information = {}
    diff_student = student_information
    diff_skills = dictionary_needed_skills

    # take info from dictionaries and put it in sets for fitness checking
    skills_student = set(diff_student['skills'])
    skills_need = set(diff_skills['skills'])

    # get skills information that student has and does not have
    skills_not_known = skills_need.difference(skills_student)
    skills_known = skills_need.intersection(skills_student)

    # get how much % of skills has student
    fit_percent = round(100 - ((100 / len(skills_need)) * len(skills_not_known)))

    # add information in dictionary
    user_compare_information['has'] = list(skills_known)
    user_compare_information['lacks'] = list(skills_not_known)
    user_compare_information['fit_percent'] = fit_percent

    return tuple(user_compare_information.values())

def check_number_input(student_number):
    '''Сheck the correct input student number'''
    while student_number.isdigit() != True:
        student_number = input("Введите номер студента\n")
    student_number = int(student_number)
    return student_number