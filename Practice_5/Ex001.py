# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from os import system
from random import randint
from math import floor


# Начало игры
def start_game():
    print("""
    Добро пожаловать в игру!
    Выберите вариант игры:
    1. С компьютером.
    2. Два игрока.
    3. С "умным" компьютером. """)
    a=0
    while a<1 or a>3:
        a = int(input("    Что выбираем? "))
    return a

# Режим двух игроков - пользователей     
def two_players(cand):
    candies = cand
    # 0 индекс - это компьютер, 1 игрок - это пользователь
    players= [0,0]
    move = 29
    select=randint(0,1)
    print('Итак, на столе лежит 2021 конфета')
    while candies!=0:
        while move>28:
            print(f'Игрок {select+1}, Ваш ход.')
            move = int(input(f'Сколько конфет заберем? Помни, не больше 28!    -   Осталось {candies} конфет.  '))    
        if candies-move>=0:
            players[select]+=move
            candies -= move
            if candies != 0:
                select = len(players)-1-select
        move=29
    return select+1

# Режим игры с компьютером
def bot_player(cand):
    candies = cand
    # 0 индекс - это компьютер, 1 игрок - это пользователь
    players = [0,0]
    move=29
    select = randint(0,1)
    print('Итак, на столе лежит 2021 конфета')
    while candies!=0:
        while move>28:
            if select == 1:
                print(f'Игрок, Ваш ход.')
                move = int(input(f'Сколько конфет заберем? Помни, не больше 28!    -   Осталось {candies} конфет.  ')) 
                print('___________________________________________')
            else:
                print('Ход компьютера')
                if candies>=28:
                    move = randint(1,28)
                    print(f'Компьютер забирает {move} конфет.                      -   Осталось {candies-move} конфет.\n___________________________________________')
                else:
                    move = candies
                    print(f'Компьютер забирает {move} конфет.                      -   Осталось {candies-move} конфет.\n___________________________________________')

        if candies-move>=0:
            players[select]+=move
            candies -= move
            if candies != 0:
                select = len(players)-1-select
        move=29
    return select+1

# Режим игры с "умным" компьютером
def clever_bot_player(cand):
    candies = cand
    # 0 индекс - это компьютер, 1 игрок - это пользователь
    players = [0,0]
    move=29
    select = randint(0,1)
    print(f'Итак, на столе лежит {candies} конфета')
    while candies!=0:
        while move>28:
            if select == 1:
                print(f'Игрок, Ваш ход.')
                move = int(input(f'Сколько конфет заберем? Помни, не больше 28!    -   Осталось {candies} конфет.  ')) 
                print('___________________________________________')
            else:
                print('Ход компьютера')
                if candies > 28:
                    move=candies - floor(candies / move)*move
                    print(f'Компьютер забирает {move} конфет.                      -   Осталось {candies} конфет.\n___________________________________________')
                else:
                    move = candies
                    print(f'Компьютер забирает {move} конфет.                      -   Осталось {candies} конфет.\n___________________________________________')

        if candies-move>=0:
            players[select]+=move
            candies -= move
            if candies != 0:
                select = len(players)-1-select
        move=29
    return select+1

# Ход игры
def game(choice):
    total_candies = 2021
    if choice == 2:
        win = two_players(total_candies)
    elif choice ==1:
        win = bot_player(total_candies)
    else:
        win = clever_bot_player(total_candies)

    return win

# Очистка консоли
clear = lambda: system('cls')

# Печать информации о победителе
def print_winner(choice,player):
    type = choice
    winner = player
    if type == 1 or winner ==1:
        print('Компьютер выиграл!')
    elif type==2:
        print(f'Игрок {winner}-выиграл!!!')
    elif type ==3 or winner ==1:
        print('Игрок победил!!!')

# Игра
def Main():
    clear()
    type = start_game()
    winner = game(type)
    print_winner(type,winner)

Main()        