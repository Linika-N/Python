import user_interface
import os

clear=lambda: os.system('cls')

def main():
    clear()
    print("""Привет! Добро пожаловать в справочник версии 1.2!
    1. Добавить номер в список.
    2. Поиск по фамилии.
    3. Поиск по номеру""")
    num = user_interface.user_request()
    user_interface.user_response(num)

main()