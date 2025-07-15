#1
#def text():
#    print('''“Don't compare yourself with anyone in this world…
#        if you do so, you are insulting yourself.”
#                                                Bill Gates''')
#text()



#2
#def digit(start, end):
#    for i in range(start, end):
#        if i%2==0:
#            print(i)
#digit(3,8)


#3
#def square(lengh, symbol, logic):
#    for i in range(lengh):
#        if logic or i == 0 or i == lengh - 1:
#            print(lengh*symbol)
#        else:
#            print(symbol, end = ' ')
#            print(' '*(lengh-4), end = ' ')
#            print(symbol)
#square(20, '*', False)


#4
#def digit(a, b, c, d, e):
#    min = a
#    if b<min:
#        min = b
#    if c<min:
#        min = c
#    if d<min:
#        min = d
#    if e<min:
#        min = e
#    return min
#print(digit(5,1,8,0,2))



#5
#def digit(start, end):
#    if start>end:
#        start, end = end, start
#    result = 1
#    for i in range(start, end):
#        result *= i
#    return result
#print(digit(5, 1))



#6
#def digit(a):
#    return (len(str(abs(a))))
#print(digit(25647))


#7
def digit(a):
    #return (len(str(a)))
    num = str(a)
    return num == num[::-1]
print(digit(123325))