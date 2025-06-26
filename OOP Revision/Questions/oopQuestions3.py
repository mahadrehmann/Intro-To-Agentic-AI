'''
Question 3.1: Create a base class Animal with an __init__ taking name and sound. Add a method make_sound() that prints the animal's name and sound. Create a subclass Dog that inherits from Animal. Create an instance of Dog and call make_sound(). 
'''
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print("I'm", self.name, "and my sound is", self.sound)
   
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

d1 = Dog("Lucy", "Woof")
d1.make_sound()
print("\n")


'''
Question 3.2: Define a base class Shape with a method area() that returns 0. Create two subclasses: Rectangle (with length and width) and Circle (with radius). Both subclasses should override the area() method to calculate their specific area. 
'''
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

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        # super().__init__()
        self.radius = radius

    def area(self):
        return 3.141 * self.radius ** 2
        
rec = Rectangle(4,2)
cir = Circle(3)

print("Rectangle's Area:",rec.area())
print("Circle's Area:",cir.area())
print("\n")


'''
Question 3.3: Design a base class Employee with __init__ taking name and employee_id. Add a method get_details(). Create a subclass Manager that inherits from Employee and adds an __init__ parameter for department. 
'''
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
print("\n")


'''
Question 3.4: From Q3.1, in the Dog subclass, override the make_sound() method so that instead of just printing "Woof!", it prints "{} says: Woof Woof!". Ensure the Animal's __init__ is still called correctly using super(). 
'''
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print("I'm", self.name, "and my sound is", self.sound)
   
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        super().make_sound()
        print("Woof Woof!")

d1 = Dog("Lucy", "Woof")
d1.make_sound()
print("\n")



'''
Question 3.5: Extend the Employee and Manager classes. Override the get_details() method in Manager to also include the department information, while still calling the Employee's get_details() using super(). 
'''
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id=employee_id

    def get_details(self):
        print("My name is",self.name,"with id", self.employee_id)

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def get_details(self):
        super().get_details()
        print("and my dept is", self.department)

manag= Manager("bob", "E-001", "Finance")
manag.get_details()
print("\n")



'''
Question 3.6: Create a base class Vehicle with __init__ taking make and model, and a method start_engine(). Create a subclass ElectricCar that inherits from Vehicle. Override start_engine() in ElectricCar to print "Starting electric motor silently." 
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Starting vehicle")

class ElectricCar(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def start_engine(self):
        print("Starting electric motor silently." )

ecar = ElectricCar("mercedes", "2005")
ecar.start_engine()
