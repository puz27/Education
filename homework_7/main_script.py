from utils import *

# load data from json files
students = json_load_data("students.json")
professions = json_load_data("professions.json")
print(students)

# take data about student and work with it

student_information = None

while student_information is None:
    student_number = int(input("Введите номер студента\n"))
    student_information = (get_student_by_pk(student_number, students))
    if student_information == None:
        print("У нас нет такого студента")

#print(student_information)
print(f"Студент: {student_information['full_name']}", f"Знает: {', '.join(student_information['skills'])}", sep='\n')

dictionary_needed_skills = None
while dictionary_needed_skills == None:
    student_needed_profession = input(f"Выберите специальность для оценки студента {student_information['full_name']}\n").lower()
    # load from dictionary of skills that we want to find
    dictionary_needed_skills = load_professions(student_needed_profession, professions)
    if dictionary_needed_skills == None:
        print("У нас нет такой профессии")


#print(check_fitness(student_information, dictionary_needed_skills))
student_know, student_not_know, fitness = (check_fitness(student_information, dictionary_needed_skills))
print(f"Пригодность: {fitness}")
print(f"{student_information['full_name']} знает: {', '.join(student_know)}")
print(f"{student_information['full_name']} не знает: {', '.join(student_not_know)}")