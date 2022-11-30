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

words = ('privet', 'poka', 'folout', 'anton')
# Верно
# get random word
def get_word(words):
    """
    Получает случайное слово
    из списка слов
    """
    word = random.choice(words)
    return word
# get morse cod from word
def morse_encode(word):
    words_in_morse = []
    [words_in_morse.append(i) for i in word]
    return words_in_morse

# start
rundom_slovo = get_word(words)
print(rundom_slovo)
print(morse_encode(rundom_slovo))

#while True:
   # print("Сегодня мы потренируемся расшифровывать морзянку.", "Нажмите Enter и начнем", sep="\n")
   # input()
   # break
