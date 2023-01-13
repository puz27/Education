count_right_answer = 0

# Greeting
print("Привет! Предлагаю проверить свои знания английского!", "Расскажи, как тебя зовут!", sep="\n")
user_name = input("")
print(f"Привет, {user_name}, начинаем тренировку!")

# First question
print("My name ___ Vova")
user_answer = input()
right_answer = "is"

# Check first question
if user_answer == right_answer:
    print("Ответ верный!", "Вы получаете 10 баллов!", sep="\n")
    count_right_answer += 1
else:
    print("Неправильно.", f"Правильный ответ: {right_answer}", sep="\n")

# Second question
print("I ___ a coder")
user_answer = input()
right_answer = "am"

# Check second question
if user_answer == right_answer:
    print("Ответ верный!", "Вы получаете 10 баллов!", sep="\n")
    count_right_answer += 1
else:
    print("Неправильно.", f"Правильный ответ: {right_answer}", sep="\n")

# Third question
print("I live ___ Moscow")
user_answer = input()
right_answer = "in"

# Check third question
if user_answer == right_answer:
    print("Ответ верный!", "Вы получаете 10 баллов!", sep="\n")
    count_right_answer += 1
else:
    print("Неправильно.", f"Правильный ответ: {right_answer}", sep="\n")

# Final information
score = count_right_answer * 10
percent = round(count_right_answer / 3 * 100)

print(f"Вот и все, {user_name}!", f"Вы ответили на {count_right_answer} вопросов из 3 верно.", sep="\n")
print(f"Вы заработали {score} баллов.", f"Это {percent} процентов.", sep="\n")