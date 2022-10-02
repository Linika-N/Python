# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_of_elements(numbers):
    if numbers.replace(" ", "").isdigit():
        num_list = numbers.split(" ")
        work_list = list(map(int,num_list))
        result=[]
        i = 0
        while i<len(work_list)/2:
            result.append(work_list[i]*work_list[len(work_list)-1-i])
            i+=1
        print(f'Произведение пар чисел списка:{result}')
    else:
        print("Нужен список чисел!!!")

def Main():
    list =input('Введите числа через пробел: ')
    mult_of_elements(list)

Main()