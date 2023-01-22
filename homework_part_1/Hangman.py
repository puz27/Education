# Описание проекта: программа загадывает слово, а пользователь должен его угадать.
import random


def get_rundom_word(word):
    x = random.choice(word)
    return list(x)


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


words = ['yamaha', 'honda', 'suzuki', 'kawasaki', 'harley-davidson', 'triumph']
slovo = get_rundom_word(words)
tries = 6
flag = False
end_flag = False
working = []

for i in slovo:
    working.append('_')

print("Давайте играть в угадайку слов!")
while True:
    print(''.join(working))
    user_bukva = input('Введите букву\n')
    for i in range(len(slovo)):
        if slovo[i] == user_bukva:
            flag = True

    if flag is True:
        for i in range(len(slovo)):
            if slovo[i] == user_bukva:
                working.insert(i, slovo[i])
                working.pop(i + 1)
                # print(working)
                flag = False
                if slovo == working:
                    end_flag = True
                    break

    else:
        print("Такой буквы нет!\n")
        print(display_hangman(tries))
        tries = tries - 1
        if tries == 0:
            print("Проиграли!")
            print(display_hangman(0))
            break

    if end_flag is True:
        print("Все угадали!")
        end = ''.join(working)
        print(f'Слово {end}')
        break
