"""Программа создаёт файлы для лабораторной работы."""
import os.path, json


def get_data():
    with open('data.json', 'r') as user_data:
        data = json.load(user_data)
    if data:
        if input(f"Введите 'YES' если вы хотите использовать фамилию: {data['user_name']}"
                 f" и создать файлы для {data['last_lesson'] + 1}-го занятия: ") == 'YES':
            with open('lessons.json', 'r') as lessons_data:
                lessons = json.load(lessons_data)
                first_task, last_task = map(int, lessons[f"{data['last_lesson'] + 1}"].split())
            with open('data.json', 'w') as user_data:
                json.dump(data, user_data)
            return data['user_name'], data['last_lesson'] + 1, (first_task, last_task)
    surname = input('Введите свою фамилию: ')
    lesson = int(input('Ведите номер урока: '))
    first_task, last_task = map(int, input('Введите 1-ое и последнее задание ').split())
    data['user_name'] = surname
    data['last_lesson'] = lesson
    with open('data.json', 'w') as user_data:
        json.dump(data, user_data)
    return surname, lesson, (first_task, last_task)


def create_files():
    """Принцип работы таков что в 1-ой строке вы вписываете свою фамилию
       во 2-ой номер занятия на которое вы создаёте лабораторные файлы
       в 3-ей вы вписываете 2 номера: 1-ый - первое задание
       и 2-ой - последнее задание из списка заданий лабораторной"""
    surname, lesson, (first_task, last_task) = get_data()
    for task in range(first_task, last_task + 1):
        f = open(f'{surname}_{lesson}_{task}.py', 'w+')


if __name__ == '__main__':
    create_files()
