# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_of_odd_position(numbers):
    if numbers.replace(" ", "").isdigit():
        num_list = numbers.split(" ")
        sum=0
        for i in range(1,len(num_list),2):
            sum += int(num_list[i])
        print(f'Сумма элементов на нечетных позициях списка:{sum}')
    else:
        print("Нужен список чисел!!!")

def Main():
    list =input('Введите числа через пробел: ')
    sum_of_odd_position(list)

Main()