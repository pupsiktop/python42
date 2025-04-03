#двухсвязный список

#Задание 2
#Пользователь вводит с клавиатуры набор строк. Полученные строки необходимо сохранить в двусвязный
#список. После чего нужно показать меню, в котором
#предложить пользователю набор пунктов:
#1. Добавить элемент в список
#2. Удалить элемент из списка
#1
#3. Показать содержимое списка
#4. Проверить есть ли значение в списке
#5. Заменить значение в списке
#В зависимости от выбора пользователя выполняется
#действие, после чего меню отображается снова.

class Node:
    def __init__(self, value, nextnode = None, prevnode = None):
        self.value = value
        self.nextnode = nextnode
        self.prevnode = prevnode


class DoubleLinkList:
    head = None
    tail = None
    length = 0
    #methods
    def myappend(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            #currentnode = self.head
            #while currentnode.nextnode != None:
            #    currentnode = currentnode.nextnode
            #currentnode.nextnode = Node(value, prevnode = currentnode)
            #self.tail = currentnode.nextnode
            currentnode = self.tail
            currentnode.nextnode = Node(value, prevnode = currentnode)
            self.tail = currentnode.nextnode
        self.length += 1

    def __str__(self):
        line = '<<'
        currentnode = self.head
        while currentnode.nextnode != None:
            line += f'{currentnode.value}, '
            currentnode = currentnode.nextnode 
        line += f'{currentnode.value}>>'
        return line
    
    def get_value(self, value_fs):
        currentnode = self.head
        while currentnode.nextnode != None:
            if  currentnode.value == value_fs:
                return True
            currentnode = currentnode.nextnode
        if currentnode.value == value_fs:
            return True
        else:
            return False
        
    def del_value(self, vfd):
        if self.head.value == vfd:
            nfd = self.head
            self.head = self.head.nextnode
            self.head.prevnode = None
            del nfd
        elif self.tail.value == vfd:
            nfd = self.tail
            self.tail = self.tail.prevnode
            self.tail.nextnode = None
            del nfd

        else:
            currentnode = self.head
            while currentnode.nextnode != None:
                if  currentnode.value == vfd:
                    nfd = currentnode
                    currentnode.prevnode.nextnode = currentnode.nextnode
                    currentnode.nextnode.prevnode = currentnode.prevnode
                currentnode = self.head
            while currentnode.nextnode != None:
                if  currentnode.value == vfd:
                    nfd = currentnode
        del nfd
        self.length -= 1
                
    def update_value(self, ov, vfd):
        currentnode = self.head
        while currentnode.nextnode != None:
            if  currentnode.value == ov:
                currentnode.value = vfd
            currentnode = currentnode.nextnode
        if currentnode.value == ov:
            currentnode.value == vfd
            
            
    

#doublelinklist_ = DoubleLinkList()
#doublelinklist_.myappend(52)
#doublelinklist_.myappend(25)
#doublelinklist_.myappend(54)
#doublelinklist_.update_value(25, 203)
#print(doublelinklist_)




#Задание 3
#Реализуйте класс стека для работы с целыми значениями (стек целых).
#Стек должен иметь фиксированный размер.
#Реализуйте набор операций для работы со стеком:
#■ помещение целого значения в стек;
#■ выталкивание целого значения из стека;
#■ подсчет количества целых в стеке;
#■ проверку пустой ли стек;
#■ проверку полный ли стек;
#■ очистку стека;
#■ получение значения без выталкивания верхнего целого в стеке.
#При старте приложения нужно отобразить меню с
#помощью, которого пользователь может выбрать необходимую операцию

class Stack:
    head = None
    tail = None
    length = 0
    max_length = 5

    def stack_append(self, value):
        if self.length < self.max_length:
            if self.head == None:
                self.head = Node(value)
                self.tail = self.head
            else:
                currentnode = self.tail
                currentnode.nextnode = Node(value, prevnode = currentnode)
                self.tail = currentnode.nextnode
            self.length += 1
        else:
            print('stack is full')

    def stack_pop(self):
        nfd = self.tail
        self.tail = self.tail.prevnode
        self.tail.nextnode = None
        self.length -= 1
        del nfd
            
    def get_length(self):
        print(f'elements in stack: {self.length}')

    def check_empty(self):
        if self.head is None:
            print('stack is empty')
        else:
            print('stack isnt empty')

    def stack_clear(self):
        currentnode = self.head
        while currentnode.nextnode != None:
            nfd = currentnode
            currentnode = currentnode.nextnode
            del nfd
        del currentnode
        self.length = 0
        self.head = None
        self.tail = None

    def get_tail(self):
        print(f'the last element: {self.tail.value}')
        
            
my_stack = Stack()
#my_stack.check_empty()
#my_stack.stack_append(1)
#my_stack.stack_append(2)
#my_stack.stack_append(3)
#my_stack.stack_append(4)
#my_stack.stack_append(5)
#my_stack.check_empty()
#my_stack.stack_append(6)
#my_stack.stack_pop()
##my_stack.stack_clear()
#my_stack.get_tail()
#my_stack.get_length()
##print(my_stack.length, my_stack.tail.value)


array = input('Введите числа через пробел, максимальное количество 5')

array = array.split(' ')
for elem in array:
    my_stack.stack_append(elem)

while True:
    choice = input(f'1-добавить\n2-удалить\n3-вывод последнего\n4-проверка пустоты\n5-очистить\n0-выход')
    if choice == '1':
        value = input('Введите значение для добавления')
        my_stack.stack_append(value)
    elif choice == '2':
        my_stack.stack_pop()
    elif choice == '3':
        my_stack.get_tail()
    elif choice == '4':
        my_stack.check_empty()
    elif choice == '5':
        my_stack.stack_clear()
    elif choice == '0':
        break
print('Программа завершена')
