#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_binary(number):
    if number.isdigit():
        decimal = int(number)
        result=""
        while decimal != 0:
            result = str(decimal%2) + result
            decimal = int(decimal/2)
        print(f'Десятичное число {number} в двоичной системе - {result}')
    else:
        print("Нужен список чисел!!!")

def Main():
    num =input('Введите число: ')
    to_binary(num)

Main()