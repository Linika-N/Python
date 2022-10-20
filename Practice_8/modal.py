import re
#1-Добавление сотрудника в список
def add_line(file_function):
    data_employee = input('Введите ФИО сотрудника: ')
    data_number = input('Введите номер телефона: ')
    data_post = input('Введите должность: ')
    data_salary = input('Введите зарплату: ')
    info_phone = unic_numbers(data_number)
    file_function(data_employee,info_phone,data_post,data_salary)
    print('Добавлено')
#2-Поиск по сотруднику
def find_persons(file_func,type):
    data_search = input('Введите данные для поиска: ')
    if unic_numbers(data_search).isdigit() and (len(data_search)==11 or len(data_search)==10):
        data_search = unic_numbers(data_search)
    base = file_func()
    answer=[]
    for i in range(len(base)):
        if data_search in base[i]:
            answer.append(base[i])
    if type == 1:
        if len(answer)!=0:
            for i in range(len(answer)):
                answer[i] = answer[i].split(";")
                to_print=""
                for j in range(1,len(answer[i])):
                    to_print+=str(answer[i][j])+" "
                print(to_print)
        else:
            print('Человека с такой фамилией в списке нет')
    elif type == 2:
        return (answer,data_search)
#3-Изменение данных
def change_data(database_function,rewrite_function):
    all_base = database_function()
    (list,search) = find_persons(database_function,2)
    index_list =[]
    for i in range(len(all_base)):
        if search in all_base[i]:
            index_list.append(i)
    for i in range(len(list)):
        print(list[i])
    select = input("    Введите номер сотрудника из найденных для изменения данных\n или введите \"0\" для изменения данных всех найденных сотрудников: ")
    attr=int(input('''  Введите номер пункта, который хотите поменять: 
                    1. ФИО
                    2. Номер телефона
                    3. Должность
                    4. Зарплата     '''))
    data_change = input("   Введите новое значение данных: ")
    if unic_numbers(data_change).isdigit() and len(data_change)>=10:
        data_change = unic_numbers(data_change)
    if select ==0:
        for i in range(len(list)):
            change_attr = str(list[i]).split(";")
            change_attr[attr]=data_change
            list[i]=""
            for x in range(len(change_attr)):
                if x==len(change_attr)-1:
                    list[i]+=change_attr[x]
                else:
                    list[i]+=change_attr[x]+";"
            all_base[index_list[i]]= list[i]
            print(all_base[index_list[i]])
    else:
        for y in range(len(list)):
            list[y]=list[y].split(";")
            if select in list[y][0]:
                list[y][attr]= data_change
                unic_person = f'{list[y][0]};{list[y][1]};{list[y][2]};{list[y][3]};{list[y][4]}'
                list[y]=unic_person
                all_base[index_list[y]]= list[y]
                print(all_base[index_list[y]])
                break
    rewrite_function(all_base)
#4 - Удаление работника
def delete_person(database_f, rewrite_f):
    catalog = database_f()
    (persons_list, search) = find_persons(database_f,2)
    index_list =[]
    for i in range(len(catalog)):
        if search in catalog[i]:
            index_list.append(i)
    for i in range(len(persons_list)):
        print(persons_list[i])
    select = input("    Введите номер сотрудника из найденных для изменения данных\n или введите \"0\" для изменения данных всех найденных сотрудников: ")
    for y in range(len(persons_list)):
        check=persons_list[y].split(";")
        if select in check[0]:
            result = catalog.pop(index_list[y])
            print(f'{result} - удален')
    rewrite_f(catalog)






    


#Подгонка телефона под формат 84951356369
def unic_numbers(number):
    number = number.replace(" ","")
    number = re.sub(r'\D',"",number)
    number = re.sub('^7',"8",number)
    return number
