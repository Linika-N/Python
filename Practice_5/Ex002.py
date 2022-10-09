# Создайте программу для игры в ""Крестики-нолики"".

from os import system
from random import randint

# Вывод игрового поля в консоль
def array_print(arr):
    for i in range(len(arr)):
        print(arr[i])


# Проверка игрового поля на выигрыш
def check_field(array, player_symbol):
    count = [0,0,0,0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[j][i]==player_symbol:
                count[0]+=1
            if array[i][j]== player_symbol:
                count[1]+=1
        if count[0]!=len(array):
            count[0] = 0
        else:
            return count[0]
        if count[1]!= len(array):
            count[1] = 0
        else:
            return count[1]
        if array[i][i]==player_symbol:
            count[2]+=1
        if array[len(array)-1-i][i]==player_symbol:
            count[3]+=1
    for i in range(len(count)):
        if count[i] == len(array):
            return count[i]
    return 0


# Проверка ячеек игрового поля на попытку повторного ввода
def check_symbol(array, position):
    if position[0]==0 and position[1]==0:
        position = [1,1]
    if array[position[0]-1][position[1]-1]=='_':
        return True
    else:
        return False

# Проверка игрового поля на полное заполнение
def check_array(arr):
    check = False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]=='_':
                check = True
                return check
    return check


# Очистка консоли
clear = lambda: system('cls')

# Создание игрового поля
def field():
    size = 0 
    while size < 3 or size > 5:
        size = int(input('Добро пожаловать в игру "Крестики-нолики"\nКакого размера будет поле? Введите цифру от 3 до 5: '))
    array = [['_']*size for i in range(size)]
    return array

# Ход игры
def fill_field(array):
    game_field = array
    select = randint(0,1)
    players = ['X','O']
    move = [0,0]
    end = 0
    while end != len(game_field):
        clear()
        array_print(game_field)
        print(f'Игрок {select+1}, Ваш ход')
        while move[0]<1 or move[0]>len(game_field) or move[1]<1 or move[1]> len(game_field) or check_symbol(game_field,move)==False:
            move = [int(i) for i in (input("Введите номер строки и столбца для заполнения через пробел: ").split())]
            if check_array(game_field)== False:
                break
        game_field[move[0]-1][move[1]-1] = players[select]
        array_print(game_field)
        end = check_field(game_field,players[select])
        if end !=len(game_field):
            if check_array(game_field)==False:
                select = 2
                clear()
                array_print(game_field)
                return select
            select = len(players)-1-select
            move=[0,0]
    clear()
    array_print(game_field)
    return select
    
#Главное меню
def Main():
    clear()
    g_field = field()
    winner = fill_field(g_field)+1
    if winner == 3:
        print('Ничья! Победителей нет!')
    else:
        print(f'Игрок {winner} - победитель')
Main()