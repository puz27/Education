words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
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
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

user_answer = {}
user_words = {}
user_difficult = ('легкий', 'средний', 'сложный')

print('Выберите уровень сложности.', 'Легкий, средний, сложный.', sep='\n')
user_input = input()
if user_input.lower() == user_difficult[0]:
    print(f'Выбран уровень сложности {user_difficult[0]}, мы предложим 5 слов, подберите перевод.')