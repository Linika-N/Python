import modal

#Ввод запроса
def user_request():
    req=0
    try:
        while req<1 or req>5:
            req = int(input("Выберите пункт, наиболее подходящий под Ваш запрос: "))
    except ValueError:
        print('Это не число!')
    return req

def choice_function(number):
    if number == 1:
    #1-Добавление номера
        info_name = input('Введите ФИО человека для добавления в справочник: ')
        info_number = input('Введите номер телефона: ')
        return modal.add_line(info_name,info_number)
    #2-Поиск по фамилии
    elif number ==2:
        return modal.find_surname(input('Введите фамилию: '))
    #3-Проверка есть ли номер в справочнике
    elif number ==3:
        return modal.check_number(input('Введите номер телефона: '))

def user_response(numb):
    choice_function(numb)
#4-Удаление

#5-Создание файла для выгрузки


