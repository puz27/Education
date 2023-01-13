import random

# dictionary morse code
shift_morse ={
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}
# tuple of answers
words = ('yamaha', 'honda', 'suzuki', 'kawasaki', 'harley-davidson', 'triumph')
# tuple of words for final statistic
words_statistic = ('Всего задачек:', 'Отвечено верно:', 'Отвечено неверно:')
# list of user answers True and False
answers = []

def get_word(word):
    """Get random word from word list"""
    word = random.choice(word)
    return word


def morse_encode(word):
    """Get morse code from word"""
    words_in_morse = [shift_morse[i] for i in word if i in shift_morse.keys()]
    return '  '.join(words_in_morse)


def print_statistics(answers):
    """Show final information"""
    return len(answers), len([i for i in answers if i is True]), len([i for i in answers if i is False])

# greeting
while True:
  print("Сегодня мы потренируемся расшифровывать морзянку.", "Нажмите Enter и начнем.", sep="\n")
  if input() == "":
    break
  else:
    print("Нажмите Enter")

# check user answers and add results in final_user_answer
for num_question in range(1, 6):
  rundom_slovo = get_word(words)
  print(f'Слово {num_question}  {morse_encode(rundom_slovo)}')
  if input().lower() == rundom_slovo:
    print(f'Верно, это слово {rundom_slovo} !')
    answers.append(True)
  else:
    print(f'Неверно, это слово {rundom_slovo} !')
    answers.append(False)

# final statistic
statistic = print_statistics(answers)
print(f'\nВсего задачек: {statistic[0]}')
print(f'Отвечено верно: {statistic[1]}')
print(f'Отвечено неверно: {statistic[2]}')






