class Question:
    def __init__(self, text):
        self.text = text
        self.difficult = 1
        self.right_answer = None
        self.user_question = False
        self.user_answer = None
        self.user_counts = 0


    def get_points(counts):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """


    def is_correct():
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        pass


    def build_question():
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        pass


    def build_positive_feedback():
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        pass


    def build_negative_feedback():
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        pass



