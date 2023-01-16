from typing import NoReturn

class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_subwords(self, word) -> bool:
        return True if word in self.subwords else False

    def check_count_subwords(self) -> int:
       return len(self.subwords)

    def __repr__(self):
        pass


class Player:

    def __init__(self, name: str):
        self.name = name
        self.used_words = []


    def get_count_used_words(self) -> int:
        return len(self.used_words)

    def add_word_to_used(self, add_word) -> NoReturn:
        self.used_words.append(add_word)

    def check_already_used(self, word) -> bool:
        return True if word in self.used_words else False

    def __repr__(self):
        return 'Отгаданные слова: {}'.format(' '.join(self.used_words))
