#Создайте класс Date, который будет содержать информацию о дате (день, месяц, год). С помощью механизма
#перегрузки операторов, определите операцию разности
#двух дат (результат в виде количества дней между датами), а также операцию увеличения даты на определенное
#количество дней.

#20-03-2025

class Date:
    calendary = {
        '1': 31,
        '2': 28,
        '3': 30,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31,

    }
    def __init__(self, date):
        self.day, self.month, self.year = map(int,date.split('-'))
        self.bc = Date.bc(self.day, self.month, self.year)

    def get_date(self):
        return f'day: {self.day}, month: {self.month}, year: {self.year}'
    
    @staticmethod
    def bc(day, month, year):
        d = day
        dom = 0
        doy = 0
        while (month - 1) != 0:
            dom += Date.calendary[str(month-1)]
            month -= 1
        doy = year * 365 + len([x for x in range(1, year) if x%4==0 and(x%400==0 or x%100 !=0)])
        return d + dom + doy
    
    def __sub__(self, o):
        return f'{abs(self.bc - o.bc)} days'
    
    def __add__(self, value):
        while value != 0:
            if value > 365:
                self.year += 1
                value-=365
            elif value + self.day > Date.calendary[str(self.month)]:
                value = value + self.day - Date.calendary[str(self.month)]
                self.day = 0
                self.month += 1
            else:
                self.day = value
                value = 0
    
now = Date('10-02-2025')
now+380 
print(now.get_date())
#o = Date('20-11-2013')
#print(now.bc, o.bc)
#print(o - now)
##print(([x for x in range(1, 2025) if x%4==0 and(x%400==0 or x%100 !=0)]))
