'''
Question 2.1: Building on the Car class from Q1.3, add an instance attribute current_speed initialized to 0. Add two instance methods: accelerate(speed_increase) that increases current_speed and brake(speed_decrease) that decreases current_speed (ensure speed doesn't go below 0). Demonstrate accelerating and braking a car object. 
'''

class Car:
    def __init__(self, make, model, year, current_speed=0 ):
        self.make= make
        self.model = model
        self.year = year
        self.current_speed=current_speed

    def display_info(self):
        print("Make:", self.make, "Model:", self.model, "Year:", self.year)

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        return self.current_speed

    def brake(self, speed_decrease):
        if (self.current_speed - speed_decrease>=0):
            self.current_speed -= speed_decrease

            return self.current_speed

c1 = Car("Lamborghini", "Aventedor", 2015 )
c2 = Car("BMW", "m3", 2010 )
c3 = Car("Toyota", "Vitz", 2004 )

# for car in (c1,c2,c3):
#     car.display_info()

print(c1.accelerate(50))
print(c1.brake(10))
print("----------------------------------------------\n")



'''
Question 2.2: Create a Student class. Its __init__ method should take name and student_id. Add an instance method enroll_course(course_name) which adds the course_name to a list of courses associated with the student. Add another method get_courses() that returns the list of enrolled courses. 
'''

class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def get_courses(self):
        return list(self.courses)


s1 = Student("Mahad", "22i-0792")
s1.enroll_course("Ai")
s1.enroll_course("SE")

'''
Question 2.3: Design a BankAccount class. Its __init__ should take account_number and initial_balance. Include instance methods deposit(amount) and withdraw
(amount). Ensure withdrawals cannot go below zero balance. 
'''

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number 
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount
        return self.initial_balance

    def withdraw(self, amount):
        if (self.initial_balance - amount>=0):
            self.initial_balance -= amount

            return self.initial_balance

c1 = BankAccount("C-100", 1000 )

print(c1.deposit(500))
print(c1.withdraw(100))        
print("----------------------------------------------\n")

'''
Question 2.4: Enhance the Dog class. Add a class attribute number_of_dogs initialized to 0. Modify the __init__ method to increment number_of_dogs every time a new Dog object is created. Add a class method get_total_dogs() that returns number_of_dogs. Create several Dog objects and then print the total number of dogs using the class method. 
'''

class Dog:
    number_of_dogs=0

    def __init__(self, name, breed):
        self.name = name
        self.breed= breed
        Dog.number_of_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        return cls.number_of_dogs
    
d1 = Dog("Buddy", "Golden Retriever")
d2 = Dog("Lucy", "Labrador")
d2 = Dog("Maddy", "Husky")
print("total dogs:",Dog.get_total_dogs())
print("----------------------------------------------\n")


'''
Question 2.5: Create a Product class. It should have a class attribute discount_rate initialized to 0.10 (10%). The __init__ method should take name and price. Add an instance method get_discounted_price() that calculates the price after applying the discount_rate. Add a class method set_discount_rate(new_rate) that allows modifying the discount_rate. 
'''
class Product:
    discount_rate = 0.10
    def __init__(self,name,price):
        self.name = name
        self.price=price

    def get_discounted_price(self):
        discount = self.price*Product.discount_rate
        return (self.price - discount)
    
    @classmethod
    def set_discount_rate(cls, new_rate):
        cls.discount_rate = new_rate

p1 = Product("Pencil", 20)
print("Discounted Price is:",p1.get_discounted_price())
     
Product.set_discount_rate(0.20)
print("New Discounted Price is:",p1.get_discounted_price())
print("----------------------------------------------\n")


'''
Question 2.6: Design a Circle class. Add a class attribute PI set to 3.14159. The __init__ should take radius. Add an instance method calculate_area(). Create a class method set_pi_precision(new_pi) that allows changing the value of PI. 
'''

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.PI * self.radius * self.radius
     
    @classmethod
    def set_pi_precision(cls, new_pi):
        cls.PI = new_pi

circ = Circle(4)
print("Area is:",circ.calculate_area())
Circle.set_pi_precision(3)
print("New Area is:",circ.calculate_area())
print("----------------------------------------------\n")


'''
Question 2.7: In the Car class, add a static method display_general_car_safety_tips(). This method should print some generic safety advice (e.g., "Always wear seatbelts."). It should not access any instance or class attributes. 
'''

class Car:
    def __init__(self, make, model, year, current_speed=0 ):
        self.make= make
        self.model = model
        self.year = year
        self.current_speed=current_speed

    def display_info(self):
        print("Make:", self.make, "Model:", self.model, "Year:", self.year)

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        return self.current_speed

    def brake(self, speed_decrease):
        if (self.current_speed - speed_decrease>=0):
            self.current_speed -= speed_decrease

            return self.current_speed
    
    @staticmethod
    def display_general_car_safety_tips():
        print("Better Late than Never")

bmw = Car("BMW", "m3", 2010 )
Car.display_general_car_safety_tips()
print("----------------------------------------------\n")


'''
Question 2.8: Create a MathUtility class. Add a static method add(a, b) that returns the sum of a and b. Add another static method multiply(a, b). These methods should not depend on the state of any MathUtility object. 
'''
class MathUtility:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
print("Addition is:",MathUtility.add(10,20))
print("Multiplication is:",MathUtility.multiply(10,20))
print("----------------------------------------------\n")


'''
Question 2.9: For the Student class, add a static method generate_student_id(). This method should generate a random 6-digit student ID (e.g., using random module). It should not take self or cls as arguments and should not rely on any instance or class data. 
'''

import random

class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def get_courses(self):
        return list(self.courses)
    
    @staticmethod    #TODOO Try this.
    @classmethod
    def generate_student_id(cls):
        print(cls.courses)
        return random.randint(100000, 999999) #any six digit number


s1 = Student("mahad", "22i-0792")
print("random roll number is:", Student.generate_student_id())
