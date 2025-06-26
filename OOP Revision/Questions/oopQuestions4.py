
# Public Members 

'''
Question 4.1: Create a class Person with name and age as public attributes. Create an object, access and modify these attributes directly, and print them to demonstrate public access. 
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"name is {self.name}, {self.age} years old")

p1 = Person("khan", 54)
p1.display_info()
p1.name = "khuram"
p1.age = 55
p1.display_info()
print("\n")


'''
Question 4.2: Design a Book class with public attributes title, author, and isbn. Create a Book object and print its attributes. 
'''
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(self.title,self.author, self.isbn, "\n")

book = Book("7 Habits", "Stephen Covey", "p-1102")
book.display_info()

'''
Question 4.3: Create a class Wallet with a public attribute balance. Add methods add_money(amount) and spend_money(amount) that directly modify balance. 
'''
class Wallet:
    def __init__(self, balance):
        self.balance=balance

    def add_money(self, amount):
        self.balance+=amount
        return self.balance

    def spend_money(self, amount):
        if (self.balance - amount>=0):
            self.balance -= amount
        return self.balance               

w1 = Wallet(5000)
print(w1.add_money(200))
print(w1.spend_money(100), "\n")


# Protected Members (Convention) 

'''
Question 4.4: Modify the Person class to have _address as a protected attribute (using a single leading underscore). Show that it can still be accessed directly but explain why this is discouraged. Add a public method get_address() to access it. 
'''
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self._address = address

    def display_info(self):
        print(f"name is {self.name}, {self.age} years old, from {self._address}")

p1 = Person("khan", 54, "peshwar")
p1.display_info()
 
p1._address="rawalpindi"  #We can do this, but its discouraged as it not following proper conventions
p1.display_info()
print("\n")



'''
Question 4.5: For the BankAccount class, change account_number to _account_number to indicate it's protected. Add a public method get_account_number() to safely retrieve it. 
'''
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number 
        self.initial_balance = initial_balance

    def get_account_number(self):
        return self._account_number

c1 = BankAccount("C-100", 1000 )

print(c1.get_account_number())


'''
Question 4.6: Create a Configuration class that stores settings. Make a setting like _database_url protected. Explain that while Python doesn't strictly enforce protection, it's a signal for developers. 
'''
class Configuration:
    def __init__(self, database_url):
        self._database_url = database_url    #Even though this is accessable anywhere, any skilled pythhon dev will know its meant to be protected so only access it in this and the derived classes only

    def get_url(self):
        return self._database_url

c1 = Configuration("https:/safksrnjrkbgsjkbrgkjrbs")
print(c1.get_url(), "\n")



# Private Members (Name Mangling) 
'''
Question 4.7: Modify the Person class again. Make __ssn (Social Security Number) a private attribute (using double leading underscores). Try to access it directly from outside the class and observe the AttributeError. Then, add a public method set_ssn(ssn) and get_ssn() to properly interact with it. 
'''
class Person:
    def __init__(self, name, age, address, ssn):
        self.name = name
        self.age = age
        self._address = address
        self.__ssn = ssn

    def set_ssn(self, ssn):
        self.__ssn = ssn

    def __get_ssn(self):
        print(f"my ssn is {self.__ssn}") 

    def GETGET(self):
        self.__get_ssn()      


p1 = Person("khan", 54, "peshwar","P03221")
p1.set_ssn("P-1021")

# print(p1.__ssn)  #error: AttributeError: 'Person' object has no attribute '__ssn'
# p1.__get_ssn()
p1.GETGET()
print("\n")


'''
Question 4.8: In the BankAccount class, make __balance truly private. Implement deposit() and withdraw() methods to be the only ways to modify the balance. Add a get_balance() method. 
'''
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number 
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if (self.__balance - amount>=0):
            self.__balance -= amount


c1 = BankAccount("C-3010", 3000 )

c1.deposit(100)
c1.withdraw(50)
print(c1.get_balance())


'''
Question 4.9: Design a LoginSystem class. Make __password_hash a private attribute. Implement a set_password(password) method that hashes the password before storing and a verify_password(password) method that checks against the stored hash. 
'''

class LoginSystem:
    def __init__(self, password_hash):
        self.__password_hash = password_hash

    def set_password(self, password_hash):
        self.__password_hash=password_hash

    def verify_password(self, password):
        if(self.__password_hash ==password):
            return 1
        else:
            return 0
        
sys = LoginSystem("pakistan123")

if sys.verify_password("pakistan123"):
    print("\nCorrect Password")
else:
    print("Wrong Password")

        