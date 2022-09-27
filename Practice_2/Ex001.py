# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите число: ')
if num[0]=='-' or num[0]=='+':
    num=num[1:]
if '.' in num:
    num=num.split(".")
elif ',' in num:
    num=num.split(",")
num_final=''
num_final=num_final.join(num)
if num_final.isdigit():
    result=0
    for i in range(len(num_final)):
        result += int(num_final[i])
    print(f'Сумма цифр числа: {result}')
else:
    print("Не число!!!")