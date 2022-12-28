from utils import *

# load data from json files
students = json_load_data("students.json")
professions = json_load_data("professions.json")

#print(get_student_by_pk(1, students))
#print((load_professions('Frontend', professions)))

# take data about student and work with it
#one_student = get_student_by_pk(1, students)
#student_skills = load_professions('Backend', professions)

#print(one_student['skills'])
#print(one_profession['skills'])

#print(check_fitness(one_student, one_profession))

student_number = int(input("Введите номер студента\n"))

# dictionary of all student information
student_information = (get_student_by_pk(student_number, students))

print(student_information)
print(f"Студент: {student_information['full_name']}", f"Знает: {', '.join(student_information['skills'])}", sep='\n')
student_needed_profession = input(f"Выберите специальность для оценки студента {student_information['full_name']}\n")

# load from dictionary of skills that we want to find
dictionary_needed_skills = load_professions(student_needed_profession, professions)

#print(check_fitness(student_information, dictionary_needed_skills))
student_know, student_not_know, fitness = (check_fitness(student_information, dictionary_needed_skills))
print(f"Пригодность: {fitness}")
print(f"{student_information['full_name']} знает: {', '.join(student_know)}")
print(f"{student_information['full_name']} не знает: {', '.join(student_not_know)}")