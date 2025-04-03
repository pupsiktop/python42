##декораторы
#def f2(func):
#    print('декорируемое действие')
#    func()
#    print('второе декорируемое действие')
#
#@f2
#def f1():
#    print('какое-то важное действие')
#
#@f2
#def f3():
#    print('какое-либо маловажное действие')
#
##var = f2(f1)
#var2 = f1
#var3 = f3
#print(var2, var3)

#1

#from functools import lru_cache
#
#@lru_cache
#def f(n):
#    if n<=1: return 1
#    elif n > 1 and n % 2 == 0: return f(n - 1) *n + f(n - 2) * n
#    else: return f(n - 1) *n + f(n - 2) * n
#print(f(300))

#2

#from datetime import datetime
#
#def render():
#    print('*'*10)
#    timer() # создать функцию
#    print('*'*10)
#
#def timer():
#    time = datetime.now()
#    time = time.strftime('%H:%M')
#    print(time)
#
#def weekday()
#    today = datetime.today().weekday()
#    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
#    return week[today]
#
#render()

#3

#from datetime import datetime
#
#def render(func):
#    print('*'*10)
#    func() # создать функцию
#    print('*'*10)
#
#@render
#def timer():
#    time = datetime.now()
#    time = time.strftime('%H:%M')
#    print(time)
#
#render 

#4

margo_recipe = ('margarita', 'tomato', 'cheese', 'salad', 'onion')
cheese_recipe = ('for-cheese', 'cheese type 1','cheese type 2', 'cheese type 3', 'cheese type 4')
hawaii_recipe = ('hawaii', 'pineapple', 'salad', 'cheese', 'tomato')
caprichosa = ('caprichosa', 'tomato', 'mocarella', 'artichoke', 'olived', 'mushroom' ,'ham')
recipe_list = (None, margo_recipe, cheese_recipe, hawaii_recipe, caprichosa)

margo_price = 880
cheese_price = 750
hawaii_price = 990
caprichosa_price = 940
price_list = (None, margo_price, cheese_price, hawaii_price, caprichosa_price)
ticket = []


def menu():
    global ticket
    print('welcome to the pizzery!')
    busket = 0
    pizza_name = []
    while True:
        pizza = int(input('menu:\n1-margarita\n2-for-cheese\n3-hawaii\n4-caprichosa\n0-exit\n'))
        if pizza == 0: break
        ticket += [recipe_list[pizza]]
        pizza_name += [recipe_list[pizza][0]]
        busket += price_list[pizza]
        print(f'your order {pizza_name}, on summ {busket}')
    print(f'your order {pizza_name}, on summ {busket}')
    craft
def craft(func):
    print('preheat the oven')
    func(ticket)
    print('get the ready pizza!')

@craft
def recipe(ticket):
    print('prepare ingridients:')
    for pizz in ticket:
        for i in pizz[1:]:
            print(i)
    print('put ingridients on the pizza base')
    print('add sauce')
    print('put in oven on 40 min')
menu()