#Basic Class
class Test:
    def __init__(self, number):
        self.number = number

    def printNum(self):
        print("My Number is:" ,self.number)    


t1 = Test(12)
# t1.printNum()


#Inheritance and using the super() statement
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calcArea(self):
        return self.length * self.width

rec = Rectangle(10,5)
print(rec.calcArea())

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)

    def calcArea(self):
        return self.length * self.width

sq = Square(6)
print(sq.calcArea())



#PolyMorphism
class Vehicle:
  def __init__(self, brand):
    self.brand = brand

  def move(self):
    print("Vrooom")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Waterrrr")

class Plane(Vehicle):
  def move(self):
    print("flyyyyy")

car1 = Car("Mehran")  
boat1 = Boat("Boat")
plane1 = Plane("Boeing 777")

car1.move() 
boat1.move() 
plane1.move()
