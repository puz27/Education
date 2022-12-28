'''
def prostoe(n):
    flag = True
    counter = 0
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input())
poisk = n + 1
while prostoe(poisk) != True:
    poisk = poisk + 1
print(poisk)

def is_password_good(password):
    a1, a2, a3, a4 = False, False, False, False
    if len(password) >= 8:
        a1 = True
    if password.islower() != True:
        a2 = True
    if password.isupper() != True:
        a3 = True
    for i in password:
        if i in '1234567890':
            a4 = True
            break
    if password.isdigit() == True:
        a2 = False

    if a1 and a2 and a3 and a4 == True:
        return True
    else:
        return False

txt = input()
print(is_password_good(txt))

def is_one_away(word1, word2):
    k = 0
    if len(word1) == len(word2):
       for i in range(len(word1)):
           if word1[i] != word2[i]:
               k += 1
    if k == 1:
        return True
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))

def is_palindrome(text):
    for i in text:
        if i in (",.!?-."):
            text = text.replace(i, '')

    text2 = text[::-1]
    if text == text2:
        return True
    else:
        return False

s = input().lower().replace(' ', '')
print(is_palindrome(s))

def is_palindrome(text):
    for i in text:
        if i in (",.!?-."):
            text = text.replace(i, '')

    text2 = text[::-1]
    if text == text2:
        return True
    else:
        return False
def prostoe(n):
        flag = True
        counter = 0
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
def chet (n):
    if n % 2 == 0:
        return True
def is_valid_password(password):
    if len(slovo) > 3:
        return False
    k1 = is_palindrome(slovo[0])
    k2 = prostoe(int(slovo[1]))
    k3 = chet(int(slovo[2]))
    if k1 and k2 and k3 == True:
        return True
    else:
        return False

psw = input()
slovo = psw.split(':')
print(is_valid_password(slovo))


def is_correct_bracket(text):
    if text.count('(') == text.count(')'):
        return True
    else:
        return False
text = input()
print(is_correct_bracket(text))

def has_rrr(word):
   for i in word:
       if i in 'рР':
           return True
   return False

# Не удаляйте код ниже, он нужен для проверки

word = input()
result = has_rrr(word)
print(result)

grades = {2:"Плохо", 3:"Удовлетворительно", 4:"Хорошо", 5:"Отлично"}

def ... ()
    return ...

# Не удаляйте код ниже, он нужен для вызова функции и проверки

grade = int(input())
print(get_grade(grade))

grades = {2:"Плохо", 3:"Удовлетворительно", 4:"Хорошо", 5:"Отлично"}

def get_grade(grade):
    if grade == 2:
        return grades[grade]
    if grade == 3:
        return grades[grade]
    if grade == 4:
        return grades[grade]
    if grade == 5:
        return grades[grade]

# Не удаляйте код ниже, он нужен для вызова функции и проверки

grade = int(input())
print(get_grade(grade))

def get_grade(points):
    if 0 <= points <= 40:
        return "Плохо"
    elif 41 < points <= 60:
        return "Удовлетворительно"
    elif 61 < points <= 80:
        return "Хорошо"
    elif 81 < points <= 100:
        return "Отлично"

# Не удаляйте код ниже, он нужен для проверки

points = int(input())
grade = get_grade(points)
print(grade)

def get_period(hour):
    if 0 <= hour <= 6:
        return "ночь"
    elif 7 <= hour <= 11:
        return "утро"
    elif 12 <= hour <= 17:
        return "день"
    elif 18 <= hour <= 24:
        return "вечер"
# Не удаляйте код ниже, он нужен для проверки

hour = int(input())
time_of_day = get_period(hour)
print(time_of_day)

def avg(items):
    s = 0
    for i in items:
        s = (s + i)
    return s / len(items)

# Не удаляйте код ниже, он нужен для проверки

items = [int(x) for x in input().split(" ")]
items_avg = avg(items)
print(items_avg)

def get_rur_kop(value):
    return value // 100


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_rur_kop(value)
print(result)

def get_min_sec(sec):
    time = {}
    min = sec // 60
    secunds = sec % 60
    time['min'] = min
    time['sec'] = secunds
    return time


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_min_sec(value)
print(result)


def get_hashtags(text):

    words = text.split(" ")
    hashtags = []
    for word in words:
        if '#' in word:
            t = word.replace('#', '')
            hashtags.append(t)
    return hashtags


# Не удаляйте код ниже, он нужен для проверки

words = input()
result = get_hashtags(words)
print(result)

def get_square(radius):
   return  radius ** 2 * 3.14


# Не удаляйте код ниже, он нужен для проверки

radius = int(input())
square = get_square(radius)
print(square)

def get_longest(words):
    t = ''
    for i in words:
        if len(i) > len(t):
            t = i
    return t

# Не удаляйте код ниже, он нужен для проверки

word = input().split(" ")
result = get_longest(word)
print(result)

data = {5000: 1, 10000: 2, 20000: 3, 35000: 4, 50000: 5}

def get_discount(summ):
    if summ < 5000:
        return data[5000]
    elif summ < 10000:
        return data[10000]
    elif summ < 20000:
        return data[20000]
    elif summ < 35000:
        return data[35000]
    elif summ < 50000:
        return data[50000]
    else:
        return 6

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_discount(value)
print(result)

def get_percent_rounded(a ,b):
    x = round((a / b) * 100)
    x = str(x)
    return x + '%'

# Не удаляйте код ниже, он нужен для проверки

a = int(input())
b = int(input())
print(get_percent_rounded(a, b))

def hide():
  my_cats = ["Leo", "Simba", "Loki", "Milo"]
  my_cats.remove("Loki")
  my_cats.remove("Milo")
hide()
print(my_cats)

def get_middle_point(x1, y1, x2, y2):
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2
    return x3, y3

print(get_middle_point(0, 0, 10, 0))

import math


def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * (radius ** 2)
    return c, s

r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)

def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Нет корней')
    elif d == 0:
        x1 = (-b / (2*a))
        x2 = (-b / (2*a))
    elif d > 0:
      x1 = (-b - d ** 0.5) / (2*a)
      x2 = (-b + d ** 0.5) / (2*a)

    if x2 < x1:
      return x2, x1
    else:
      return x1, x2


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
'''
# объявление функции

