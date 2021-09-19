"""Программа создаёт файлы для лабораторной работы"""
import os.path, json
from tkinter import Tk, filedialog


def ask_directory():
    """предлагает пользователю выбрать папку"""
    if input("если вы хотите выбрать папку для создания файлов введите 'YES',"
             " если хотите создать файлы в папке программы нажмите 'ENTER': ").upper() == 'YES':
        root = Tk() # pointing root to Tk() to use it as Tk() in program.
        root.withdraw() # Hides small tkinter window.
        root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
        file_directory = filedialog.askdirectory() # Returns opened path as str
        return file_directory
    return ''


def json_data(data, used_directory=True):
    """подтягивает данные из data.json"""
    with open('lessons.json', 'r') as lessons_data:
        lessons = json.load(lessons_data)
        first_task, last_task = map(int, lessons[f"{data['last_lesson'] + 1}"].split())
    if used_directory:
        with open('data.json', 'w+') as user_data:
            data['last_lesson'] += 1
            json.dump(data, user_data)
        return data['user_name'], data['last_lesson'], (first_task, last_task), data['directory']
    else:
        data['directory'] = ask_directory()
        with open('data.json', 'w+') as user_data:
            data['last_lesson'] += 1
            json.dump(data, user_data)
        return data['user_name'], data['last_lesson'] + 1, (first_task, last_task), data['directory']


def new_data(data):
    """позволяет пользователю ввести новые данные"""
    surname = input('Введите свою фамилию: ')
    lesson = int(input('Ведите номер урока: '))
    first_task, last_task = map(int, input('Введите 1-ое и последнее задание ').split())
    data['user_name'] = surname
    data['last_lesson'] = lesson
    with open('data.json', 'w+') as user_data:
        data['directory'] = directory = ask_directory()
        json.dump(data, user_data)
    return surname, lesson, (first_task, last_task), directory

def get_data():
    """функция получает данные"""
    with open('data.json', 'r') as user_data:
        try:
            data = json.load(user_data)
        except json.decoder.JSONDecodeError:
            data = {}
    if data:
        if data['directory']:
            if input(f"Введите 'YES' если вы хотите использовать фамилию: {data['user_name']}"
                    f" и создать файлы для {data['last_lesson'] + 1}-го "
                    f"занятия в папке {data['directory']}: ").upper() == 'YES':
                return json_data(data)
        else:
            if input(f"Введите 'YES' если вы хотите использовать фамилию: {data['user_name']}"
                     f" и создать файлы для {data['last_lesson'] + 1}-го занятия: ").upper() == 'YES':
                return json_data(data, False)
    return new_data(data)


def create_files():
    """создаёт файлы"""
    surname, lesson, (first_task, last_task), directory = get_data()
    if directory:
        for task in range(first_task, last_task + 1):
            f = open(f"{directory}/" + f'{surname}_{lesson}_{task}.py', 'w+')
    else:
        for task in range(first_task, last_task + 1):
            f = open(f'{surname}_{lesson}_{task}.py', 'w+')

if __name__ == '__main__':
    create_files()
