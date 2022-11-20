questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
score_right_answer = 0
count_right_answer = 0
count_questions = len(questions)

print(count_questions)
# Greeting
print('Привет! Предлагаю проверить свои знания английского!', 'Наберите "ready", чтобы начать!', sep='\n')

user_name = input()
print(f"Привет, {user_name}, начинаем тренировку!")

for i in range(count_questions):
    print(questions[i])
    user_answer = input()
    if user_answer != answers[i]:
        print(f"Неправильно. Правильный ответ:{answers[i]}")

    else:
        print("Ответ верный!", "Вы получаете 10 баллов!", sep="\n")
        score_right_answer += 10
        count_right_answer += 1

# Final information
percent = round(score_right_answer / (10 * count_questions) * 100)
print(f"Вот и все, {user_name}!", f"Вы ответили на {round(count_right_answer)} вопросов из {count_questions} верно.", sep="\n")
print(f"Вы заработали {score_right_answer} баллов.", f"Это {percent} процентов.", sep="\n")