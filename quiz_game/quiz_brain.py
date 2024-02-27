# class QuizBrain:
#     def __init__(self, question_list):
#         self.question_number = 0
#         self.score = 0
#         self.question_list = question_list
#
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number+=1
#         input(f"Q.1{self.question_number}:{current_question.q_text}\n(True/False)")
#
#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)
#         # if self.question_number < len(self.question_list):
#         #     return True
#         # else:
#         #     False
#
#     def check_answer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             self.score+=1
#             print("You got it right")
#         else:
#             print("That's wrong")
#         print(f"The correct answer is:{correct_answer}\nyour current score is {self.score}/{self.question_number}")

















class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}:{current_question.q_text}\ntrue/false\n")
        self.check_answer(user_answer, current_question.q_answer)
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("correct")
        else:
            print("wrong")

