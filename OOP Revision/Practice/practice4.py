#------------------------------------------------------------------------
#                           ENCAPSULATION 
#------------------------------------------------------------------------

# --------------------Private--------------------
#example 1:
class PrivClass:
    def __init__(self, value):
        self.__value = value 

    def __show_value(self):  
        print(self.__value)
        
    def public_method(self):  
        self.__show_value()

obj = PrivClass(10)
# obj.__show_value()  # Error
# print(obj.__value)  # Error
obj.public_method()  
print("--------------------------------------")



#example 2:
class Person:
    def __init__(self,name, age):
        self.__name= name
        self.__age =age

    def display_info(self):
        print(f"My name is {self.__name} and my age is {self.__age}\n")

p1 = Person("Mahad", 20)
p1.display_info()

#BUT if we do directory/dict of p1
print(p1.__dict__, "\n")
print(dir(p1))             #this concept is calling magling where python stores the private var's name wiht class name     
print(p1._Person__name)    # this is NOT a good practice, dont do this

# So, in conclusion there's no pure encapsulation in python. But there IS some sort of protection. 
print("--------------------------------------")

#example 3
class TestingPrivate:
    def __init__(self, variable):
        self.__variable = variable

class DerivedTest(TestingPrivate):
    def __init__(self, variable):
        super().__init__(variable)

    def show(self):
        print(f"Var is {self.__dir__}")            

D1 =DerivedTest(20)
D1.show()
print(D1.__dict__)
print("--------------------------------------")



#---------------PROTECTED--------------------

# example 1:
class Base:
    def __init__(self, variable):
        self._variable = variable

class Derived(Base):
    def __init__(self, variable):
        super().__init__(variable)

    def access(self):
        print(f"Variable is {self._variable}")


#example 2:
class Student:
    def __init__(self, name, roll):
        self._name = name
        self._roll = roll

    def _display_roll(self):
        print("Roll:", self._roll)

class CS_Student(Student):
    def __init__(self, name, roll):
        super().__init__(name, roll)

    def displayDetails(self):
        print("Name:", self._name)
        self._display_roll()    #access protected

stu = Student("Mahad", "22i-0792")
# print(dir(stu))
print(stu._name)
stu._display_roll()

cs = CS_Student("Rehman","22p-0792")
# print(dir(cs))
cs.displayDetails()
print("--------------------------------------")


#Example 3  Normal use of protected variables
class Project:
    def __init__(self, name):
        self._name = name

class CV_Proj(Project):
    def __init__(self, name):
        super().__init__(name)

    def show_details(self):
        print(f"My Project Name is {self._name}")        

cv = CV_Proj("Alpha Project")

cv.show_details()
print("--------------------------------------")





#--------------------PUBLIC--------------------

#example:
class MyClass:
    def __init__(self, variable):
        self.variable = variable

mc = MyClass(2)
print("\n Value is" ,mc.variable)
print("--------------------------------------")


#exmaple:
class Basic:
    def __init__(self,val):
        self.val= val

b1 = Basic(23)
print(b1.val)
b1.val = 12
print(b1.val)
print("--------------------------------------")

#example:
class Test:
    def __init__(self, variable):
        self.variable = variable

class DerivedTest(Test):
    def __init__(self, variable):
        super().__init__(variable)

    def access(self):
        print(f"This is it {self.variable}")
