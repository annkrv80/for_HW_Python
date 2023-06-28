#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import re

def absolute_path(link):  
    *path, full_name_file = link.split('\\')
    name_file, exept_file = full_name_file.split('.') 
    print(f'({path}, {name_file}, {exept_file})')


absolute_path(r'C:\Users\Пользователь\Desktop\Seminar_Python\Seminar_5\Task_01.py')