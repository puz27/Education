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

# Greeting
print('Привет! Предлагаю проверить свои знания английского!', 'Наберите "ready", чтобы начать!', sep='\n')
user_command = input()
if user_command == 'ready':

    for i in range(count_questions):
        count_false_answer = 0

        # check user answer
        print(questions[i])
        user_answer = input()

        # if user false in answer. Give chance!
        if user_answer != answers[i]:
            # user has 3 attemps
            while count_false_answer < 3:
                print(f"Осталось попыток: {3 - count_false_answer}, попробуйте еще раз!")
                user_answer = input()
                # check user answer
                if user_answer != answers[i]:
                    # numbers of user attemps
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
    print("")
    print(f"Вот и все!", f"Вы ответили на {round(count_right_answer)} вопросов из {count_questions} верно.", sep="\n")
    print(f"Вы заработали {score_right_answer} баллов.")

else:
    print('Кажется, вы не хотите играть. Очень жаль.')
