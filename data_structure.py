###################### LIST #######################

lo = [1,2,3,'one','two','three',None,True,False]
for i in lo:
    if isinstance(i,int):
        print(i)

for i in lo:
    if isinstance(i,str):
        print(i) 

for i in lo:
    if isinstance(i,bool):
        print(i) 

for i in lo:
    if isinstance(i,float):
        print(i) 

for i in lo:
    if i is None:
        print(i)

# to delete all strings togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,str)]
print(lo)
# end        
# to delete all int togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,int)]
print(lo)
# end  
# to delete all booleans togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,bool)]
print(lo)
# end   
# to delete all float togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,float)]
print(lo)


# enumerate() method
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(index, value)

# end
                   
################################# END LIST ####################    

########################### DICTIONARY ################################

# two ways of creating dictionary using dict constructor
dict1 = dict(name='abu',age=12)
print(dict1)
dict2 = dict({'name':'abu','age':18})
print(dict2)
# end
######################### END DICTIONARY ########################  

############################# STACK ############################

# stack implementation using list
stack = []
# push can be done with append()
stack.append(1)
print(stack)
stack.append(10)
print(stack)
stack.append(100)
print(stack)
# pop can be done with pop
stack.pop()
print(stack)
# last value (top()) can be acced usig index
print(stack[-1])
# isEmpty() using leng()
if len(stack) == 0:
    print('stack is empty')



# problem
stack = []
def push():
    if len(stack) == n:
        print('stack is full')
    else:
        add = int(input('enter number:'))
        stack.append(add)
        print(stack)

def pop():
    if len(stack) == 0:
        print('stack is empty')
    else:
        stack.pop()
        print('result is :',stack)

n = int(input('enter limit:'))

while True:
    print('eneter your choise 1 for push 2 for pop 3 for quit')
    choice = int(input('enter choice:'))
    if choice == 1:
        push()
    elif choice == 2:   
        pop()
    elif choice == 3:
        break
    else:
        print('invalid result')

# stack implementation using deque class of collection moodule
import collections
stack = collections.deque()
print(len(stack))
stack.append(1)
print(stack)
stack.append(20)
stack.append(50)
stack.append(100)
print(stack)
stack.pop()
print(stack)
print(stack[-1])
if len(stack) == 0:
    print('stack is empty')
else:
    print('stack is not empty')

# stack implementation using LifoQueue class of queue moodule    
import queue
stack = queue.LifoQueue()
stack.put(1)
print(stack)
stack.put(20)
stack.put(30)
stack.put(40)
print(stack)
stack.put(68)
stack.get()
stack.get()
print(stack)


# reversing string using stack
def reversing_string_with_stack(string):
    stack = []

    for i in string:
        stack.append(i)

    reversed_string = ''
    while stack:
         reversed_string += stack.pop()    

    return reversed_string

lo =reversing_string_with_stack('hello world')
print(lo)


######################## END STACK ######################





##################################### LINKED LIST ########################################

#(1).singly linked list



                #------- traversing---------#
#creating nodes
# we can create individual nodes like this
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

# while creating a node intially its reference is given as null/none

#to connect individual nodes wee need a  another class 
class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'---->',end=" ")
                n = n.ref 

                #---------insertion---------#
        # add-begin        
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

        # add-end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print('node is added at the empty linked list')
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
             # in between nodes
        # add_after
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
              break
            n = n.ref

        if n is None:
            print('node is not present in LL')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node 

        # add before    
    def add_before(self,data,x):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return 
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print('node is not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('linked list is not empty')

               #---------Deletion---------#

    def delete_begin(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print('linked list is empty')
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None   

    # delete at any position you want
    def delete_by_value(self,x):
        if self.head is None:
            print('Linked list empty,cant delete')
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print('node is not present')
        else:
            n.ref = n.ref.ref


    
             



SLL1 = LinkedList()
SLL1.add_end(50)
SLL1.add_end(40)
SLL1.add_end(30)
SLL1.add_end(60)
SLL1.add_after(35,30)
SLL1.add_before(25,30)
SLL1.add_begin(20)
SLL1.add_begin(10)
SLL1.insert_empty(100)
SLL1.delete_begin()
SLL1.delete_end()
SLL1.delete_by_value(35)
SLL1.delete_by_value(50)
SLL1.delete_by_value(20)
SLL1.print_LL()

#(2). doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:
    def __init__(self):
        self.head = None
          
        #--------------- traversing-----------#

    # front-ward traversing
    def print_LL(self):
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'---->',end=" ")
                n = n.nref

    # back-ward traversing    
    def print_LL_reverse(self):
        print()
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,'------>',end =" ")
                n = n.pref
    
    # insertion when linked list is empty
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked List is not empty')
    
    # add begin
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    # add end
    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    
    # add after
    def add_after(self,data,x):
        print('hell')
        if self.head is None:
            print('linked list is empty')
        else:
            print('gooys')
            n = self.head
            while n is not None:
                print('enterd')
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('given node is not present in the list')
            else:
                print('chunk')
                new_node = Node(data)
                new_node.nref = n.nref
                n.nref = new_node
                if n.nref is not None:
                    n.nref.pref = new_node
                new_node.pref = n
    
    # add before
    def add_before(self,data,x):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            
            if n is None:
                print('given node is not present')
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    

    # delete begin
    def delete_begin(self):
        if self.head == None:
            print('Linked List is empty,cant delete')
            return
        if self.head.nref is None:
            self.head = None
            print('DLL is empty after deleting the node!')
        else:
            self.head = self.head.nref
            self.head.pref = None
    
    # delete end
    def delete_end(self):
        if self.head is None:
            print('Linked List is empty, cant delete')
            return
        if self.head.nref is None:
            self.head = None
            print('DLL is empty after deleteing node!')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None 

    # delete by value
    def delete_by_value(self,x):
        if self.head == None:
            print('Linked List is empty')
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
                print('item delted and List empty')
            else:
                print('given node not present in Linked List')
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break  
            n = n.nref
        if n.nref is not None:
            print('kery')
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            print('seen1')
            if n.data == x:
                print('seen 2')
                n.pref.nref = None
            else:
                print('node is not present in the Linked List')
                
        


