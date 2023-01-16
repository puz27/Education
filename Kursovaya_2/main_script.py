from utils import *
import requests

# load_word = load_random_word('https://www.jsonkeeper.com/b/UUW0')
load_word = json_load_data('questions.json')
print(load_word.word)
print(load_word.subwords)

user = Player(input('Ввведите имя игрока\n'))
print('Привет {}!'.format(user.name))
print('Составьте 8 слов из слова {}'.format(load_word.word.upper()))
print('Слова должны быть не короче 3 букв')
print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
print('Поехали, ваше первое слово?')

print(load_word.check_count_subwords())
while user.get_count_used_words() != load_word.check_count_subwords():
    user_word = input()

    if user_word.lower() in ('stop', 'стоп'):
        print('Прекращаем игру')
        break

    elif len(user_word) < 3:
        print('Слишком короткое слово')

    elif user_word not in load_word.subwords:
        print('Не верно. Слова нет в списке допустимых')

    elif user.check_already_used(user_word) is True:
        print('Это слово уже использовано')

    elif load_word.check_subwords(user_word):
        user.add_word_to_used(user_word)
        load_word.check_count_subwords()
        print('Верно. Слово {} подходит'.format(user_word.upper()))


print(get_statistic(user))