# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

def pi(dg):
    if dg<=-1 and dg>=-10:
        x = str(math.pi)
        print(f'Число ПИ с заданной точностью {10**dg} - {x[:2+abs(dg)]}')
    else:
        print("Нужна степень от -1 до -10!!!")

def Main():
    degree =int(input('Введите степень 10 от -1 до -10: '))
    pi(degree)

Main()