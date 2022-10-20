import modal
import logger

#Ввод запроса
def user_request():
    req=0
    try:
        while req<1 or req>4:
            req = int(input("Выберите пункт, наиболее подходящий под Ваш запрос: "))
    except ValueError:
        print('Это не число!')
    return req
#Выбор функции
def choice_function(number):
    if number == 1:
    #1-Добавление нового сотрудника
        return modal.add_line(logger.add_file)
    #2-Поиск по фамилии или номеру телефона
    elif number ==2:
        return modal.find_persons(logger.read_file,1)
    #3-Изменение данных
    elif number ==3:
        return modal.change_data(logger.read_file,logger.rewrite_file)
    #Удаление сотрудника
    elif number ==4:
        return modal.delete_person(logger.read_file,logger.rewrite_file)
# Вывод ответа
def user_response(numb):
    choice_function(numb)


