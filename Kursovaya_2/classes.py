from typing import NoReturn

class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_subwords(self) -> bool:
        pass

    def check_count_subwords(self) -> int:
        pass

    # def __repr__(self):
    #     return self.word

class Player:

    def __init__(self, name, used_words = ''):
        self.name = name
        self.used_words = used_words

    def get_used_words(self) -> int:
        pass

    def add_word_to_used(self) -> NoReturn:
        pass

    def check_already_used(self) -> bool:
        pass