DLL1 = doublyLL()
DLL1.insert_empty(5)
DLL1.add_end(10)
DLL1.add_begin(0)
DLL1.add_after(7,5)
DLL1.add_before(3,5)
DLL1.delete_by_value(100)
DLL1.print_LL()
DLL1.print_LL_reverse()


        
####################### END LINKED LIST ############################



######################### LINEAR SEARCH #########################

def linearSearch(l,key):
    for idx,x in enumerate(l):
        if key == x:
            print('item found at :',idx+1)
            break
    else:
        print('item not found in the given list')

linearSearch([3,45,67,90],67)


list1 = [1,22,32,43,5,67,89]
print('this is the list for you :',list1)
try:
  num = int(input('enter the number you want to find:'))
  for idx,x in enumerate(list1):
    if num == x:
        print('item found at :',idx + 1)
        break

  else:
    print('item not found')
except ValueError as e:
    print(e)

########################## END ####################################

########################## BINARY SEARCH #########################
def binarySearch(num_list,key):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end)//2
        if num_list[mid] == key:
            return mid + 1
        elif num_list[mid] < key:
            start = mid + 1
        elif num_list[mid] > key:
            end = mid -1
    return -1
pos = binarySearch([1,2,3,4,5],5)
if pos != -1:
    print('element found at :',pos)
else:
    print('element not found') 

############################# END BINARY SEARCH ############################



############################### STRING ################################

a = "Hello, World!"

# accessing and slicing
print(a[7])
print(a[2:5])
print(a[:5])
print(a[-11:-1])

# accessing with for loop
for i in a:
    print(i)

# len() = finding length of string
print(len(a))

# present or not
# in\not in
txt = "The best things in life are free!"
print('free' in txt)

if 'free' in txt:
    print('yes, \"free\" is present ')

print( 'boss' not in txt )

if 'boss' not in txt:
    print('no, \'boss\' not present')
else:
    print('yes, \'boss\' exists')

# upper() = making string in to uppercase
print(txt.upper())

# lower() = making string in to lowercase
print(txt.lower())

# stripe() = removing white space
aj = ' akmal ali '
print(aj.strip())

# replace() = replace a character with other 
print(aj.replace('k','j'))

# split() = splitting a string in to list of substring
print(aj.split(' '))

b = 'Hellow'
c = 'World'
print(b+' '+c)

# format()
aj_name = 'ajmal {}'
age = 22
print(aj_name.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {1} pieces of item {0} for {2} dollars."
print(myorder.format(quantity,itemno,price))

# escape character
print("i am \'mohammed\' sabeel")
print("i am 'mohammed' sabeel")


# capitalize() = convert the first character in to capital
mun = 'mUNAVAR'
print(mun.capitalize())

# casefold() = convert the strings in to lower case
print(mun.casefold())

# center() = used to center string by taking space specified inside center
chunk = mun.center(20)
print(len(chunk),chunk)

# count() = it return the number of specified strings
print(mun.count('m'))

# endswith() = it return the True if the string ends with specified character in the endswith()
print(mun.endswith('R'))

# expandtabs() = to increase tab size
print(mun.expandtabs())

# find() = find the starting index of specified item in the string,return -1 if the value not found
print(mun.find('NAVAR'))

# index() = find the starting index of specified item in the string ,it will raise an exception if value not found
print(mun.index('AVAR'))



################################# END STRING ###########################