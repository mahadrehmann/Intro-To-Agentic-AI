'''
Project 2: Simple E-commerce System Till 11 pm today
Objective: Create an OOP system to simulate a basic online store, allowing customers to browse products, add them to a shopping cart, and place orders. 

Concepts to Apply: 

Classes & Objects: Product, Customer, ShoppingCart, Order. 

Attributes & Methods: 
Product: Name, price, stock quantity. Methods to check availability, reduce stock. 

Customer: Name, customer ID, contact info. 

ShoppingCart: Stores Product objects and quantities. Methods to add/remove items, calculate total. 

Order: Stores ordered items, total amount, customer info, order status. 


Encapsulation: Make product_id, customer_id, stock_quantity, and order_id private/protected, with public getters/setters or methods for interaction. 

Inheritance (Optional but Recommended): 
Product base class, with subclasses ElectronicProduct (might have warranty info) and ClothingProduct (might have size/color). 

Polymorphism (Optional): If different Product types, a display_details() method could show different info based on the product type. 

Core Features: 
Product Catalog: Add products to the store's catalog. 

Shopping Cart: Customers can add products to their cart, update quantities, remove items. 

Checkout Process: Calculate total cost, simulate placing an order. 

Order Tracking: Basic order status (e.g., "Pending", "Shipped"). 

User Interface: Simple text-based menu for customers to interact. 
'''

class Product:
    product_count = 6
    def __init__(self, product_id, name, price, stock_quantity):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self._stock_quantity = stock_quantity  

    def get_product_id(self):
        return self.__product_id

    def get_stock_quantity(self):
        return self._stock_quantity
    
    def check_availability(self):
        if self.stock_quantity>=1:
            return True
        else:
            return False
    
    def reduce_stock(self, amount):
        if self.stock_quantity-amount>=0:
            self.stock_quantity -= amount
        else:
            print("Stock Can't be Negative")
    
    def display_details(self):
        pass            

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, warranty_info):
        super().__init__(product_id, name, price, stock_quantity)
        self.warranty_info = warranty_info

    def display_details(self):
        print(f"{self.get_product_id()}. Electronic Product {self.name}, Price: Rs.{self.price}, Stock Amount: {self.get_stock_quantity()}, Warranty: {self.warranty_info}")            


class ClothingProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, size):
        super().__init__(product_id, name, price, stock_quantity)
        self.size = size
   
    def display_details(self):
        print(f"{self.get_product_id()}. Clothing Product {self.name}, Price: Rs.{self.price}, Stock Amount: {self.get_stock_quantity()}, Size: {self.size}")  


class ShoppingCart:
    def __init__(self):
        self.products = []   #TODO: when to udse what, whats the best practice? 
        '''
        timeit("[]")
        0.040084982867934334
        
        timeit("list()")
        0.17704233359267718
        
        Hence using [] is faster
        
        '''
        self.quantities = list()

    def add_items(self, item, amount):
        self.products.append(item)
        self.quantities.append(amount)    


class Order:
    order_count = 0

    def __init__(self, order_id, items, total_amount, customer_id):
        self.__order_id = order_id
        self.items = items
        self.total_items = total_amount
        self.customer_id = customer_id
        self.order_status = "Pending"

    def get_order_id(self):
        return self.__order_id

    def display_order(self):
        for item, qtn in self.items:
            print(f"{item.get_product_id()}. {item.name} Rs.{item.price}, Items Bought: {qtn}, Order Status: {self.order_status}")

class Customer:
    def __init__(self, customer_id, name, contact_info ):
        self.__customer_id = customer_id
        self.name = name
        self.contact_info= contact_info
        self.cart = ShoppingCart()
        self.orders = list()

    def get_customer_id(self):
        return self.__customer_id
    
    def add_to_cart(self, item, amount):
        self.cart.add_items(item, amount)

class Store:
    def __init__(self, products, customers):
        self.products = list(products)
        self.customers = list(customers)

    def display_catalogue(self):
        for item in self.products:
            item.display_details()

    def add_product(self):
        Product.product_count+=1
        name = input("Enter Product Name: ")
        price = input("Enter Product Price: ")
        sq = input("Enter Stock Quantity: ")
        typee = int(input("Is it an Electronic or Clothing Product? Enter 0 for Electronice and 1 for Clothing: "))

        if typee:
            size = input("Enter Cloth Size: ")
            new_p = ClothingProduct(Product.product_count, name, price, sq, size  )
        else:
            war = input("Enter Waranty info: ")
            new_p = ElectronicProduct(Product.product_count, name, price, sq, war)

        self.products.append(new_p)    
    
    def shop(self):
        self.display_catalogue()
        
        item_id = int(input("\nPlease enter the item Id which you want to add to cart: "))
        current_item = 0
        for item in self.products:
            if item.get_product_id() == item_id:
                current_item = item
                break

        amount =   input("\nHow many articles do you want: ")  
        current_user.add_to_cart(current_item, amount)

    def checkout(self):
        total_bill=0
        order_items = []

        # print("This is your cart: ")
        for item, qtn in zip(current_user.cart.products, current_user.cart.quantities):
            total_bill += (int(item.price) * int(qtn) )

            order_items.append((item, int(qtn)))
            # print(item.name, qtn)

        Order.order_count+=1
        new_order = Order(Order.order_count, order_items, total_bill, current_user)
        current_user.orders.append(new_order)

        new_order.display_order()
        new_order.order_status = "Dispathching"
        print("Checked Out! Yout Total is:", total_bill)    


# Some Predefined products
p1 = ElectronicProduct(1, "Microwave", 60000, 20, "5 Years")
p2 = ElectronicProduct(2, "Mini Fridge", 40000, 10, "12 Years")
p3 = ElectronicProduct(3, "Blender", 20000, 50, "2 Years")
p4 = ClothingProduct(4, "Plain T-shirt", 1000, 100, "Medium")
p5 = ClothingProduct(5, "Blue Jeans", 2000, 150, "Small")
p6 = ClothingProduct(6, "Socks", 500, 400, "Small")

products = [p1,p2,p3,p4,p5,p6]

c1 = Customer(1, "Mahad", "0333-9000000")
c2 = Customer(2, "Bonjour Khan", "0301-9000000")

customers = [c1, c2]

store = Store(products, customers)

print("\n------------------------------------")
print("Welcome to Mini Ecommerce System!")
print("------------------------------------")

mainLoop= 1
restart = 1
while(mainLoop):

    current_user_id = int(input("Enter your User id to continue: "))
    
    # First finding the current customer
    for user in store.customers:
        if current_user_id == user.get_customer_id():
           current_user = user
           break

    # print("Curremt banda hai:", current_user.name)

    restart = 1
    while(restart):
        print("\n1. Display Catalogue\n2. Add Product \n3. Shop \n4. Checkout \n5. View Cart \n6. View Orders\n9. Logout\n0. Exit\n\nEnter your choice:")
        option = int(input())

        match option:
            case 0:
                restart = 0
                mainLoop = 0
            case 1:
                store.display_catalogue()
            case 2:
                store.add_product()    
            case 3:
                store.shop()
            case 4:
                store.checkout()
            case 5:
                print("Your Cart:")
                for item, qtn in zip(current_user.cart.products, current_user.cart.quantities):
                    print(item.name, qtn)
                print("\n")
            case 6:
                print("Your Orders:")
                for order in current_user.orders:
                    order.display_order()
            case 7:
                restart = 0    
            case _:  
                print("Invlaid input\n")            
        
