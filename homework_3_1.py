# lists questions and answers
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# counter user right answers
count_right_answer = 0
# counter amount questions
count_questions = len(questions)

# Greeting
print('Привет! Предлагаю проверить свои знания английского!', 'Наберите "ready", чтобы начать!', sep='\n')
user_command = input()
if user_command == 'ready':

    # check user answer
    for i in range(count_questions):
        print(questions[i])
        user_answer = input()
        if user_answer != answers[i]:
            print(f"Неправильно. Правильный ответ:{answers[i]}")

        else:
            print("Ответ верный!")
            count_right_answer += 1

    # Final information
    percent = round(count_right_answer / count_questions * 100)
    print()
    print(f"Вот и все! Вы ответили на {count_right_answer} вопросов из {count_questions} верно.", sep="\n")
    print(f"Это {percent} процентов.", sep="\n")

# user do not want to play
else:
    print('Кажется, вы не хотите играть. Очень жаль.')