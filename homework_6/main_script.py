import os
import random

# counter right user answers
count_right_answer = 0


def change_word(word):
    """Mix letter in word"""
    slovo_as_list = random.sample(word, len(word))
    return(''.join(slovo_as_list))


def read_words_from_file(file_name):
    """Read words from file, add it to list for user questions"""
    user_questions = []
    path_file_questions = os.path.join(os.getcwd(), file_name)
    with open(path_file_questions) as file:
        for i in file:
            user_questions.append(i.rstrip())
    return (user_questions)


def write_statistic_to_file(user_name, count_right_answer, file_name):
    """Write user name and user counts to file"""
    user_statistic = user_name + ' ' + str(count_right_answer) + '\n'
    path_file_statistic = os.path.join(os.getcwd(), file_name)
    with open(path_file_statistic, 'a') as file:
        file.write(user_statistic)


def show_statistic_from_file(file_name):
    """Take information from file with game statistic and show it"""
    counter_games = 0
    # list where we add all results and after will find best result
    user_results = []
    path_file_statistic = os.path.join(os.getcwd(), file_name)
    with open(path_file_statistic, 'r') as file:
        for i in file:
            counter_games += 1
            user_result = i.rstrip().split(' ')
            user_results.append(user_result)

            max_count = 0
            max_count_user_name = ''
            #print(user_results)
            for i in range(len(user_results)):
                #print(user_results[i][1])
                if int(user_results[i][1]) >= max_count:
                    max_count = int(user_results[i][1])
                    max_count_user_name = user_results[i][0]

        #print(max_count_user_name, max_count)
        return counter_games, max_count_user_name, max_count


# start game
user_name = input("Введите ваше имя\n")

# read words from file
user_question = read_words_from_file("words.txt")

# user answer on questions. count the number of user points
for i in range(len(user_question)):
    print(user_question[i])
    print(f"Угадайте слово: {change_word(user_question[i])}")
    if input() == user_question[i]:
        print("Верно! Вы получаете 10 очков.")
        count_right_answer += 10
    else:
        print(f"Неверно! Верный ответ – {user_question[i]}")

# write user game statistic to file
write_statistic_to_file(user_name, count_right_answer, "history.txt")

# read & show user game statistic
statistic_from_file = show_statistic_from_file("history.txt")
print(f"\nВсего игр сыграно: {statistic_from_file[0]}\nВаш результат: {count_right_answer}\nМаксимальный рекорд у пользователя с именем {statistic_from_file[1]}: {statistic_from_file[2]}")