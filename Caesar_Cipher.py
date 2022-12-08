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

def decode_bukva(bukva, abc):
    find_bukva = abc.find(bukva)
    if find_bukva >= user_sdvig:
        return abc[find_bukva - user_sdvig]
    else:
        return abc[len(abc) - user_sdvig + find_bukva]


user_slovo = input("Введите слово\n")
user_sdvig = int(input("Введите сдвиг\n"))
user_choise = input("Кодируем - введите - KOD, декодируем - DECOD\n")

if user_choise == 'KOD':
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
    print(''.join(incode_base))

if user_choise == 'DECOD':
    decode_base = []
    for world in user_slovo:
        if world in eng_lower_alphabet:
            decode_base.append(decode_bukva(world, eng_lower_alphabet))
        elif world in eng_upper_alphabet:
            decode_base.append(decode_bukva(world, eng_upper_alphabet))
        elif world in rus_lower_alphabet:
            decode_base.append(decode_bukva(world, rus_lower_alphabet))
        elif world in rus_upper_alphabet:
            decode_base.append(decode_bukva(world, rus_upper_alphabet))
        else:
            decode_base.append(world)
    print(''.join(decode_base))


