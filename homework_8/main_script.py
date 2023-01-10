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
    #print(question)
    questions_information_list.append(Question(question['q'], question['d'], question['a']))


#print(questions_information_list)
#print(random.choice(questions_information_list))
#current = random.choice(questions_information_list)


for user_round in questions_information_list:
    print("Вопрос: {} {}\nСложность: {}/5".format(user_round.user_question, user_round.right_answer, user_round.question_difficult))
    user_round.user_answer = input()
    print(user_round.build_feedback())








