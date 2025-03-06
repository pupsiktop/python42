#пример "простого" класса
#class MyFirstClass:
#    pass
#my_first_object = MyFirstClass()
#print(my_first_object)
#print(x for x in range(10))

#class MyClass:
#    parent = 'MyClass'
#    '''это созданный мною класс'''
#    def __init__(self):
#        self.creator = 'Joe'
#    #creator = 'Joe'
#obj = MyClass()
#print(obj.__dict__, obj.creator)
#obj.date = '06-03-2025'
#print(obj.__dict__)
#obj2 = MyClass()
#obj2.date = '24.03.2025'
#print(obj.parent, print(obj2.parent))

#class Human:
#    def __init__(self):
#        self.name = 'Ray'
#        self.bod = '36.66.66'
#        self.mobile = '99999999'
#        self.city = 'Maldives'
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
#user1 = Human()
#print(user1.__dict__)
##user1.set_info()
#user1.update_info()
#user1.get_info()


#class City:
#    def __init__(self):
#        self.city = None
#        self.country = None
#        self.residents = None
#        self.phonecode = None
#    def city_info(self):
#        self.city = int(input('write your city'))
#    def country_info(self):
#        self.country= int(input('write your country'))
#    def resident_info(self):
#        self.residents = int(input('write your resident'))
#    def phonecode_info(self):
#        self.phonecode = int(input('write your phone code'))
#    def get_info(self):
#        print(f'city: {self.city}\ncountry: {self.country}\nresident: {self.residents}\nphone code: {self.phonecode}', sep = '\n')
#    def update_info(self):
#        change = input('1-change city\n2-change country\n3-change resident\n4-change phone code')
#        if change == '1':
#            self.city = input('write your new city ')
#        elif change == '2':
#            self.country = input('write your new country ')
#        elif change == '3':
#            self.residents = input('write your new residents ')
#        elif change == '4':
#            self.phonecode = input('write your new phone code ')
#
#u1 = City()
##print(u1.city)
##print(u1.country)
##print(u1.residents)
##print(u1.phonecode)
#u1.city_info()
#u1.country_info()
#u1.update_info()
#u1.get_info()


class Car:
    def __init__(self,price,color):
        self.tone = color
        self.sale = price
car = Car(100_000, 'red')
print(car.__dict__)

