#------------------------------------------------------------------------
#                     INSTANCE vs CLASS Attributes 
#------------------------------------------------------------------------

class MyClass:
  counter = 0

  def __init__(self, variable):
     self.variable = variable
     MyClass.counter =  MyClass.counter+1

  @classmethod
  def get_counter(cls):
     return MyClass.counter


mc = MyClass(2)
print("\nCounter Value is" ,MyClass.get_counter()) 


#Accessing class attr using an instance creates a local copy of that in its own instance 
class Example:
    shared = 0

var1 = Example()
var2 = Example()
var1.shared = 5

print(var1.shared)  # ouptut: 5  
print(var2.shared)  # ouptut: 0  




#------------------------------------------------------------------------
#                     STATIC vs CLASS Methods 
#------------------------------------------------------------------------


#---------------Demo Class-----------------
class DemoClass:
    def instance_method(self):
        return ("instance method called", self)

    @classmethod
    def class_method(cls):
        return ("class method called", cls)

    @staticmethod
    def static_method():
        return ("static method called",)

obj = DemoClass()
print(obj.instance_method())
print(obj.class_method())
print(obj.static_method())
print("---------------------------------------\n")
print(DemoClass.instance_method(obj))
print(DemoClass.class_method())
print(DemoClass.static_method())
print("---------------------------------------\n")



#-------------------Pizza Class---------------------
class Pizza:
    def __init__(self, toppings):
      self.toppings = list(toppings)

    def __repr__(self):
      return f"Pizza({self.toppings})"
    
    def add_topping(self, topping):
      self.toppings.append(topping)

    def remove_topping(self, topping):
      self.toppings.remove(topping)

    @classmethod
    def plain_pizza(cls):
        return cls(["Bread", "Cheese"])
    
    @staticmethod
    def get_size_in_inches(size):
        size_map = {
            "small": 8,
            "medium": 12,
            "large": 16,
        }
        return size_map.get(size, "Unknown size")


a_pizza = Pizza(["cheese", "tomatoes"])
print(a_pizza)
a_pizza.add_topping("garlic")
print(a_pizza)

#class method calling
print(Pizza.plain_pizza())

#static method calling
print(a_pizza.get_size_in_inches("medium"))
print(Pizza.get_size_in_inches("small"))

#---------------My Class-----------------
class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def class_method(cls, x):
        cls.class_variable += x
        return cls.class_variable

# Creating instances of the class
obj1 = MyClass(5)
obj2 = MyClass(10)

# Calling the class method
print(MyClass.class_method(3))  # Output: 3
print(MyClass.class_method(7))  # Output: 10