# lists questions and answers
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# counter user score
score_right_answer = 0
# counter user right answers
count_right_answer = 0
# counter when user false in answer
count_false_answer = 0
# counter amount questions
count_questions = len(questions)

print(count_questions)
# Greeting
print('Привет! Предлагаю проверить свои знания английского!', 'Наберите "ready", чтобы начать!', sep='\n')

user_name = input()
print(f"Привет, {user_name}, начинаем тренировку!")

for i in range(count_questions):
    count_false_answer = 0
    print(questions[i])
    user_answer = input()

    # check user answer
    if user_answer != answers[i]:
        # if user false in answer. Give chance!
        while count_false_answer < 3:
            print(f"Осталось попыток: {3 - count_false_answer}, попробуйте еще раз!")
            user_answer = input()
            # check user answer
            if user_answer != answers[i]:
                count_false_answer += 1
            else:
                # if user right in answer
                score_right_answer += (3 - count_false_answer)
                count_right_answer += 1
                print(f"Ответ верный! Вы получаете {3 - count_false_answer} баллов!", sep="\n")
                break
        else:
            print(f"Увы, но нет. Верный ответ: {answers[i]}", sep="\n")

    # if user right in answer
    else:
        print("Ответ верный!", "Вы получаете 10 баллов!", sep="\n")
        score_right_answer += 10
        count_right_answer += 1

# Final information
percent = round(score_right_answer / (10 * count_questions) * 100)
print("")
print(f"Вот и все, {user_name}!", f"Вы ответили на {round(count_right_answer)} вопросов из {count_questions} верно.", sep="\n")
print(f"Вы заработали {score_right_answer} баллов.", f"Это {percent} процентов.", sep="\n")
