# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from random import randrange
import re

def poly(k):
    poly = ''
    n = 0
    for i in reversed(range(len(k))):
        r = k[n]
        r = '' if r == 1 else f'{r}*'
        if i >= 2: poly += f'{r}X^{i} + '
        elif i == 1: poly += f'{r}X + '
        else: poly += f'{k[n]} = 0'
        n += 1
    return poly

f1 = re.findall('[0-9]+', open("c:/Users/User/Documents/Обучение Программист Python Цифровые профессии/ДЗ/2 четверть/Знакомство с языком Python/1/Python-Education/poly.txt", "r").read())
f2 = re.findall('[0-9]+', open("c:/Users/User/Documents/Обучение Программист Python Цифровые профессии/ДЗ/2 четверть/Знакомство с языком Python/1/Python-Education/poly2.txt", "r").read())
fNew = []
for i in range(len(f1)):
    fNew.append(int(f1[i]) + int(f2[i]))

with open("c:/Users/User/Documents/Обучение Программист Python Цифровые профессии/ДЗ/2 четверть/Знакомство с языком Python/1/Python-Education/poly3.txt", "w") as f3:
    f3.write(poly(fNew))

print(f'Cуммa многочленов - {poly(fNew)}')