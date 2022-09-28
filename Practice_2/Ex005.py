# Реализуйте алгоритм перемешивания списка.

from random import shuffle

def mixing_list(list_size):
    if list_size.isdigit() and int(list_size)>1:
        list_size=int(list_size)
        result=[(i+1) for i in range(list_size)]
        print(f'N = {list_size}, Список:\n {result}')
        shuffle(result)
        print(f'Перемешанный список:\n {result}')
    else:
        print("Нужно ввести число больше 1!!!")


def Main():
    lenght =input('Введите число элементов: ')
    mixing_list(lenght)

Main()