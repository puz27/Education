'''
students = {
  "Алиса": 70,
  "Эльдар" : 20 ,
  "Агата": 40,
  "Ярослав": 84,
}

user_input = input()

if 0 < students[user_input] <= 60:
  print(f"{students[user_input]} баллов, оценка C")
elif 60 < students[user_input] <= 80:
  print(f"{students[user_input]} баллов, оценка B")
elif 80 < students[user_input]:
  print(f"{students[user_input]} баллов, оценка A")

locations = {     'Каньон':'Котлован заброшенной стройки на пл. Яхтенной',
                  'Убежище':'Сквер рядом с историческим дотом на севере',
                  'Пентагон':'Пятиэтажки на улице Ленина',
                  'Безумный Макс':'Памятник Максиму Горькому перед ТЮЗом',
                  'Централь':'Линии подачи ТЭЦ',
                  'Улитки':'Улица Литке, д. 6',
                }

user_input = input()
print(locations[user_input])

keywords = ["Желание", "Семнадцать", "Ржавый", "Пропуск", "Печь" ]

word_count = {}

for i in keywords:
    word_count[i] = len(i)

print(word_count)
'''

year = input()
month = input()
day = input()

birth_date = {"year": year, "month": month, "day": day }

# Не удаляйте код ниже: он нужен для проверки.

print(" ".join([x for x in birth_date.keys()]))
print(" ".join([str(x) for x in birth_date.values()]))


