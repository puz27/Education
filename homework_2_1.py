'''
number = input()
if int(number) == 0:
    print("ноль")
elif int(number) == 1:
    print("один")
elif int(number) == 2:
    print("два")
elif int(number) == 3:
    print("три")
elif int(number) == 4:
    print("четыре")

score = int(input())
age = int(input())

if (score >= 20) and (age >= 18):
    print("Вот ваши права")
else:
    print("Мы не можем выдать вам права")


temp = float(input())

if temp < 36.5:
    print("Температура понижена")
elif 36.5 <= temp <= 36.7:
    print("Температура в норме")
elif temp > 36.7:
    print("Температура повышена")

answer = input()
correct_answer = input()

if answer == correct_answer:
    is_correct = True
else:
    is_correct = False

word1 = input()
word2 = input()

counter = 0

if "р" in word1:
  counter += 1

if "р" in word2:
    counter += 1

print(counter)

residency = int(input())
salary = int(input())
experience = int(input())

counter = 0

if residency >= 2:
    counter += 1
if salary >= 50000:
    counter += 1
if experience >= 2:
    counter += 1

print(f"Ваш кредитный рейтинг - {counter}")


price = 300
money = 500
print(type(price > money))


#Введите оценку звездочками ***
stars = input()
if stars == '*':
    print("Ужасно")
if stars == '**':
    print("Очень плохо")
if stars == '***':
    print("Средненько")
if stars == '****':
    print("Всё в порядке")
if stars == '*****':
    print("Прекрасная поездка!")


age = int(input())

if age < 7:
  print("бесплатно")
elif 7 <= age <= 17:
    print("100 рублей")
elif 18 <= age <= 24:
    print("200 рублей")
elif 25 <= age <= 60:
    print("300 рублей")
elif age > 60:
    print("бесплатно")


water_delivered = int(input())

if 20000 <= water_delivered < 30000:
    bonus_percent = 10
elif water_delivered >= 30000:
    bonus_percent = 20
else:
    bonus_percent = 0


print(f"Бонус = {bonus_percent}%")

n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

result = n_1 + n_2 + n_3

print(result)


a = int(input())
b = int(input())

if a >= 0 or b >= 0:
    print("Есть положительное число")
else:
    print("Нет положительных чисел")

space_total = 110
space_os = 30
space_docs = 22
space_free = space_total - space_os - space_docs

print(space_free)

summ = int(input())

# Половина
half = round(summ / 2, 1)
# Четверть
quarter = round(summ * 0.25, 1)
# Десятая часть
decimal = round(summ * 0.1, 1)

print("Половина", half)
print("Четверть", quarter)
print("Десятая", decimal)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

min_of = min(number_1, number_2, number_3)
max_of = max(number_1, number_2, number_3)
avg_of = round((number_1 + number_2 + number_3) / 3)

print(f"Минимум: {min_of}")
print(f"Максимум: {max_of}")
print(f"Среднее: {avg_of}")


number = int(input())

number_exp_2 = number ** 2
number_exp_3 = pow(number, 3)
number_exp_4 = pow(number, 4)

print(number_exp_2)
print(number_exp_3)
print(number_exp_4)


income = int(input())

necessity_jar = round(income / 100 * 55) # Текущие расходы
financial_freedom_jar = round(income * 0.1)  # Финансовая свобода
education_jar = round(income * 0.1)  # Образование
savings_jar = round(income * 0.1) # Резервный фонд
play_jar = round(income * 0.1) # Развлечения
give_jar = round(income * 0.05) # Благотворительность и подарки

print(f"Текущие расходы {necessity_jar}")
print(f"Финансовая свобода {financial_freedom_jar}")
print(f"Образование {education_jar}")
print(f"Резервный фонд {savings_jar}")
print(f"Развлечения {play_jar}")
print(f"Благотворительность и подарки {give_jar}")

number = int(input())

if number % 3 == 0:
    print("Число делится на 3")
else:
    print("Число НЕ делится на 3")

number_of_students = int(input())

number_of_groups = number_of_students // 4

print(f"Получится {number_of_groups} полных групп")
'''

students_count = int(input())
students_online = int(input())

online_percent = students_online / students_count * 100
print(f"На встречу пришло {round(online_percent)} процентов")