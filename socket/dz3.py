#dz n1

#g = input('enter your string')
#if g == g[::-1]:
#    print('yes')
#else:
#    print('no')


#dz n3

g = input('enter your string')
c = 0
g = list(g)
for i in g:
    if i == '.' or i =='!' or i == '?':
        c+=1
print(c)
