# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:49:10 2017

@author: Friend
"""

"""
Расчёт массы галактики по её видимой звёздной величине, красному смещению
и среднему по этой галактике отношению "масса-светимость"
"""
import numpy as np
import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-m","--mag", type=float, metavar='',
                    help='visual stellar magnitude of the galaxy in B band\noptional, if you don\'t specify it, it will be assigned with 10 mag')
parser.add_argument("-r","--redshift", type=float, metavar='',
                    help="redshift of the galaxy\noptional, if you don\'t specify it, it will be assigned with 0.002")
parser.add_argument("-d","--divMtoL", type=float, metavar='', 
                    #если закомментировать metavar='', 
                    #то будут выдаваться названия аругментов с большими буквами
                    help="""Mass-to-Luminosity in B ratio of the galaxy in Solar units\noptional, if you don't specify it, it will be assigned with 2 Solar units""")

lsp = parser.parse_args()
#Будет выдан словарь с ключами - названиями опциональных аргументов,
#под которыми находятся соответствующие значения, введённые с клавиатуры
#Если какой-то аргумент не указан при вызове с команды, под соответствующим
#ключом будет значение None
args = vars(lsp)
#Оставим в словаре только те пары ключей-значений, у которых значения не None
args = { k : args[k] for k in args if args[k] != None }
#Словарь со значениями по умолчанию для опциональных аргументов
params = {'mag':10,'redshift':0.002,'divMtoL':2}
#Переписывание значениями, введёнными с клавиатуры
for k,v in args.items():
    params[k] = v
#Расчётная часть
m = params['mag']
z = params['redshift']
MtoL = params['divMtoL']
#Расстояние до галактики в парсеках
D = 3e5*z/72*1e6
#Абсолютная звёздная величина
M = m+5-5*np.log10(D)
#Светимость в светимостях Солнца в полосе B
#абсолютная звёздная величина Солнца в полосе B равна 5.5 mag
L = 10**(0.4*(5.5-M))
#Искомая масса галактики в массах Солнца
Mass = MtoL * L
#Вывод в экспоненциальной форме
print('Mass of the galaxy is {:.2e} Solar masses'.format(Mass))