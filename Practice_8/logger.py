path = 'Practice_8/database.txt'
catalog=""
#Чтение файла
def read_file():
    global catalog
    with open(path,'r',encoding='utf-8') as file:
        catalog = file.read().split('\n')
    return catalog

#Запись в файл
def add_file(data_person,number,post,salary):
    with open(path,'a+',encoding='utf-8') as file:
        base = read_file()
        length = len(base)
        file.write(f'{length};{data_person};{number};{post};{salary};\n')

#Перезапись данных
def rewrite_file(array):
    with open(path,'w',encoding='utf-8') as file:
        for i in range(len(array)):
            file.write(f'{array[i]}\n')