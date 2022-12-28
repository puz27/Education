from utils import *

# load data from json files
students = json_load_data("students.json")
professions = json_load_data("professions.json")

#print(get_student_by_pk(1, students))
#print((load_professions('Frontend', professions)))

# take data about student and work with it
one_student = get_student_by_pk(1, students)
one_profession = load_professions('Backend', professions)

#print(one_student['skills'])
#print(one_profession['skills'])

print(check_fitness(one_student, one_profession))