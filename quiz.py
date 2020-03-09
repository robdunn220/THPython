import datetime
import random
from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        self.start_time = datetime
        self.end_time = datetime
        question_types = (Add, Multiply)
        for i in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self):
        self.start_time = datetime.datetime.now()
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()

        self.summary()

    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def ask(self, question):
        correct = False
        question_start = datetime.datetime.now()

        answer = input(question.text + ' = ')

        if answer == str(question.answer):
            correct = True

        question_end = datetime.datetime.now()

        return correct, question_end - question_start

    def summary(self):
        print('You answered {} out of {} correctly.'.format(
            self.total_correct(), len(self.questions)
        ))
        print('It took you {} seconds total.'.format(
            self.end_time-self.start_time)
        )


q1 = Quiz()
q1.take_quiz()