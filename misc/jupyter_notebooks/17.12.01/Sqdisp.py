# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:19:04 2017

@author: Friend
"""
"""
Программа, вычисляющая квадрат числа.
Может выдавать сообщение с результатом 
разными способами по выбору в зависимости
от ключа-цифры.
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", 
                    type=int, 
                    #указание набора значений, которые может принимать
                    #аргумент verbosity (если указан)
                    
                    choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 = {}".format(args.square, answer))
else:
    print(answer)
    
"""
Для демонстрации - запустить
python Sqdisp.py 9
python Sqdisp.py 9 -v 0
python Sqdisp.py 9 -v 1
python Sqdisp.py 9 -v 2
python Sqdisp.py 9 -v 3 - выдаст ошибку, поскольку число 3 не принадлежит
                          возможному набору значений аругмента verbosity
"""