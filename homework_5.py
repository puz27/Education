text = "The quick brown fox jumps over the lazy dog"


def text_length():
    text2 = text.replace(' ', '')
    return len(text2)

def text_length_full():
    return len(text)

def text_word_count():
    return (text.count(' ') + 1)

# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length())
print(text_length_full())
print(text_word_count())