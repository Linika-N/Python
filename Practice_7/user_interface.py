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
#Выбор функции
def choice_function(number):
    if number == 1:
    #1-Добавление номера
        info_name = input('Введите ФИО человека для добавления в справочник: ')
        info_number = input('Введите номер телефона: ')
        return modal.add_line(info_name,info_number)
    #2-Поиск по фамилии или номеру телефона
    elif number ==2:
        return modal.find_surname_or_number(input('Введите фамилию или номер телефона: '))
# Вывод ответа
def user_response(numb):
    choice_function(numb)


