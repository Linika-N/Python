# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import sympy
from random import randint

def polynomial(degree):
    if degree>0:
        x = sympy.Symbol('x')
        result = ((randint(0,10))*x + (randint(0,10)))**degree
        result = str(sympy.expand(result)) + " = 0"
        print(result)
        return result
    else:
        print("Степень должна быть натуральной!")

def write_to_file(str):
    path = 'Practice_4/Ex004/file.txt'
    data = open(path,'w')
    data.write(str)
    data.close()

def Main():
    k =int(input('Введите степень: '))
    answer = polynomial(k)
    write_to_file(answer)

Main()