## Упаковка (оператор *)
#var1 = 34
#var2 = 'Python'
#var3 = True
#*my_list, = var1, var2, var3
#print(my_list)
#
#
## Распаковка *
#list = [23, 'Hello', False] * 2
##a, b, c = list
#c, *a, b = list
#print(c, a, b)
#
#def f(*param):
#    print(param[2:5])
#
#f(23, 5,76,908, 7,0)
#
#
## Распаковка **
#def f(**kwargs):
#    print(kwargs)
#
#f(param1 = 14, param2 = 'Python', param3 = True)


# Распаковка в цикле
#list_users = [
#    ['Joe', 'Byden'],
#    ['Donald', 'Tramp'],
#    ['Micky', 'Mouse']
#]

#for name, last_name in list_users:
#    print(f'name: {name}; Last name: {last_name}\n')
#line = -7, 10
#print(line)
#for i in range(*line):
#    print(i)

#print(*range(10))


#Есть некоторый словарь, который хранит названия
#стран и столиц. Название страны используется в качестве
#ключа, название столицыв качестве значения. Необходимо
#реализовать: добавление данных, удаление данных, поиск
#данных, редактирование данных, сохранение и загрузку
#данных (используя упаковку и распаковку).

#def add_data(country_dict):
#    data = input('type country and capital in a space')
#    country, capital = data.split(' ')
#    if country in country_dict.keys():
#        print('this country is already exist')
#    else:
#        country_dict[country] = capital
#    return country_dict
#
#def delete_data(country_dict):
#    data = input('type country to delete')
#    if data in country_dict.keys():
#        del country_dict[data]
#        print(f'country {data} is deleted!')
#    else:
#        print('error! it isnt that country')
#    return country_dict
#
#def search_dict(country_dict):
#    data = input('type country or capital')
#    for country, capital in country_dict.items():
#        if data == country or data == capital:
#            print(f'result of search is:\n {country} {capital}')
#            break
#    else:
#        print('no matches found')
#    return country_dict
#
#def edit_dict(country_dict):
#    data = input('type new country and capital')
#    country, capital = data.split(' ')
#    country_dict[country] = capital
#    return country_dict
#
#def save_dict(country_dict):
#    data = ''
#    for key, value in country_dict.items():
#        data += f'{key}:{value}\n'
#    with open('country_dict.txt', 'w') as file:
#        file.write(data)
#    return country_dict
#
#def loading_data(country_dict):
#    with open('country_dict.txt', 'r') as file:
#        for line in file:
#            country, capital = line.split(':')
#            country_dict[country] = capital[:-1]
#    return country_dict
#
#country_dict = {}
#loading_data(country_dict)
#while True:
#    print(country_dict)
#    choice = int(input('country and Capital \nmenu: \n1-add \n2-delete \n3-search \n4-edit \n5-save \n6-Data loading \n0-exit'))
#    if choice == 0:
#        save_dict(country_dict)
#        break
#    elif choice == 1:
#        add_data(country_dict)
#    elif choice == 2:
#        delete_data(country_dict)
#    elif choice == 3:
#        search_dict(country_dict)
#    elif choice == 4:
#        edit_dict(country_dict)
#    elif choice == 5:
#        save_dict(country_dict)
#    elif choice == 6:
#        loading_data(country_dict)
        


#Задание 2
#Есть некоторый словарь, который хранит названия
#музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
#альбомов в качестве значения. Необходимо реализовать:
#добавление данных, удаление данных, поиск данных,
#редактирование данных, сохранение и загрузку данных
#(используя упаковку и распаковку).

class Music:
    music_dict = {}

    def add_band(self, name_band):
        band = Band(name_band)
        self.music_dict[band.name] = band.discography

class Band:
    def __init__(self, name):
        self.name = name
        self.discography = []

    def add_album(self, name_alb):
        self.discography.append(name_alb)

spotify = Music()
spotify.add_band('Depeche Mode')
print(spotify.music_dict)

        