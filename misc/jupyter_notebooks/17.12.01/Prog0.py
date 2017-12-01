# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:19:32 2017

@author: Friend
"""
"""
Простая программа, которая ничего не делает
"""

import argparse
#Создание парсера - объекта класса ArgumentParser, разделяющего аргументы.
#Так и назовём этот объект - parser
parser = argparse.ArgumentParser()
#Собственно разделение аргументов через метод parse_args().
#Пока разделять нечего - мы никаких аргументов не добавляли
parser.parse_args()


"""
Для демонстрации - запустить
python Prog0.py
python Prog0.py -h      - появится help, пока что не носящий особой информации
python Prog0.py --help
python Prog0.py meow    - выдаст ошибку, т. к. никаких аргументов мы этой
                        программе ещё не задавали
"""