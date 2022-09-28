# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

def mult_num(n):
    if n.isdigit() and int(n)>0:
        n=int(n)
        result=[]
        for i in range(-n,n+1):
            result.append(i)
        print(f'N = {n}, Набор элементов: {result}')
        with open('Practice_2\Ex004.file\\file.txt') as x:
            file = x.read().split("\n")
        print(f'Позиции из файла: {file}')
        mult=1
        for i in range(len(file)):
            if int(file[i])<len(result):
                mult *= result[int(file[i])]
        print(f'Произведение элементов последовательности от [-{n};{n}] по позициям из файла:\n {mult}')
    else:
        print("Нужно ввести число больше 0!!!")

def Main():
    num =input('Введите число элементов: ')
    mult_num(num)

Main()