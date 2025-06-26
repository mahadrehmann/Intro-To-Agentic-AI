# Method Overriding (as a form of Polymorphism) 
'''
Question 5.1: (Revisit) Create a base class Shape with a method draw(). Create subclasses Circle and Square, both overriding draw() to print "Drawing a Circle" and "Drawing a Square" respectively. Create a list of Shape objects (containing both Circle and Square instances) and iterate through it, calling draw() on each. 
'''
class Shape:
    def __init__(self):
        pass

    def draw(self):
        print("Shape")   
    
class Circle(Shape):
    def __init__(self):
        pass

    def draw(self):
        print("Drawing a Circle")   

class Square(Shape):
    def __init__(self):
        pass

    def draw(self):
        print("Drawing a Square")   

shapes = [Circle(), Square(), Circle(), Square()]
for shape in shapes:
    shape.draw()
print("\n")    


'''
Question 5.2: Define a Printer base class with a print_document(doc) method. Create subclasses LaserPrinter and InkjetPrinter. Override print_document in each to simulate different printing behaviors (e.g., "Laser printing..." vs. "Inkjet printing..."). Demonstrate by putting instances in a list and calling the method. 
'''
class Printer:
    def __init__(self):
        pass
    
    def print_document(self, doc):
        pass

class LaserPrinter(Printer):
    def __init__(self):
        pass
    
    def print_document(self, doc):
        print("Laser Printing", doc)

class InkjetPrinter(Printer):
    def __init__(self):
        pass
    
    def print_document(self, doc):
        print("Inkjet Printing",doc)

doc = "sample"
printers = [LaserPrinter(), LaserPrinter(), InkjetPrinter(), InkjetPrinter()]

for printer in printers:
    printer.print_document(doc)
print("\n")    


'''
Question 5.3: Create a base class PaymentMethod with a method process_payment(amount). Create subclasses CreditCardPayment, PayPalPayment, and CashPayment. Override process_payment in each to simulate specific payment processing steps. 
'''
class PaymentMethod:
    def __init__(self):
        pass

    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self):
        pass

    def process_payment(self, amount):
        print("CreditCard transacted", amount)


class PayPalPayment(PaymentMethod):
    def __init__(self):
        pass

    def process_payment(self, amount):
        print("PayPalPayment transacted", amount)


class CreditCardPayment(PaymentMethod):
    def __init__(self):
        pass

    def process_payment(self, amount):
        print("CreditCard transacted", amount)


amount = 1000

pays = [CreditCardPayment(),PayPalPayment(),CreditCardPayment()]
for pay in pays:
    pay.process_payment(amount)
print("\n")    


# Polymorphism with a Common Interface (Duck Typing) 
'''
Question 5.4: Create two unrelated classes, Robot with a perform_action() method and Human with a perform_action() method. The Robot's method should print "Robot is performing a task," and the Human's should print "Human is performing an activity." Create a list containing instances of both Robot and Human and call perform_action() on each, demonstrating polymorphism through "duck typing." 
'''
class Robot:
    def __init__(self):
        pass

    def perform_action(self):
        print("Robot is performing a task")


class Human:
    def __init__(self):
        pass

    def perform_action(self):
        print("Human is performing an activity.")

actioners = [Human(), Robot(), Robot(), Human()]

for actioner in actioners:
    actioner.perform_action()
print("\n")    


'''
Question 5.5: Define a function process_items(items_list) that iterates through a list. Each item in the list is expected to have a process() method. Create two distinct classes, FileProcessor and DataAnalyzer, each with a process() method that does something different. Demonstrate process_items working with a list containing instances of both. 
'''
class FileProcessor:
    def __init__(self):
        pass
    
    def process(self):
        print("File Processer")

class DataAnalyzer:
    def __init__(self):
        pass
    
    def process(self):
        print("Data Analyzer")

def process_items(items_list):
    for item in items_list:
        item.process()

items = [DataAnalyzer(), FileProcessor(), FileProcessor()]
process_items(items)
print("\n")

'''
Question 5.6: Create a Notifier function that takes an object and calls its send_notification() method. Then, create two classes EmailSender and SMSSender, both having a send_notification() method (with different implementations). Show how Notifier can work with either. 
'''
class EmailSender:
    def __init__(self):
        pass

    def send_notification(self):
        print("Email Sent")

class SMSSender:
    def __init__(self):
        pass

    def send_notification(self):
        print("SMS Sent")

def Notifier(items):
    for item in items:
        item.send_notification()

items = [SMSSender(), EmailSender()]
Notifier(items)        
print("\n")



# Operator Overloading (Briefly) 
'''
Question 5.7: Create a Vector class with x and y coordinates. Override the __add__ operator so that two Vector objects can be added together, 
resulting in a new Vector object where x and y coordinates are summed independently. 
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):    
        return Vector(self.x + obj.x, self.y+obj.y)
    
    def print(self):
        print(f"Vector({self.x}, {self.y})\n")

v1 = Vector(2,3)
v2 = Vector(3,3)
v3 = v1+v2
v3.print()

'''
Question 5.8: For the Book class (from Q4.2), override the __len__ method to return the length of the book's title. 
'''
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(self.title,self.author, self.isbn, "\n")

    def __len__(self):
        return len(self.title)    

book = Book("7 Habits", "Stephen Covey", "p-1102")
print("Len of Book is ", len(book))

'''
Question 5.9: Create a Money class with an amount attribute. Override the __eq__ (equality) operator to compare two Money objects based on their amount. 
'''
class Money:
    def __init__(self, amount):
        self.amount= amount

    def __eq__(self, obj):
        if self.amount == obj.amount:
            return 1
        else: 
            return 0

m1 = Money(5000)
m2 = Money(2000)

if m1==m2:
    print("\nMoney1 is grater")
else:
    print("\nMoney2 is grater")