# объявление функции
'''
def get_shipping_cost(quantity''):
    if n == 1:
        cost = 1000
    else:
        cost = 1000 + 120 * (n - 1)
    return cost

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


def get_month(language, number):
    if str(language) == 'ru':
        return lng_ru[number - 1]
    else:
        return lng_en[number - 1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))

# объявление функции
def is_magic(date):
    dat2 = []
    date = date.split('.')
    for i in date:
        x = int(i)
        dat2.append(x)
    year = dat2[2]
    if dat2[0] * dat2[1] == year % 100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

# объявление функции
def is_pangram(text):
    abcde = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for i in abcde:
        if i in text.lower():
            continue
        else:
            return False

    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

# объявление функции
def draw_triangle(n):
    for i in range(0, n):
        print(' ' * (n - 1 - i) + "*" * (1 + i * 2))

# основная программа
draw_triangle(8)

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def compute_binom(n, k):
    temp = n - k
    end = factorial(n) / (factorial(k) * factorial(temp))
    return round(end)
n = int(input())
k = int(input())
print(compute_binom(n, k))


zero_to_ninety_nine = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 
'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 
'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть',
 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре',
  'тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 
  'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь', 
  'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 
  'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 
  'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять', 'восемьдесят шесть', 
  'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 
  'девяносто семь', 'девяносто восемь', 'девяносто девять']

 def number_to_words(num):
    return zero_to_ninety_nine[num]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))

'''
# Исходный код
guides = [ {
  "pk": 1,
  "fields": {
    "user": 2,
    "surname": "Васечкин",
    "full_name": "Андрей Васечкин",
    "tours_count": 5,
    "bio": "Я обожаю Москву, и изучаю город с необычных ракурсов. С радостью поделюсь с вами своими лучшими открытиями. Мы поднимемся на сталинские высотки и посмотрим на исторический центр сверху. Я покажу вам то, что скрыто от глаз большинства туристов и даже жителей города. Маршруты подобраны индивидуально под ваш запрос. Для влюбленных доступна услуга свидания на крыше.",
    "is_pro": True,
    "company": 1
  }
},
{
  "pk": 2,
  "fields": {
    "user": 1,
    "surname": "Новикова",
    "full_name": "Людмила Новикова",
    "tours_count": 2,
    "bio": "Я петербурженка в 7-м поколении. Люблю делиться историями и секретами дореволюционных петербургских зданий и особняков. Поделюсь историями моей бабушки. Вместе со мной работает небольшая дружная команда влюбленных в Петербург местных гидов. Мы раскроем вам секреты старинных домов и покажем то, что скрыто от глаз большинства туристов и жителей города.",
    "is_pro": True,
    "company": 2
  }
},
{
  "pk": 3,
  "fields": {
    "user": 3,
    "surname": "Беридзе",
    "full_name": "Георги Беридзе",
    "tours_count": 5,
    "bio": "Филолог-журналист по образованию. За плечами более 9 лет экскурсий по Грузии и барменский опыт. Писатель. Перфекционист. И просто увлеченный человек. Родился и вырос в Тбилиси. Более 10 поколений тут. Люблю этот райский уголок на планете и свою работу. Мама-кулинар привила любовь к вкусной еде.",
    "is_pro": True,
    "company": None
  }
},
{
  "pk": 4,
  "fields": {
    "user": 4,
    "surname": "Ласкина",
    "full_name": "Оксана Ласкина",
    "tours_count": 2,
    "bio": "Я всегда увлекалась историей и, как следствие, получила образование гида-экскурсовода. С удовольствием знакомлю гостей города с историей, татарской культурой и традициями. Вы влюбитесь в наш край.",
    "is_pro": True,
    "company": 5
  }
},
{
  "pk": 5,
  "fields": {
    "user": 5,
    "surname": "Горячий",
    "full_name": "Иван Горячий",
    "tours_count": 7,
    "bio": "Работал учителем истории более 10 лет, последние 5 лет живу в Сочи и уже третий год провожу экскурсии, организовываю туры. На моих прогулках и турах вы узнаете не только об экскурсионных объектах, но и о том, чем живет современный Сочи: о ценах, недвижимости, об интересных местах города и его необычных заведениях. Есть туры разного уровня сложности и комфорта, где можно с детьми и без. Бесплатным бонусом ко всем экскурсиям станет фотосессия на зеркальный фотоаппарат.",
    "is_pro": True,
    "company": 4
  }
},
{
  "pk": 6,
  "fields": {
    "user": 6,
    "surname": "Ивлева",
    "full_name": "Яна Ивлева",
    "tours_count": 5,
    "bio": "Я живу в Стамбуле много лет. По образованию филолог и историк. О Стамбуле читаю, пишу, живу этим городом и люблю его. Раскрою его вам таким, какой он есть: великолепный, приветливый, неизменно интересный и всегда загадочный. Ваше путешествие по этому сказочному городу навсегда останется в памяти и сердце. ",
    "is_pro": True,
    "company": 1
  }
},
]
'''
for i in guides:
    if i["fields"]["tours_count"] >= 5:
        name = i["fields"]['full_name']
        count = i["fields"]["tours_count"]
        print(f"{name} | туров: {count}")

s = int(input())
#inpt = int(input())
for i in guides:
   if i['pk'] == s:
       in_data = i['fields']
       print(f"{in_data['full_name']}, туров: {in_data['tours_count']}")
       print(f"{in_data['bio']}")
'''

s = [{'pk': 1, 'full_name': 'Jane Snake', 'skills': ['Python', 'Linux', 'MacOS', 'Docker', 'Flask']}, {'pk': 2, 'full_name': 'Sheri Torres', 'skills': ['Java', 'Swify', 'Fortran', 'Basic']}, {'pk': 3, 'full_name': 'Burt Stein', 'skills': ['Planning', 'Negotiation', 'Management', 'Windows']}, {'pk': 4, 'full_name': 'Bauer Adkins', 'skills': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js']}]
dic = []
for i in s:
  dic.append(i['pk'])
print(dic)