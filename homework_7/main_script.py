from utils import *

# load data from json files
students = json_load_data("students.json")
professions = json_load_data("professions.json")

# variables for processing our inputs
student_information = None
dictionary_needed_skills = None

# get number and find information
while student_information is None:
    student_number = check_number_input(input("Введите номер студента\n"))
    student_information = (get_student_by_pk(student_number, students))
    if student_information == None:
        print("У нас нет такого студента")

# output information about student
print(f"Студент: {student_information['full_name']}", f"Знает: {', '.join(student_information['skills'])}", sep='\n')

# get profession and find information
while dictionary_needed_skills == None:
    student_needed_profession = input(f"Выберите специальность для оценки студента {student_information['full_name']}\n").lower()
    dictionary_needed_skills = load_professions(student_needed_profession, professions)
    if dictionary_needed_skills == None:
        print("У нас нет такой профессии")

# get fitness information
student_know, student_not_know, fitness = (check_fitness(student_information, dictionary_needed_skills))

# output information
print(f"Пригодность: {fitness}")
print(f"{student_information['full_name']} знает: {', '.join(student_know)}")
print(f"{student_information['full_name']} не знает: {', '.join(student_not_know)}")