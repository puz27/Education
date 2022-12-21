import os
import random

def change_word(word):
    slovo_as_list = random.sample(word, len(word))
    return(''.join(slovo_as_list))

def read_words_from_file(file_name):
    user_questions = []
    path_file_questions = os.path.join(file_name)
    with open(path_file_questions) as file:
        for i in file:
            user_questions.append(i.rstrip())
    return (user_questions)

def write_statistic_to_file(user_name, count_right_answer, file_name):
    user_statistic = user_name + ' ' + str(count_right_answer) + '\n'
    path_file_statistic = os.path.join(file_name)
    with open(path_file_statistic, 'a') as file:
        file.write(user_statistic)

#print("Введите ваше имя")
user_name = input()

# counter for answer
count_right_answer = 0

user_question = read_words_from_file("words.txt")

for i in range(len(user_question)):
    print(user_question[i])
    print(f"Угадайте слово: {change_word(user_question[i])}")
    if input() == user_question[i]:
        print("Верно! Вы получаете 10 очков.")
        count_right_answer += 10
    else:
        print(f"Неверно! Верный ответ – {user_question[i]}")

write_statistic_to_file(user_name, count_right_answer, "history.txt")

counter_games = 0
user_results = []
with open("history.txt", 'r') as file:
    for i in file:
        counter_games += 1
        user_result = i.rstrip().split(' ')
        user_results.append(user_result[1])
    print(counter_games)
print(max(user_results))
