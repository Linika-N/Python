import re
import logger
#1-Добавление номера
def add_line(info_person,phone):
    info_phone = unic_numbers(phone)
    logger.add_file(info_person,info_phone)
    print('Добавлено')
#2-Поиск по фамилии или номеру
def find_surname_or_number(string):
    if unic_numbers(string).isdigit():
        string = unic_numbers(string)
    phone_book = logger.read_file()
    answer=[]
    for x in range(len(phone_book)):
        if string in phone_book[x]:
            answer.append(phone_book[x])
    if len(answer)!=0:
        for i in range(len(answer)):
            answer[i] = answer[i].split(";")
            print(str(answer[i][1]) + "\n" + str(answer[i][2]))
        exp = input('Хотите загрузить результаты поиска в файл? Введите "Да" или "Нет": ')
        if exp.lower() == "да":
            logger.export(answer)
            print("Файл для выгрузки готов!")
    else:
        print('Человека с такой фамилией в списке нет')
#Подгонка телефона под формат 84951356369
def unic_numbers(number):
    number = number.replace(" ","")
    number = re.sub(r'\D',"",number)
    number = re.sub('^7',"8",number)
    return number
