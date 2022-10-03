# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import re

def is_float(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def check_list(array):
    i=0
    check = True
    while check and i<len(array):
        check = is_float(array[i])
        i+=1
    return check

def diff_between_min_max(numbers):
    num_list = numbers.split(" ")
    if check_list(num_list):
        work_list = list(map(lambda x: re.sub(r'\d+\.', "0.", x),num_list))
        work_list = list(map(float,work_list))
        work_list = list(filter(lambda x: x<1, work_list))
        print(work_list)
        result = max(work_list)- min(work_list)
        print(f'Разница между максимальной и минимальной дробной частью элементов:{result}')
    else:
        print("Нужен список чисел!!!")

def Main():
    list =input('Введите вещественные числа через пробел: ')
    diff_between_min_max(list)

Main()