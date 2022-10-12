# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def multipliers_of_n(n):
    if n>0:
        result=[x for x in range(1,n+1) if not n %x]
        print(f'Множители числа {n} - {result}')
    else:
        print("Число должно быть натуральным!!!")

def Main():
    num =int(input('Введите число: '))
    multipliers_of_n(num)

Main()