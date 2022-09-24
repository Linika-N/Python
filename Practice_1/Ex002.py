# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите числа 0 или 1 для следующих переменных: ')
x=int(input('Введите значение X: '))
while x!=0 and x!=1:
   x=int(input('Введите значение X: '))
else: 
    y=int(input('Введите значение Y: '))
    while y!=0 and y!=1:
        y=int(input('Введите значение Y: '))
    else: 
        z=int(input('Введите значение Z: '))
        while z!=0 and z!=1:
            z=int(input('Введите значение Z: '))

first = not(x or y or z)
second = not x and not y and not z  
print(f'x = {x}, y = {y}, z = {z}')
print(f'x or y or z = {x} или {y} или {z} = {x or y or z}')
print(f'not(x or y or z) = not {x or y or z} = {not x or y or z}')
print(f'not x = {not x}, not y = {not y}, not z = {not z}')
print(f'not x and not y and not z = {not x and not y and not z}')
print(f'{first} - {second}')
if first == second:
    print('Утверждения истины')
else:
    print('Утверждения ложны')