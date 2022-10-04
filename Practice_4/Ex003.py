# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def numbers_to_set(numbers):
    if numbers.replace(" ", "").isdigit():
        result = set(numbers.split())
        print(f'Список неповторяющихся элементов - {result}')
    else:
        print("Нужен список чисел!!!")

def Main():
    nums =input('Введите числа через пробел: ')
    numbers_to_set(nums)

Main()