#FACADE - суть паттерна в объединении структуры классов в один интерфейс.
#создайте реализацию паттерна Facade. Протестируйте работу созданного класса
#Симулировать выпуск цифрового продукта. Продукт является результатом действия трех составных: дизайн, программирование, тестирование

#class Designe:
#    def __init__():
#        return f'результат деятельности отдела дизайна'
#    
#class Programmer:
#    def __init__(self):
#        return f'результат деятельности отдела програмирования'
#    
#class Tester:
#    def __init__(self):
#        return f'результат деятельности отдела тестирования'
#    
#class WebStudio: #наш фасад
#    def __init__(self, name):
#        self.name = name
#
#    def get_designe(self):
#        return Designe()
#
#web_studio = WebStudio('студия цифровых продуктов')
#
#print(web_studio.get_designe())



#adapter - позволяет несовместимым объектам работать вместе

#Создайте реализацию паттернаAdapter. Протестируйте
#работу созданного класса. Есть два кашелька в rub  и tng, нужно сделать адаптер для конвертации валют

#class WalletRub:
#    def __init__(self, cashe):
#        self.cashe = cashe
#
#    def cb(self):
#        print(f'{self.cashe} RUB')
#
#class WalletTenge:
#    def __init__(self, cashe):
#        self.cashe = cashe
#
#    def cb(self):
#        print(f'{self.cashe} TENGE')
#
#class AdapterRubToTenge:
#    def __init__(self, cashe):
#        self.cashe = cashe * 6.26
#
#    def cb(self):
#        print(f'{self.cashe} TENGE')
#
#my_wallet_ru = WalletRub(100)
#my_wallet_ru.cb()
#
#kzfriend_wallet_tenge = WalletTenge(12)
#kzfriend_wallet_tenge.cb()
#        
#My_Wallet_kzt = AdapterRubToTenge(my_wallet_ru.cashe)
#My_Wallet_kzt.cb()



#Strategy
#Создайте реализацию паттерна Strategy. Протестируйте
#работу созданного класса. Пользователь выбирает стратегию продажи или аренды недвижимости.

#class User:
#    def __init__(self):
#        pass
#
#    def start(self, strategy):
#        print(strategy)
#
#class Strategya:
#    list_product = ['площадь 20 кв.м', 'площадь 230 кв.м']
#    def strategy():
#        return Strategya.list_product
#
#class Strategyb:
#    list_product = ['площадь 2400 кв.м', 'площадь 3000 кв.м']
#    def strategy():
#        return Strategyb.list_product
#
#user = User()
#user.start(Strategya.strategy())
#print('2 hours later')
#user.start(Strategyb.strategy())



#iterator позволяет итерировать (перебирать) элементы объекта класса, сохраняя все принципы инкапсуляции
#Есть список (каталог) товаров, создать класс и метод вывода каталога товаров

#class Market:
#    def __init__(self, list_product):
#        self.list_product = list_product
#        self.index = 0
#
#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        if self.index < len(self.list_product):
#            product = self.list_product[self.index]
#            self.index += 1
#            return product
#        else:
#            raise StopIteration
#        
#products = ['Чокопай', 'Яшкино', 'Орео', 'меллер'] 
#wb = Market(products)
#for product in wb:
#    print(product)




#В каждом учебном заведении есть студенты.Студенты
#входят в состав групп. Вам необходимо создать эмуляцию учебного процесса. Приложение должно позволять
#добавлять, удалять, изменять информацию о студентах
#и группах. При реализации используйте паттерн Iterator
#(для отображения студентов, входящих в группу) и другие
#необходимые паттерны.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update(self):
        menu = input('update\n1-name\n2-age')
        new_info = input('enter a new value')
        if menu == '1':
            self.name = new_info
        else:
            self.age = int(new_info)

class Group:
    def __init__(self, name):
        self.name = name
        self.list_students = []
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.list_students):
            product = self.list_students[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
        
    def add_students(self, name, age):
        self.list_students.append(Student(name, age))

    def delete_student(self, name_s):
        for index_student in range(len(self.list_students)):
            if self.list_students[index_student].name == name_s:
                student = self.list_students[index_student]
                self.list_students.pop(index_student)
                del student
                return self.list_students
            
    def update(self, new_name):
        self.name = new_name
        return self 
    

    def render_g(self):
        print(f'group"{self.name}"')
        num = 1
        for student in self.list_students:
            print(f'{num}, name {student.name}, age {student.age}')
            num += 1


class Academy:
    def __init__(self, name):
        self.name = name
        self.list_group = []
        self.index = 0
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(self.list_group):
            product = self.list_group[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
        
    def add_g (self, name):
        self.list_group.append(Group(name))

    def delete_Group(self, name_g):
        for index_student in range(len(self.list_group)):
            if self.list_group[index_student].name == name_g:
                student = self.list_group[index_student]
                self.list_group.pop(index_student)
                del student
                return self.list_group
            
    def add_student(self, name_g, name_s, ags):
        for group in self.list_group:
            if name_g == group.name:
                group.add_students(name_s, ags)

academy = Academy('TOP')

while True:
    print('menu')
    menu = input('1-add group\n2-add student in group\n3-groups output\n4-group list output\n5-delete group\n6-delete student\n7-edit group info\n8-edit student info\n0-exit\n')
    if menu == '1':
        group_n = input('enter group name')
        academy.add_g(group_n)
    elif menu == '2':
        info = input('enter group name, name of student, age separated by commas')
        group_n, name_s, afe_s = info.split(',')
        academy.add_student(group_n, name_s, afe_s)
    elif menu == '3':
        print(f'academy {academy.name}')
        for group in academy:
            print(group.name )
    elif menu == '4':
        group_n = input('enter group name')
        for group in academy:
            if group.name == group_n:
                group.render_g()
                break
            else:
                print('this group isnt exist')
    elif menu == '5':
        group_n = input('enter group name')
        academy.delete_Group(group_n)
    elif menu == '6':
        group_n, name_s = input('enter group name and name of student separated by commas').split(',')
        for group in academy:
            if group.name == group_n:
                group.delete_student(name_s)
                break
            else:
                print('this group dont exist')
    elif menu == '7':
        group_n = input('enter group name')
        new_group_n = input('enter new group name')
        for group in academy:
            if group.name == group_n:
                group.update(new_group_n)
    elif menu == '8':
        group_n, name_s = input('enter group name and name of student separated by commas').split(',')
        for group in academy:
            if group.name == group_n:
                for student in group:
                    if name_s == student.name:
                        student.update()
    elif menu == '0':
        print('the end of the program')
        break

#std1, std2, std3 = Student('Joe', 15), Student('Leo', 15), Student('Max', 15)
#top = Academy('top')
#top.add_g('Python42')
#top.add_g('WEB42')
#top.add_g('designe2')
#top.add_student('Python42', 'Joe', 15)
#top.add_student('Python42', 'Leo', 19)
#top.add_student('WEB42', 'Max', 15)
#top.add_student('WEB42', 'Anna', 16)
#top.add_student('designe2', 'Olga', 26)
#top.add_student('designe2', 'Poly', 23)
#for group in top:
#    print(group.name)
#    group.render_g()
#print(std1.__dict__,std2.__dict__,std3.__dict__)
#group1 = Group('Python42')
#group1.add_students(std1)
#group1.add_students(std2)
#group1.add_students(std3)
##print('group', group1.name)
##for student in group1:
##    print(student.name, student.age)
#group1.render_g()
#group1.delete_student('Leo')
#group1.update('Python 43')
#group1.render_g()


