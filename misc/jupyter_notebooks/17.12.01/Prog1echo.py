# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:00:50 2017

@author: Friend
"""
"""
Добавление позиционного аргумента имени echo. 
Вывод на экран того, что было введено при вызове данного скрипта
"""
import argparse
#Создание парсера - объекта класса ArgumentParser, разделяющего аргументы.
#Так и назовём этот объект - parser
parser = argparse.ArgumentParser()
#Добавление позиционного аргумента, назовём его echo
#Он имеет имя echo
#parser.add_argument("echo")
"""
Как сделать help действительно помогающим
"""
parser.add_argument("echo", help="echo the string you write")
#Теперь метод parse_args() передаёт в переменную args всю информацию,
#которую мы ввели в командную строку
#Собственно разделение аргументов через метод parse_args().
args = parser.parse_args()
#Обращение к переменной echo, её имя - то, что было внутри кавычек
#при добавлении аргумента
print(args.echo)

"""
Для демонстрации - запустить
python Prog1echo.py Hello!
python Prog1echo.py Hello, World! - выдаст ошибку, так как ожидался один 
позиционный аргумент, а подано было два (аргументы разделяются пробелами)
"""