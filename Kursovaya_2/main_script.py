from utils import *

load_word = load_random_word('https://www.jsonkeeper.com/b/UUW0')
#print(load_word.word)
#print(load_word.subwords)

user = Player(input('Ввведите имя игрока\n'))
print('Привет {} !'.format(user.name))
print('Составьте 8 слов из слова {}'.format(load_word.word))
print('Слова должны быть не короче 3 букв')
print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
print('Поехали, ваше первое слово?')
