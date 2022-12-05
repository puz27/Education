'''
weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for day in weekdays:
  print(day)


numbers = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000]

# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for number in numbers:
  print(number)

fruits = ["яблоко", "груша", "ананас", "апельсин", "виноград"]

element = fruits[1]

print(element)


fruits = ["яблоко", "груша"]
fruits.extend(['лимон', 'банан', 'киви'])



# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for fruit in fruits:
  print(fruit)


list_1 = ["apple", "banana", "blueberry", "strawberry", "melon"]
list_2 = ["blue", "orange", "blue", "blue", "yellow"]
list_3 = [True, False, True, True, False, True]

list_1_len = len(list_1)
list_2_len = len(list_2)
list_3_len = len(list_3)

print(list_1_len, list_2_len, list_3_len)

fruits = ["banana", "orange", "apple"]
print(f"В списке элементов: {len(fruits)}")


weekdays = [
"pirmdiena",
"otrdiena",
"trešdiena",
"ceturtdiena",
"piektdiena",
"sestdiena",
"svētdiena"]

workdays = weekdays[0:5]

# Не удаляйте код ниже, он нужен для проверки

for workday in workdays:
  print(workday)
print(workdays)

numbers = ["нула", "една", "две", "три", "четири", "пет", "шест"]
numbers[0] = "ноль"
numbers[1] = "одна"
numbers[2] = "две"
numbers[4] = "четыре"
numbers[5] = "пять"
numbers[6] = "шесть"

# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for number in numbers:
  print(number)

managers = ["Алексей", "Денис", "Юля", "Руслан",  "Алексей", "Денис", "Юля"]

managers[1] = "Татьяна"
managers[5] = "Татьяна"

# Не удаляйте код ниже, он необходим для проверки

for manager in managers:
  print(manager)

months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

months_id = int(input())

x = months_id - 1

print(months[x])


colors = ["красный", "оранжевый", "синий", "черный"]

del colors[0]

# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for color in colors:
  print(color)


colors = ["красный", "оранжевый", "красный", "синий", "красный", "черный"]
for i in colors:
  if i == "красный":
    colors.remove("красный")

# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for color in colors:
  print(color)

things = ["кошки","мышки","мошки","тотошки"]
"ошки" in things

good_food = ["яблоко", "сельдерей", "брокколи"]

questionable = input()

if questionable in good_food:
  print("Это полезно")
else:
  print("Возможно, это вредно")

active_days = [1, 5, 6, 8, 10, 12, 15, 19, 22, 27, 30]

current_day = int(input())

if current_day in active_days:
  print("Это был полезный день")
else:
  print("Это был бесполезный день")

things = ["кошки", "мышки", "мошки", "тотошки"]
# Метод pop
things.pop()
print(things)

kings = ['Генрих', 'Людовик', 'Фридрих', 'Ричард']
for i in kings:
  print(i)

keywords = ["Желание", "Семнадцать", "Пропуск", "Ржавый", "Пропуск", "Печь" ]
z = [keywords[i] for i in range(len(keywords)) if keywords[i] != 'Пропуск']
print(z)

keywords = ["Желание", "Семнадцать", "Пропуск", "Ржавый", "Пропуск", "Печь" ]
z = [i for i in keywords if i != 'Пропуск']
print('\n'.join(z))

residents = [5, 3, 2, 20, 5, 30, 5, 34]
residents_count = 0
age_sum = 0

for i in residents:
    age_sum += i
print(round(age_sum / (len(residents))))

throws = [5, 3, 2, 10, 5, 0, 5]
points = 0
for i in range(len(throws)):
    if throws[i] != 0:
        points += throws[i]
    else:
        points = points - 10
print(points)


weather = ["солнечно", "дождливо", "пасмурно",
         "солнечно", "дождливо", "дождливо",
         "солнечно"]

days_sunny = 0
days_gloomy = 0
days_rainy = 0

for day in weather:
  if day == "солнечно":
      days_sunny += 1
  if day == "пасмурно":
      days_gloomy += 1
  if day == "дождливо":
      days_rainy += 1


print(f"Солнечных дней: {days_sunny}")
print(f"Пасмурных дней: {days_gloomy}")
print(f"Дождливых дней: {days_rainy}")

i = 0
while i <= 100:
    print(i)
    i += 10


deposit = 0
fulfillment = 1500
while deposit <= 10000:
    deposit += 1500
    print(f"Баланс счета = {deposit}")

deposit = 0
fulfillment = int(input())
while deposit < 10000:
    deposit += fulfillment
    print(f"Баланс счета = {deposit}")

deposit = 0
months = 0
while deposit < 1000:
    fulfillment = int(input())
    months += 1
    deposit += fulfillment
print(months)

day = 1
distance = 2.0

while distance < 5.0:
    in_day = distance / 100 * 20
    distance += in_day
    day += 1
    print(day)

number_of_elements = 0

while True:
  user_input = input()
  number_of_elements = number_of_elements + 1
  if user_input == "stop":
      break
print(number_of_elements - 1)

expenses = 0
while True:
    answer = input()
    if answer == "стоп":
        break

    k = int(answer)
    expenses += k

print(expenses)


shopping_list = []
while True:
    answer = input()
    if answer == "стоп":
        break
    shopping_list.append(answer)

[print(el) for el in shopping_list]

x = int(input())
for i in range(1,x):
  print(i)

for i in range(0, 101, 10):
    print(i)

x, y = int(input()), int(input())
for i in range(x + 1, y):
    print(i)

words = ["Zero", "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
for i in range(1, len(words)):
    print(words[i])

words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo",
         "Foxtrot", "Golf", "Hotel", "India", "Juliett",
         "Kilo", "Lima", "Mike", "November", "Oscar",
         "Papa", "Quebec", "Romeo", "Sierra", "Tango",
         "Uniform", "Victor", "Whiskey", "X-ray", "Yankee",
         "Zulu"]
for i in range(5):
    print(words[i])

words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo",
         "Foxtrot", "Golf", "Hotel", "India", "Juliett",
         "Kilo", "Lima", "Mike", "November", "Oscar",
         "Papa", "Quebec", "Romeo", "Sierra", "Tango",
         "Uniform", "Victor", "Whiskey", "X-ray", "Yankee",
         "Zulu"]
for i in range(-5, 0):
    print(words[i])

weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
work = [True, True, True, True, True, False, False]
plans = ["за покупками", "отдыхать", "играть", "лениться", "гулять", "кутить", "страдать"]

for i in range(7):
    if work[i] == True:
        print(f"{weekdays[i]} - это рабочий день, а вечером {plans[i]}.")
    else:
        print(f"{weekdays[i]} - это выходной день, а вечером {plans[i]}.")


for toy in ['плюшевый мишка', 'мячик', 'машинка', 'конструктор', 'забытая конфета']:
    print(toy)
    if toy == "машинка":
        break

for i in range[1,5]:
    print(i)


for floor in range(1, 19):
    if floor == 4 or floor == 13:
        continue
    print(f"{floor} этаж")

items = ["Alpha", "Bravo", "Charlie"]

[print(item) for item in items]

[print(item) for item in range(6)]
'''

words = ["ракушка", "кукушка", "рыбка"]
words_with_r = [i for i in words if 'р' in i]
# Не удаляйте этот код, он нужен для проверки

[print(w) for w in words_with_r]


