#паттерны проектирования:
#1.пораждающий: (Singleton, Factory, Abstract Factory)
#2.структурный:(Facade)
#3.поведенческий: (iterator)


#Создайте классическую реализацию паттерна Singleton.
#Протестируйте работу созданного класса.
#__init__ - команда определения экземпляра __new__ - команда конструктор

#class Singleton:
#    _instance = None
#    def __new__(cls):
#        if cls._instance is None: #если экземпляра-одиночки нет
#            cls._instance = super(Singleton, cls).__new__(cls) #создать экз. одиночку
#        else:
#            print('экземпляр одиночка уже создан')
#        return cls._instance
#    
#class NotSingleton:
#    pass
#    
#refery = Singleton()
#print(refery)
#refery2 = Singleton()
#print(refery2)
#print(refery is refery2)
#
#obj1 = NotSingleton()
#obj2 = NotSingleton()
#print(obj1 is obj2, obj1, obj2)
#
#
##pattern factory
#
#class Fabric:
#    def __init__(self, name, age, professional):
#        self.name = name
#        self.age = age
#        self.professional = professional
#
#    def get_info(self):
#        return f'name: {self.name}, professional {self.professional}'
#
#class Driver(Fabric):
#    def __init__(self, name, age, professional):
#        super().__init__(name, age, professional)
#
#class Pilot(Fabric):
#    def __init__(self, name, age, professional):
#        super().__init__(name, age, professional)
#
#user1 = Driver('Dominic Toretto', 45, 'Speedster')
#user2 = Pilot('Alasheev', 76, 'the test pilot')
#print(user1, user2)
#print(issubclass(Driver, Fabric), issubclass(Pilot, Fabric))



#Создайте реализацию паттерна Abstract Factory. Протестируйте работу созданного класса.

#from abc import ABC, abstractmethod
#class AbstractFactory(ABC):
#    @abstractmethod
#    def create_factory(name):
#        if name == 'Lada':
#            factory = LadaFactory()
#            return factory
#        elif name == 'Sukhoi':
#            factory = SukhoiFactory()
#            return factory
#
#class LadaFactory(AbstractFactory):
#    def __init__(self):
#        self.name = 'Ladas company Factory'
#
#class SukhoiFactory(AbstractFactory):
#    def __init__(self):
#        self.name = 'Sukhois company Factory'
#    def create_factory(self, name):
#        return super().create_factory(name)
# 
#f = SukhoiFactory()
#factory_from_irkutsk = f.create_factory('Sukhoi')
#print(factory_from_irkutsk)



#Пользователь вводит с клавиатурынабор чисел и путь
#кфайлу для сохранения полученных данных. Необходимо:
#■ Сохранить все полученные числа.
#■ Найти максимум, минимум. Эти значения сохранить
#в том же файле.
#■ Отобразить числа.
#■ Отобразить максимум и минимум.
#■ Создать класс для логгирования операций. При создании объекта класса нужно уточнить куда производится
#логгирование: экран или файл. В программе можно
#создать только один объект класса. Все действия
#объекта этого класса.

class Logger:
    _instance = None
    loggerlocation = None
    def __new__(cls):
        if cls._instance is None:
            cls.loggerlocation = input('where to put logger record:\n1-in file\n2-in terminal')
            cls._instance = super(Logger, cls).__new__(cls)
        else:
            print('Logger is alr exist')
        return cls._instance

    def logging(self, message):
        if self.loggerlocation == '2':
            print(message)
        else:
            with open('Logging.txt', 'a', encoding='utf-8')as file:
                file.write(message + '\n')

    def log_input_digit(self):
        self.logging('number have been added')

    def log_extrem_digit(self, maxx, minx):
        self.logging(f'the search for the max and min. Max {maxx}, Min {minx}')

    def log_render(self, listdigit):
        self.logging(f'massivs render{listdigit}, max el {max(listdigit)} and min el {min(listdigit)}')

class Digits:
    def __init__(self, path='Digit.txt', logger=None):
        array = input('enter the numbers with the space')
        self.path = path
        self.logger = logger
        self.listdigit = list(map(int, array.split(' ')))
        with open(path, 'a', encoding='utf-8')as file:
            for digit in self.listdigit:
                file.write(str(digit)+'\n')
        logger.log_input_digit()

    def get_extrem(self):
        maxx = max(self.listdigit)
        minx = min(self.listdigit)
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(f'max el {maxx}, min el {minx}')
        self.logger.log_extrem_digit(maxx, minx)

    def render(self):
        print(f'массив чисел: {self.listdigit}.\nMax: {max(self.listdigit)}, min: {min(self.listdigit)}')
        self.logger.log_render(self.listdigit)


logger = Logger()
print(logger)
array = Digits(logger=logger)
array.get_extrem()
array.render()