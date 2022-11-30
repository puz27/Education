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
# dictionary of words
words = ('privet', 'poka', 'folout', 'anton')
# get random word
def get_word(word):
    """
    Получает случайное слово
    из списка слов
    """
    word = random.choice(word)
    return word
# get morse code from word
def morse_encode(word):
    words_in_morse = []
    [words_in_morse.append(shift_morse[i]) for i in word]
    return '  '.join(words_in_morse)

def print_statistics(answers):
  #return len(answers)
  return [i for i in answers if i == True]


answers = []

# start
#rundom_slovo = get_word(words)
#print(rundom_slovo)
#print(morse_encode(rundom_slovo))

#while True:
   # print("Сегодня мы потренируемся расшифровывать морзянку.", "Нажмите Enter и начнем", sep="\n")
   # input()
   # break

for num_question in range(1, 6):
  rundom_slovo = get_word(words)
  print(f'Слово {num_question}  {morse_encode(rundom_slovo)}')
  if input() == rundom_slovo:
    print(f'Верно, это слово {rundom_slovo}!')
    answers.append(True)
  else:
    print(f'Неверно, это слово {rundom_slovo}!')
    answers.append(False)
z = answers
print(print_statistics(z))



