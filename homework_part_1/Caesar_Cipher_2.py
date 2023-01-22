# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def incode_bukva(bukva, abc, sdvig):
    find_bukva = abc.find(bukva)
    otr = len(abc) - find_bukva - 1
    if otr >= sdvig:
        return abc[find_bukva + sdvig]
    else:
        return abc[sdvig - otr - 1]

def cleaning_word(word):
    clean_word = ''
    for i in word:
        if i not in ',.!?"':
            clean_word = clean_word + i
    return clean_word


user_slovo = input().split()
code_word = []
for i in user_slovo:
    clean_word = cleaning_word(i)
    sdvig = len(clean_word)
    for j in i:
        if j in eng_lower_alphabet:
            code_word.append(incode_bukva(j, eng_lower_alphabet, sdvig))
        elif j in eng_upper_alphabet:
            code_word.append(incode_bukva(j, eng_upper_alphabet, sdvig))
        else:
            code_word.append(j)
    code_word.append(' ')
print(''.join(code_word))


