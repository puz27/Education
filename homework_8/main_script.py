from utils import *
from classes import *

# load answers from json file
questions = json_load_data("questions.json")

# list of questions
question_list= []

for question in questions:
    print(question)
    user_game = Question(question['q'])
    user_game.difficult = question['d']
    user_game.right_answer = question['a']





