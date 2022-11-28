# dictionaries of words
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people" : "люди",
    "evening" : "вечер",
    "minute" : "минута",
}
words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}
words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}
# dictionaries to check user level
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
# with this dictionary user will work after he select a level
user_words = {}
# dictionary all user answers
final_user_answer = {}
# options of user game level
user_difficult = ('легкий', 'средний', 'сложный')
# number right user answers
user_right_answer = 0

# Select level
while True:
    print('Выберите уровень сложности.', 'Легкий, средний, сложный.', sep='\n')
    user_input = input()
    if user_input.lower() == user_difficult[0]:
        print(f'Выбран уровень сложности {user_difficult[0]}, мы предложим 5 слов, подберите перевод.')
        user_words = words_easy
        break
    elif user_input.lower() == user_difficult[1]:
        print(f'Выбран уровень сложности {user_difficult[1]}, мы предложим 5 слов, подберите перевод.')
        user_words = words_medium
        break
    elif user_input.lower() == user_difficult[2]:
        print(f'Выбран уровень сложности {user_difficult[2]}, мы предложим 5 слов, подберите перевод.')
        user_words = words_hard
        break

# check user answers and add results in final_user_answer
# key - word, value - translation
for key, value in user_words.items():
    print(f'{key}, {len(value)} букв, начинается на {value[0]}')
    user_answer = input().lower()
    if user_answer == user_words[key]:
        final_user_answer[key] = final_user_answer.get(key, 'True')
        print(f'Верно, {key} — это {value}.')
        print()

    else:
        final_user_answer[key] = final_user_answer.get(key, 'False')
        print(f'Неверно. {key} — это {value}.')
        print()

# print result information
print("Правильно отвечены слова:")
for answer in final_user_answer:
   if final_user_answer.get(answer) == 'True':
       user_right_answer += 1
       print(answer)
print("Неправильно отвечены слова:")

for answer in final_user_answer:
    if final_user_answer.get(answer) == 'False':
        print(answer)

print()
if user_right_answer in levels:
    print("Ваш ранг:", levels[user_right_answer], sep='\n')
