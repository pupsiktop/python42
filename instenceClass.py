##static method
#class MyClass:
#    def example_method(self):
#        print('метод экземпляра класса')
#
#    @staticmethod # статический - значит принадлежащий только классу (не экземплярам)
#    def static_method(name):
#        print('статический метод', name)
#
#obj = MyClass()
##obj.example_method()
##MyClass.static_method('MyClass')





#class User:
#    def __init__(self, name, last_name, mobile, email, age ):
#        self.name = name
#        self.last_name = last_name
#        self.mobile = mobile
#        self.email = email
#        self.age = age
#
#    def other_method(self):
#        print('некоторый метод')
#
#class Student(User):
#    def __init__(self, name, last_name, mobile, email, age, group):
#        super().__init__(name, last_name, mobile, email, age)
#        self.group = group
#
#    def lesson(self):
#        print('go on the lesson')
#
#class Teacher(User):
#    def __init__(self, name, last_name, mobile, email, age):
#        super().__init__(name, last_name, mobile, email, age)
#
#    def lesson(self):
#        print('do a lesson')
#
#student = Student('donald', 'Tramp', '34567532', 'waterwaterbro@mail.ru', 66, 'python42')
#print(student.__dict__)
#student.lesson()
#
#teacher = Teacher('pupsik', 'top', '34567532', 'waterwaterbro@mail.ru', 10909)
#teacher.lesson()
#
##функция issubclass()
#print(issubclass(Student, User))
#
##функция isinstance
#print(isinstance(student, Student))
#print(isinstance(teacher, Student))
#print(isinstance(student, User))
#print(isinstance(True, int))



#class Human:
#    count=0
#
#    @staticmethod
#    def get_count():
#        print(f'колтчество созданых экземпляров класса{Human.count}')
#
#    def __init__(self):
#        self.name = 'Ray'
#        self.bod = '36.66.66'
#        self.mobile = '99999999'
#        self.city = 'Maldives'
#        Human.count += 1
#    #def set_info(self):
#    #    self.name = input('write your name')
#    #    self.bod = input('write your bod')
#    #    self.mobile = input('write your mobile')
#    #    self.city = input('write your city')
#
#    def get_info(self):
#        print(f'name: {self.name}\nbirthday: {self.bod}\nphone number: {self.mobile}\ncity: {self.city}', sep = '\n')
#
#    def update_info(self):
#        change = input('1-change name\n2-change birthday\n3-change phone number\n4-change city')
#        if change == '1':
#            self.name = input('write your new name ')
#        elif change == '2':
#            self.bod = input('write your new bod ')
#        elif change == '3':
#            self.mobile = input('write your new mobile ')
#        elif change == '4':
#            self.city = input('write your new city ')
#        else:
#            print('there isnt that comand')
#
#obj1 = Human()
#obj2 = Human()
#Human.get_count()
#obj3 = Human()
#Human.get_count()




#class Figure:
#    count = 0
#    def init(self, name, *l): # (a = None, b = None, c = None, d = None)
#        self.name = name.lower()
#        self.lenght = l
#
#    def s(self):
#        if len(self.lenght) == 3:
#            p = round(sum(self.lenght) / 2, 2)
#            a = self.lenght[0]
#            b = self.lenght[1]
#            c = self.lenght[2]
#            self.square = (p * round(p - a,2) * round(p - b,2) * round(p - c,2)) ** 0.5
#            Figure.count += 1
#        elif len(self.lenght) == 4:
#            a = list(set(self.lenght))[0]
#            b = list(set(self.lenght))[1]
#            self.square = a * b
#        else:
#            print('Некорректный ввод')
#
#
#figure1 = Figure(25, 25, 49)
#figure2 = Figure(3, 3, 5, 5)
#figure1.s()
#figure2.s()
#print(figure1.square, figure2.square)



#class MathClass:
#    @staticmethod
#    def max(a, b, c, d):
#        print(max(a, b, c, d))
#
#    @staticmethod
#    def min(a, b, c, d):
#        print(min(a, b, c, d))
#
#    @staticmethod
#    def sum(a, b, c, d):
#        print(sum([a, b, c, d])/4)
#
#    @staticmethod
#...



#class Human:
#    def __init__(self, name, last_name, age):
#        self.name = name
#        self.last_name = last_name
#        self.age = age
#
#    def work(self):
#        print('doing work')
#    
#class Builder(Human):
#    def __init__(self, name, last_name, age, company):
#        super().__init__(name, last_name, age)
#        self.company = company
#
#    def process(self):
#        print('building')
#
#class Sailor(Human):
#    def __init__(self, name, last_name, age, ship):
#        super().__init__(name, last_name, age)
#        self.ship = ship
#    def process(self):
#        print('floating on the water')
#class Pilot(Human):
#    def __init__(self, name, last_name, age, plane):
#        super().__init__(name, last_name, age)
#        self.plane = plane
#    def process(self):
#        print('skying in the sky')
#builder = Builder('Ivan', 'Kaspersky', 29, 'krililu')
#sailor = Sailor('Rina', 'Ravy', 30, 'titanik')
#pilot = Pilot('Sasha', 'Arabovna', 37, 'Arabic Airline')
#print(builder.company)
#builder.process()
#sailor.process()
#pilot.process()
        


#class Passport:
#    def __init__(self, name, last_name, bod, country, number):
#        self.name = name
#        self.ln = last_name
#        self.bod = bod
#        self.country = country
#        self.number = number
#
#class ForeignPassport(Passport):
#    def __init__(self, name, last_name, bod, country, number):
#        super().__init__(name, last_name, bod, country, number)
#....
        


# атрибуты: название, тип, наличие шерсти, среда обитания.
# методы: голос, способ питания.
class Animal:
    def __init__(self, name, type, wool, habitat):
        self.name = name
        self.type = type
        self.wool = wool
        self.habitat = habitat

class Rabbit(Animal):
    def __init__(self, name, type, wool, habitat):
        super().__init__(name, type, wool, habitat)
        
    def voice(self):
        print('frfrfrfrforreallbrrr--o')

    def feeding_method(self):
        print('harbivore')
    
        