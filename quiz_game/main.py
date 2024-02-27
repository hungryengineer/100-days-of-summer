# from quiz_game import Question
# from quiz_game_data import question_data
# from quiz_brain import QuizBrain
#
# #question = Question(question, answer)
#
# question_bank = []
# for question in question_data:
#     question_text = (question['text'])
#     answer_text = (question['answer'])
#
#     new_question = Question(question_text, answer_text)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
# while quiz.still_has_questions() is True:
#   quiz.next_question()
#
# print("Quiz completed")
# print(f"You got {quiz.score}/{quiz.question_number}")
#














from quiz_game_data import question_data
from quiz_game import Question
from quiz_brain import *

question_list = [] #initiated an empty list to store questions from question_data so that Question class method can fetch it one by one
for questions in question_data:
    q_text = questions['text']
    q_answer = questions['answer']
    quiz_questions = Question(q_text,q_answer) #created an object from Question class to store questions
    question_list.append(quiz_questions) #appended the questions from our quiz_game_data to the list
#print(question_list[1].q_text)

quiz = QuizBrain(question_list)
while quiz.still_has_question(): #and quiz.check_answer(q_text, q_answer):
    quiz.next_question()


