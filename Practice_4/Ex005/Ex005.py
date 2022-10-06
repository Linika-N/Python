# Даны два файла, в каждом из которых находится запись многочлена. З
# адача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11


import sympy
from random import randint

# создание многочлена
def polynomial(degree):
    x = sympy.Symbol('x')
    result = ((randint(0,10))*x + (randint(0,10)))**degree
    result = str(sympy.expand(result))
    return result

#запись в файл 
def write_to_file(file,str):
    path = file
    data = open(path,'w')
    data.write(str)
    data.close()


# сумма двух многочленов
def sum_of_poly(file1, file2):
    with open(file1) as first:
        first_file = first.read()
    with open(file2) as second:
        second_file = second.read()
    x = sympy.Symbol('x')
    answer = first_file + " + " + second_file
    answer = str(sympy.collect(answer,x))
    return answer

def Main():
    # степени многочленов
    a = randint(1,5)
    b = randint(1,5)
    # пути к файлам
    a_path = 'Practice_4/Ex005/file.txt'
    b_path = 'Practice_4/Ex005/file2.txt'
    res_path = 'Practice_4/Ex005/file3.txt'
    # создние многочленов
    a_poly = polynomial(a)
    b_poly = polynomial(b)
    # запись в файлы многочленов
    write_to_file(a_path,a_poly)
    write_to_file(b_path,b_poly)
    # сумма многочленов
    res = sum_of_poly(a_path,b_path)
    # запись в файл суммы многочленов
    write_to_file(res_path, res)
    print('Готово!')

Main()