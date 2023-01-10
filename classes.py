'''
class Bottle:

  def __init__(self, color, volume):
    self.color = color
    self.volume = volume

bottle_1 = Bottle("Красная", 0.7)
bottle_2 = Bottle("Белая", 0.3)
bottle_3 = Bottle("Черная", 1.0)

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.volume)
print(bottle_2.color, bottle_2.volume)
print(bottle_3.color, bottle_3.volume)


class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

alisa = Student("Алиса", 3)
alisa2 = Student("Маргарита", 2)

print(alisa.name)

class Album:

    def __init__(self, artist, title, tracks):
        self.artist = artist
        self.title = title
        self.tracks = tracks

album_1 = Album('Queen', 'Killer Queen', ['Brighton rock', 'Killer Queen', 'Tenement Funster'])
album_2 = Album('Metallica', 'Black Album', ['Enter Sandman', 'Sad But True', 'Holier Than Thou'])


class Bottle:

    def __init__(self, color):
        self.color = color
        self.contains = 0.0

    def get_content(self):
        return self.contains

    def fill(self, volume):
        self.contains = float(volume)

bottle_1 = Bottle("Красная")
bottle_2 = Bottle("Синяя")


# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())

class TodoList:
  def __init__(self, tasks):
    self.tasks = tasks

  def add_task(self, zad):
    self.tasks.append(zad)


todo_list = TodoList([])
todo_list.add_task('Выключить свет')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Включить свет')

# Не удаляйте этот код, он нужен для проверки

print(" ".join(todo_list.tasks))

class TodoList:
    tasks = []

    def add_task(self, zad):
        self.tasks.append(zad)


todo_list = TodoList()
todo_list.add_task('Выключить свет')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Включить свет')

# Не удаляйте этот код, он нужен для проверки

print(" ".join(todo_list.tasks))



class Player:
    def __init__(self, name):
        self.name = str(name)
        self.score = 0

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score


player_1 = Player("Алиса")


# Не удаляйте этот код, он нужен для проверки

print(player_1.name, player_1.get_score())
player_1.set_score(200)
print(player_1.name, player_1.get_score())
player_1.set_score(500)
print(player_1.name, player_1.get_score())


class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, number):
        self.value = self.value + number

    def subtract(self, number):
        self.value = self.value - number


x = Number(7)
x.add(3)
x.subtract(10)
x.get()

# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.radius * 2

    def get_perimeter(self):
        return 2 * self.radius * 3.14

# Не удаляйте этот код, он нужен для проверки

circle_1 = Circle(7)
print("радиус", circle_1.get_radius() )
print("диаметр", circle_1.get_diameter() )
print("периметр", round(circle_1.get_perimeter(),1))

class Square:

    def __init__(self, side_length, color = 'white'):
        self.side_length = side_length
        self.color = color

    def set_side(self, length):
        self.side_length = length

    def set_color(self, color):
        self.color = color

    def get_side(self):
        return int(self.side_length)

    def get_color(self):
        return self.color

    def get_perimeter(self):
        return self.side_length * 4
# Не удаляйте этот код, он нужен для проверки

square_1 = Square(2)
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1.set_side(3)
square_1.set_color("red")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1 = Square(1, "black")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())


class Room:

    def __init__(self, number, is_free):
        self.number = number
        self.is_free = is_free


def get_free_rooms(rooms):
    free_rooms = []
    for i in rooms:
        if i.is_free == True:
            free_rooms.append(i)
    return free_rooms


rooms = [Room(14, True), Room(15, False), Room(16, True)]
rooms_free = get_free_rooms(rooms)

# Не удаляйте этот код, он нужен для проверки

[print(r.number) for r in rooms_free]
'''


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)