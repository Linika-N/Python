path = 'Practice_7/catalog.txt'
export_path = 'Practice_7/export.txt'
catalog=""
#Чтение файла
def read_file():
    global catalog
    with open(path,'r',encoding='utf-8') as file:
        catalog = file.read().split('\n')
    return catalog

#Запись в файл
def add_file(str1, str2):
    with open(path,'r+',encoding='utf-8') as file:
        length = len(file.readlines())
        file.write(f'{length+1};{str1};{str2}\n')

#Экспорт файла с найденными строками
def export(array):
    with open(export_path,'w',encoding='utf-8') as file:
        count = 1
        for i in range(len(array)):
            file.write(f'{count}.{array[i][1]}, телефон {array[i][2]}\n')
            count+=1