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


# Begin Portion 1#
import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        self.connections[connection_id] = connection_load
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0

        # Add up the load for each of the connections
        for i in self.connections.values():
            total += i

        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

server = Server()
server.add_connection("192.168.1.1")
print(server.load())

#Begin Portion 2#
# Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        total_server = 0
        for server in self.servers:
            total_load += server.load()
            total_server += 1
        return total_load / total_server

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


# End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())


class Character():
    def move(self, direction, distance):
        directions_list = {"north": "на север", "south": "на юг", "west": "на запад", "east": "на восток"}
        if direction not in directions_list.keys():
            print(self.name, "движется непонятно куда")
        else:
            print(self.name, "движется", distance, "метров", directions_list[direction])


class Hero(Character):
    def __init__(self, name):
        self.name = name
class Enemy(Character):
    def __init__(self, name):
        self.name = name

pythomir = Hero("Питомир")
bugoonya = Enemy("Багуня")

pythomir.move("north", 50)
pythomir.move("west", 10)
pythomir.move("climb", 0)

bugoonya.move("north", 50)
bugoonya.move("west", 10)
pythomir.move("climb", 0)

# Не удаляйте код ниже, это проверка!

if not 'Character' in dir():
    print("Общий класс родитель Character не создан")

if not hasattr(Character, "move"):
    print("У общего класса отсутствует метод move")


class Enemy():

  def __init__(self, name, health):

    self.is_alive = True;
    self.name = name
    self.health = health


class Dragon(Enemy):
    def bite(self):
        print("я кусаюсь")

    def burn(self):
        print("я дышу огнем")

dragon = Dragon("Инхеритий Проворный", 300)

# Не удаляйте код ниже, это проверка!

dragon.bite()
dragon.burn()

class Hero():

  def __init__(self, name, posessions):
    self.name = name
    self.posessions = posessions
  def __repr__(self):
      return "Герой {} взял с собой {}".format(self.name, ', '.join(self.posessions))

# Не удаляйте кед ниже, он нужен для проверки

hero = Hero("Питомир", ["меч", "плащ", "шляпа"])
print(hero)
'''

class Box():
    def __init__(self, size, weight, contains):
        self.size = size
        self.weight = weight
        self.contains = contains

    def observe(self):
        return "Это похоже на ящик размером {} и весом {}кг".format(self.size, self.weight)

class Container(Box):
    def open(self):
        return "В ящике размером {} и весом {}кг оказалось {}".format(self.size, self.weight, self.contains)

box_1 = Box("30x30", 1, "15 золотых монет")
container_1 = Container("50x30", 2, "7 золотых монет")

# Код проверки, не удаляйте его

try: Box
except:print("Класс Box не задан")
try: Container
except:print("Класс Container не задан")
try: Container.open
except:print("Метод open у Container не задан или с ошибкой")
try: Container.observe
except:print("Метод observe у Container не наследуется или с ошибкой")
try: box_1
except:print("Экземпляр box_1 не существует")
try: container_1
except:print("Экземпляр container_1 не существует")

print(container_1.observe())
print(container_1.open())


