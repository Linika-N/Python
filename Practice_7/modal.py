import re
import logger
#1-Добавление номера
def add_line(info_person,phone):
    info_phone = unic_numbers(phone)
    logger.add_file(info_person,info_phone)
    print('Добавлено')
#2-Поиск по фамилии
def find_surname(surname):
    phone_book = logger.read_file()
    answer=[]
    for x in range(len(phone_book)):
        if surname in phone_book[x]:
            answer.append(phone_book[x])
    if len(answer)!=0:
        for i in range(len(answer)):
            answer[i] = answer[i].split(";")
            print(str(answer[i][1]) + "\n" + str(answer[i][2])) 
    else:
        print('Человека с такой фамилией в списке нет')
#3-Проверка номера в справочнике
def check_number(number):
    print('Номер найден')
#4-Удаление
#5-Создание файла для выгрузки

#Подгонка телефона под формат 84951356369
def unic_numbers(number):
    number = number.replace(" ","")
    number = number.replace('+7',"8")
    number = re.sub(r'\D',"",number)
    return number
