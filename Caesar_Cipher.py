eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def find_bukva(bukva, abc):
    '''Insert bukba + spisok where finf it'''
    find_bukva = abc.find(bukva)
    return (abc[find_bukva + user_sdvig])



user_slovo = input()
#user_type = input()
#user_language = input()

#print(user_slovo)

'''
for i in user_slovo:
    print(i)
    for j in i:
        print(j)
        print(find_bukva(j, rus_lower_alphabet))
'''
user_sdvig = int(input())
#k = input()
for k in user_slovo:
    find_bukva = eng_lower_alphabet.find(k)
    otr = len(eng_lower_alphabet) - find_bukva - 1
    if otr >= user_sdvig:
        print(eng_lower_alphabet[find_bukva + user_sdvig])
    else:
        print(eng_lower_alphabet[user_sdvig - otr - 1])




