eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def incode_bukva(bukva, abc):
    find_bukva = abc.find(bukva)
    otr = len(abc) - find_bukva - 1
    if otr >= user_sdvig:
        return abc[find_bukva + user_sdvig]
    else:
        return abc[user_sdvig - otr - 1]



user_slovo = input()
user_sdvig = int(input())
#user_type = input()
#user_language = input()

#print(user_slovo)
'''
for k in user_slovo:
    find_bukva = eng_lower_alphabet.find(k)
    otr = len(eng_lower_alphabet) - find_bukva - 1
    if otr >= user_sdvig:
        print(eng_lower_alphabet[find_bukva + user_sdvig], end='')
    else:
        print(eng_lower_alphabet[user_sdvig - otr - 1], end='')
'''
incode_base = []
for world in user_slovo:
    if world in eng_lower_alphabet:
        incode_base.append(incode_bukva(world, eng_lower_alphabet))
    elif world in eng_upper_alphabet:
        incode_base.append(incode_bukva(world, eng_upper_alphabet))
    elif world in rus_lower_alphabet:
        incode_base.append(incode_bukva(world, rus_lower_alphabet))
    elif world in rus_upper_alphabet:
        incode_base.append(incode_bukva(world, rus_upper_alphabet))
    else:
        incode_base.append(world)
#BYFFI!
print(''.join(incode_base))
'''
for k in user_slovo:
    find_bukva = eng_lower_alphabet.find(k)
    otr = len(eng_lower_alphabet) - find_bukva - 1
    if otr >= user_sdvig:
        print(eng_lower_alphabet[find_bukva + user_sdvig], end='')
    else:
        print(eng_lower_alphabet[user_sdvig - otr - 1], end='')
'''



