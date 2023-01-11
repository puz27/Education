class Question:
    """
    Класс на базе которого создаем экземпляры для обработки вопросов/ответов пользователя
    Атрибуты: вопрос, сложность вопроса, правильный ответ, флаг задан ли вопрос, флаг есть ли ответ, баллы за вопрос
    """
    def __init__(self, user_question, question_difficult, right_answer):

        self.user_question = user_question
        self.question_difficult = question_difficult
        self.right_answer = right_answer
        self.is_question_asked = False
        self.user_answer = None
        self.user_counts = 0


    def get_points(self):
        """
        Возвращает int, количество баллов. Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.question_difficult) * 10


    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом, иначе False.
        """
        return True if self.user_answer == self.right_answer else False


    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag? Сложность 4/5
        """
        return "{}\n{}".format(self.user_question, self.question_difficult)


    def build_feedback(self):
        """
        Возвращает: Ответ верный, получено __ баллов
        Если ответ верный помечает атрибут user_answer экземпляра как True, в противном случае False
        Помечает атрибут is_question_asked (был задан ли вопрос) экземпляра как True
        """
        if self.is_correct() is True:
            self.user_counts = self.get_points()
            self.is_question_asked = True
            self.user_answer = True
            return "Ответ верный, получено {} баллов\n".format(self.get_points())
        else:
            self.is_question_asked = True
            self.user_answer = False
            return "Ответ неверный, верный ответ {}\n".format(self.right_answer)