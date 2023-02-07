import requests
import random
import json
from Fail import get_all
from Fail import get_password
from Fail import get_score
with open('users.json', 'r', encoding='utf-8') as users_data:
    fail=json.load(users_data)
attempts = 2
used_answers = []
number_question = 0
score = 0
random_answer = []
print(fail)
names_of_players = get_all()  # имена прошлых игроков
passwords_of_players = get_password()  # пароли прошлых игроков
best_score_of_players = get_score()  # лучшие результаты прошлых игроков
user_choice = input("Выберите вход(если вы уже играли в викторину) или регистрация(если вы тут впервые)>>>")
name = input("Напишите ваше имя>>>")
if user_choice == "вход":
    if name in names_of_players:
        password = input("Введите пароль>>>")
        print(passwords_of_players)
        if int(password) in passwords_of_players:
            print("Ты попал на викторину.")
            print(
                "Твоя задача-побить рекорд прошлых игроков или хотя бы досчить того же уровня,как и они,иначе ты проиграешь.")
        else:
            while int(password) not in passwords_of_players:
                password = input("Неправильный пароль.Попробуйте еще раз")
    else:
        while name not in names_of_players:
            name = input("Неправильный логин.Попробуйте еще раз.")
        password = input("Введите пароль>>>")
        print(passwords_of_players)
        if int(password) in passwords_of_players:
            print("Ты попал на викторину.")
            print(
                "Твоя задача-побить рекорд прошлых игроков или хотя бы досчить того же уровня,как и они,иначе ты проиграешь.")
        else:
            while int(password) not in passwords_of_players:
                password = input("Неправильный пароль.Попробуйте еще раз")
if user_choice == "регистрация":
    if name in names_of_players:
        while name in names_of_players:
            name = input("Такое имя уже используется,выберите другое.")
        password = input("Придумайте пароль>>>")
        while int(password) in passwords_of_players:
            password = input("Такой пароль уже используется.Выберите другой.")
        password1 = input("Повторите пароль>>>")
        while password1 != password:
            password1 = input("Неправильно.Попробуйте еще раз.")
        print("Ты попал на викторину.")
        print(
            "Твоя задача-побить рекорд прошлых игроков или хотя бы досчить того же уровня,как и они,иначе ты проиграешь.")
    else:
        password = input("Придумайте пароль>>>")
        while int(password) in passwords_of_players:
            password = input("Такой пароль уже используется.Выберите другой.")
        password1 = input("Повторите пароль>>>")
        while password1 != password:
            password1 = input("Неправильно.Попробуйте еще раз.")
        print("Ты попал на викторину.")
        print(
            "Твоя задача-побить рекорд прошлых игроков или хотя бы досчить того же уровня,как и они,иначе ты проиграешь.")


def get_questions(level_question: int):
    questions_list = []
    response = requests.get(f"https://engine.lifeis.porn/api/millionaire.php?qType={level_question}&count=5").json()
    for question_data in response["data"]:
        correct_answer = question_data['answers'][0]
        question_answers = question_data['answers']
        random.shuffle(question_answers)
        questions_list.append(
            {
                'answers': question_answers,
                'question': question_data['question'].replace('\u2063', ''),
                'correct_answer': correct_answer,
                'score': level_question * 10
            }
        )
    return questions_list


def show_question(question_data):
    print(question_data['question'])
    print("---Варианты ответа---")
    print("\n".join(question_data['answers']) + "\n")


def user_answer_check(user_answ, question_data, score_user):
    if user_answ == question_data['correct_answer']:
        score_user += question_data['score']
        text = "Верно!"
        return score_user, text
    else:
        text = f"Неверно\n Правильный ответ {question_data['correct_answer']}"
        return score_user, text


for count_round in range(1, 4):
    questions = get_questions(level_question=count_round)
    for question in questions:
        show_question(question_data=question)
        user_answer = input("Введите ответ>>>")
        score, text_output = user_answer_check(user_answ=user_answer, question_data=question, score_user=score)
        print(text_output)

print("Ваш счет:", score)
random_answer = []
fail.append({"name": name, "best_result": score, "password": int(password)})
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(fail, file, indent=4)
