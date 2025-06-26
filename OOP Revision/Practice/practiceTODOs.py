# These were some ToDo tasks I was given to think about 


#TODO: final keyword in py

from typing import final

class Parent:
    @final                    
    def test(self):
        print("parent method")

# Static‑type checker ERROR: "Cannot override final attribute 'test'
class Child(Parent):
    def test(self):
        print("child method")

c = Child()       
c.test()          
print("\n")



#TODO ; how does overrding affect at memory levrl 

class Parent:
    def speak(self):
        print("Parent speaking")

class Child(Parent):
    def speak(self):
        print("Child speaking")

c = Child()
c.speak()

# These are two separate function objects, stored in two separate class dictionaries. So it doesn't replace, rather it adds.
print(Parent.__dict__)
print(Child.__dict__)

print("\n")



# TODO : Class as Public/ Private
# protected class
class _Animal:
    pass

# in theory, not accessible from outside
# from animals import _Animal works, but says "internal use only"
# Dev can still subclass, but _ tells them that this base class isn’t to be inherirted


# private class
class __Animal:
    pass
# In theory not accessible from outide. Name is mangled as _ModuleName__Animal

#another usecase
class Car:
    class __Engine:  
        def start(self): print("Engine started")

    def __init__(self):
        self.__engine = self.__Engine()

    def start(self):
        self.__engine.start()

car = Car()
car.start()
# car.__engine  #error



#TODO : what does memeory level super().init
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id=employee_id

    def get_details(self):
        print("My name is",self.name,"with id", self.employee_id)

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)     #TODO: whats mememory level happening here?
        self.department = department

manag= Manager("bob", "E-001", "Finance")
manag.get_details()

# First checks MRO, where is super linking to?
print(Manager.mro())
# In manag, A __dict__ is created to store attributes like name, employee_id, department
print(manag.__dict__)

print("\n")



#TODO: kya farq parey ga if we write super or not?
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,leght, width):
        # super().__init__()     #TODO: kya farq parey ga?
        self.length = leght
        self.width = width


class Shape:
    def __init__(self):
        self.color = "black"   # feature added later

class Rectangle(Shape):
    def __init__(self, length, width):
        # super().__init__()   # missing
        self.length = length
        self.width  = width

r = Rectangle(2, 3)
# print(r.color)


# Mutliple Inheritance problem
class Drawable:
    def __init__(self):
        super().__init__()
        self.visible = True

class Shape:
    def __init__(self):
        super().__init__()
        self.color = "black"

class Rectangle(Drawable, Shape):
    def __init__(self, length, width):
        # super().__init__()
        self.length = length
        self.width  = width


# TODO : What happens in memory in encapsulation??
class Person:
    def __init__(self, name, age):
        self.name = name         
        self._age = age            
        self.__secret = "hidden"   

p = Person("Mahad", 20)

#saves it all in memory in the form of dictionary
print(p.__dict__)


# TODO : FRIEDN CLASSES in py??
# not Directly, but through either setter/getters or composition
