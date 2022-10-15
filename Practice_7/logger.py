path = 'Practice_7/catalog.txt'
catalog=""
#Чтение файла
def read_file():
    global catalog
    with open(path,'r',encoding='utf-8') as file:
        catalog = file.read()

#Запись в файл
def add_file(str1, str2):
    count = 0
    with open(path,'r+',encoding='utf-8') as file:
        print(file)
        print(file.readlines())
        for line in file:
            count +=1
            print(count)
        file.writelines(f'{count};{str1};{str2}\n')

#Экспорт файла в форматах
add_file('Иванов Иван Иванович', '+7 (495) 4567158')
