import random

from utils import *
from classes import *

# load answers from json file
questions_information = json_load_data("questions.json")

# list of questions
questions_information_list = []
result_user_counts = 0

#random.shuffle(questions_information)

for question in questions_information:
    questions_information_list.append(Question(question['q'], question['d'], question['a']))

#data = []
#for i in questions_information_list:
    #data.append(i.is_question_asked)


while all(check_question_status(questions_information_list)) is False:

    current_question = random.choice(questions_information_list)

    if current_question.is_question_asked is False:
        print("Вопрос: {} {}\nСложность: {}/5".format(current_question.user_question, current_question.right_answer, current_question.question_difficult))
        current_question.user_answer = input()
        print(current_question.build_feedback())


print(show_statistic(questions_information_list))







