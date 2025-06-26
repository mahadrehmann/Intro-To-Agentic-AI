#------------------------------------------------------------------------
#                           INHERITANCE 
#------------------------------------------------------------------------

# sub-classes

#example 1:
class BaseClass:
    def __init__(self, value):
        self.value=value

    @staticmethod
    def test(x):
        print("baseclass", x)    

class SubClass(BaseClass):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def test(x):
        BaseClass.test(x+1)
        print("dervied class", x)

sub = SubClass(12)
SubClass.test(12)
print("--------------------------------------------")


#example 2:
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_num):
        super().__init__(name)
        self.roll_num = roll_num

    def display_info(self):
        print(self.name, self.roll_num)
        print("--------------------------------------------")

s1 = Student("Mahad", "22i-0792")
s1.display_info() 


# Fun Example 3:
# Class attributes are shared unless explicitly overridden
class A:
    shared = []

class B(A):
    shared=[]
    pass

# TODO : how to overcome overriding

A.shared.append("A")
B.shared.append("B")

print(A.shared)  
print(B.shared) 
print("--------------------------------------------")


# example 4
class Base:
    category = "Base"

    @classmethod
    def whoami(cls):
        print(f"I am a {cls.category}")

    @staticmethod
    def whoami_static():
        print("I am a Base")

class Sub(Base):
    category = "Sub"

Sub.whoami()        
Sub.whoami_static() 
print("--------------------------------------------")


# example 5:
class Parent:
    @staticmethod
    def identify():
        print("Parent static")

class Child(Parent):
    @classmethod
    def identify(cls):
        Parent.identify()
        print(f"{cls.__name__} class method")   #TODO

Child.identify()  # Output? => "Child class method"


#example 6:
class Vehicle:
    def __init__(self, engine_num, year):
        self.engine_num = engine_num
        self.year = year

class Car(Vehicle):
    def __init__(self, engine_num, year,name):
        super().__init__(engine_num, year)
        self.name = name

    def display_info(self):
        print(self.engine_num, self.year, self.name)
        print("--------------------------------------------")

bmw = Car("SD-10w", "2010", "BMW M4")
bmw.display_info()






# method overiding

#example 1:
class Parent: 
   def test(self):
      print ('parent method')

class Child(Parent): 
   def test(self):
      print ('Calling child method')   #TODO: final keyword??

c = Child() 
c.test()
print("--------------------------------------------")


#example 2:
class Animal:
    def speak(self):
        print("i am an animal")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")


x = 5
y = 4
                    #TODO ; how does overrding affect atn memory levrl 
x=y

print("X IS", x)

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()  
cat.speak()
print("--------------------------------------------")


# example 3 : diamond probelm
class A:
    def who_am_i(self):
        return "I am A"
class C(A):
    def who_am_i(self):
        return "I am C" 
class B(A):
    def who_am_i(self):
        return "I am B"

class D(C, B):
    pass

d = D()
print(d.who_am_i())  
print(D.mro())   #Method resolution order  
print("--------------------------------------------")


#example 4:
class Parent1(): 
	def show(self): 
		print("Inside Parent1") 
	
class Parent2(): 
    @staticmethod
    def show(): 
        print("Inside Parent2") 
		
class Child(Parent2, Parent1): 
	pass
		
obj = Child() 

obj.show() 
# obj.display()
print("--------------------------------------------")


# example 5:
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        parent_message = Parent.greet(self)
        return f"{parent_message} and Hello from Child"

c = Child()
print(c.greet()) 
print("--------------------------------------------")

