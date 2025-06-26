#------------------------------------------------------------------------
#                           POLYMORPHISM 
#------------------------------------------------------------------------

# --------------Overloading----------------

# example
def product(a, b):
    p = a * b
    print(p)

product(4, 5)

def product(a, b, c):   #only this is considered
    p = a * b *c
    print(p,"\n")

product(4, 5, 6)

#TODO why this, cuz its an intrepreted language

# example
def add(datatype, *args):  #TODO list or tuple, its a tuple
    if datatype == "int":
        res = 0
    elif datatype == "str":
        res = ''
    
    for item in args:
        res += item

    print(res)


def add(datatype, *args):
    print("MEEE")
    return datatype

add("int", 5, 6, 7, 8)
add("int", 5, 6)
add("str", "yo", "Mahada")
print("\n")


# example:
def check_function(a, b=0):
    if b == 0: 
        print("a is:", a)
    else:
        print("a is", a, "and b is",b, "\n")

check_function(3)
check_function(3,8)
             
# Operator Overloading in Python

# magic method __add__ is called when call + for objects

class Test:
    def __init__(self, val):
        self.val = val

    def __add__(self, v1):
        return self.val - v1.val

obj1 = Test(10)
obj2 = Test(20)
obj3 = Test(30)
print("Sum is",obj1+obj2, "\n")
print("Sum is",Test.__add__(obj2,obj3), "\n")

#TODO: Why have a magic function if we cant overload it, why cant i make it ternary 

# example:
class Checker:
    def __init__(self, var):
        self.var = var

    def __lt__(self, obj):
        if self.var > obj.var:
            print("First Obj is larger\n")
        elif self.var < obj.var:        
            print("Second Obj is larger\n")
        else:
            print("Both are Equal\n")

c1 = Checker(12)
c2 = Checker(15)

c1<c2
c1.__lt__(c2)


'''
Here are all the operators
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)

<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)
'''


#---------------Overriding----------------------

# Inheritance Class Polymorphism

#example
class Animal:
    def sound(self):
        return "animal animal"

class Dog(Animal):
    def no(self):
        return "NO"
    def sound(self):
        return "Bark"

class Dog(Animal):  #TODO : types of error. What type? This is a logical error
    def sound(self):
        return "Meow"

animals = [Dog(), Dog(), Animal()]
for animal in animals:
    print(animal.sound()) #dynamic

print(Dog().no())
print("\n")    




# example:
class Parent1(): 
	def show(self): 
		print("Inside Parent1") 
	
class Parent2(): 
    def show(self): 
        print("Inside Parent2") 
		
class Child(Parent2, Parent1): 
	pass
		
obj = Child() 

obj.show() 


# example:
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        parent_message = Parent.greet(self)
        return f"{parent_message} and Hello from Child"

c = Child()
print(c.greet()) 


