import re
path = 'Practice_7/catalog.txt'
catalog=""
#Чтение файла
def read_file():
    global catalog
    with open(path,'r',encoding='utf-8') as file:
        catalog = file.read().split('\n')
    return catalog

#Запись в файл
def add_file(str0, str1, str2):
    with open(path,'w',encoding='utf-8') as file:
        length = len(file.readlines())
        file.writelines(f'{length+1};{str1};{str2}\n')



#Экспорт файла в формата
