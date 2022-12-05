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

# get random word
def get_word(word):
    """
    Get random word from word list
    """
    word = random.choice(word)
    return word
# get morse code from word
def morse_encode(word):
    """
    Convert word to morse code
    """
    words_in_morse = []
    [words_in_morse.append(shift_morse[i]) for i in word]
    return '  '.join(words_in_morse)
def print_statistics(answers):
    """
    Show final information
    """
    return len(answers), len([i for i in answers if i == True]), len([i for i in answers if i == False])

# list of user answers True and False
answers = []

# greeting
while True:
   print("Сегодня мы потренируемся расшифровывать морзянку.", "Нажмите Enter и начнем.", sep="\n")
   input()
   break

# check user answers and add results in final_user_answer
for num_question in range(1, 6):
  random_slovo = get_word(words)
  print(random_slovo )
  print(f'Слово {num_question}  {morse_encode(random_slovo)}')
  if input().lower() == random_slovo:
    print(f'Верно, это слово {random_slovo} !')
    answers.append(True)
  else:
    print(f'Неверно, это слово {random_slovo} !')
    answers.append(False)

# final statistic
print()
statistic = print_statistics(answers)
print(f'Всего задачек: {statistic[0]}')
print(f'Отвечено верно: {statistic[1]}')
print(f'Отвечено неверно: {statistic[2]}')






