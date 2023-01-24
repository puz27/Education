# работа через декоратор property напрямую
class Player:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def get_name(self):
        print("GET NAME!")
        return self.name

    def set_name(self, name: str):
        print("SET NAME!")
        self.name = name

    vizov = property(get_name, set_name)

man = Player('anton')
man.vizov = 10
print(man.vizov)


# работа через декоратор property
class Player2:
    def __init__(self, name):
        self.name = name
        self.age = 0

    @property
    def man_name(self):
        print("GET NAME!")
        return self.name

    @man_name.setter
    def man_name(self, name: str):
        print("SET NAME!")
        self.name = name

boy = Player2('ANTON')
print(boy.man_name)
boy.man_name = 'NICK'
print(boy.name)


# общее
class Player3:
    def __init__(self, name):
        self.__name = name

    @property
    def instance_name(self):
        print("возврат имени")
        return self.__name
    @instance_name.setter
    def instance_name(self, input):
        self.__name = input

girl = Player3('Elena')
print(girl.instance_name)
girl.instance_name = 'Sveta'
print(girl.instance_name)
