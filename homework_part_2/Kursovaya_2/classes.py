class BasicWord:
    '''
    class on the basis of which create instance for work with word and subwords
    '''
    def __init__(self, word: str, subwords: list) -> None:
        self.word = word
        self.subwords = subwords


    def check_subwords(self, word: str) -> bool:
        '''
        check user entered word in possible answers
        '''
        return True if word in self.subwords else False


    def check_count_subwords(self) -> int:
        '''
        return count of possible right answers
        '''
        return len(self.subwords)


    def __repr__(self) -> str:
        '''
        not used in execution. used only for debugging
        '''
        return '{} {}'.format(self.word, self.subwords)


class Player:
    '''
   class on the basis of which create instance for work with user answers and his statistic
    '''
    def __init__(self, name: str) -> None:
        self.name = name
        self.used_words = []


    def get_count_used_words(self) -> int:
        '''
        return count of words that user has already found
        '''
        return len(self.used_words)


    def add_word_to_used(self, add_word: str) -> None:
        '''
        add user answer to list used_words
        '''
        self.used_words.append(add_word)


    def check_already_used(self, word: str) -> bool:
        '''
        check user answer. Find his answer in list of used words
        '''
        return True if word in self.used_words else False


    def __repr__(self) -> str:
        '''
        return statistic of user round
        '''
        return '\nПользователь: {}\nУгаданные слова: {}'.format(self.name, ', '.join(self.used_words))
