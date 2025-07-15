#a = int(input('введите первое число'))
#b = int(input('введите второе число'))
#c = int(input('введите третье число'))
#g = input('1-умножение, 2-сложение')
#if g == '1':
#    print(a*b*c)
#elif g == '2':
#    print(a+b+c)
#else:
#    print('неверное число')
    



#a = int(input('введите первое число'))
#b = int(input('введите второе число'))
#c = int(input('введите третье число'))
#g = input('1-max, 2-min, 3-среднее арифметическое')
#if g == '1':
#    print(max(a,b,c))
#elif g == '2':
#    print(min(a,b,c))
#elif g == '3':
#    print((a+b+c)/3)
#else:
#    print('некорректная информация')


a = float(input('введите колличество метров'))
g = input('1-мили, 2-дюймы, 3-ярды')
if g == '1':
    print(a/1609.34)
elif g == '2':
    print(a*39.37)
elif g == '3':
    print(a*1.09)
else:
    print('incorrect')