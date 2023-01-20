from utils import *

def main() -> None:
    '''
    load data, check user answers, print statistic
    '''
    # load data and create instance of BasicWord class
    load_word = load_random_word('https://www.jsonkeeper.com/b/UUW0', 'questions.json')

    # create instance of Player class
    user = Player(input('Ввведите имя игрока\n'))

    # greetings user
    print_greetings(user, load_word)

    # check user answers
    while user.get_count_used_words() != load_word.check_count_subwords():
        user_word = input().lower()

        if user_word in ('stop', 'стоп'):
            print('\nПрекращаем игру')
            break

        elif len(user_word) < 3:
            print('{} - cлишком короткое слово'.format(user_word.upper()))

        elif user_word not in load_word.subwords:
            print('Неверно. Слова {} нет в списке допустимых'.format(user_word.upper()))

        elif user.check_already_used(user_word) is True:
            print('Слово {} уже использовано'.format(user_word.upper()))

        elif load_word.check_subwords(user_word):
            user.add_word_to_used(user_word)
            load_word.check_count_subwords()
            print('Верно. Слово {} подходит. '
                  'Количество найденных слов на данный момент: {}'.format(user_word.upper(), user.get_count_used_words()))

    # print user statistic
    print_statistic(user)

if __name__ == "__main__":
    main()