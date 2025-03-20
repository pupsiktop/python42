#class FirstSuper:
#    def __init__(self, a):
#        self.a = a
#
#    def meth(self):
#        return f'FirstSuper'
#    
#class SecondSuper:
#    def __init__(self, b):
#        self.b = b
#
#    def meth(self):
#        return f'SecondSuper'
#    
#class Sub(SecondSuper, FirstSuper):
#    def __init__(self, a, c, b):
#        super().__init__(a)
#        FirstSuper.__init__(self,b)
#        self.c = c
#
#obj = Sub(1, 2, 3)
#print(obj.meth())
##print(obj.__dict__)
#print(Sub.mro())
##print(Sub.__mro__)
#print(obj.a)


#class Square:
#    def __init__(self, a):
#        self.a = a
#    def s_square(self):
#        return self.a ** 2
#class Circle:
#    def __init__(self, r):
#        self.r = r
#    def s_circle(self):
#        return self.r ** 2
#    
#class Squaroffarea(Square, Circle):
#    def __init__(self, a, r):
#        super().__init__(a)
#        Circle.__init__(self,r)
#    def check_area(self):
#        if self.a == 2 * self.r:
#            print('окружность вписана в квадрат')
#        else:
#            print('окружность не вписана в квадрат')
#
#figure = Squaroffarea(4, 2)
#figure.check_area()
#figure2 = Squaroffarea(324, 43)
#figure2.check_area()


class Wheels:
    def __init__(self, count, d):
        self.count = count
        self.d = d

class Engine:
    def __init__(self, power, type):
        self.power = power
        self.type = type

    def sound_engine(self):
        if self.type == 'electric':
            return f'shh-shh-shh'
        else:
            return f'JJJRRRH_JRSJD'
        
class Door:
    def __init__(self, count):
        self.count = count
    