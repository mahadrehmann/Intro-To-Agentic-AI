'''
Project 1: Simple Library Management System 
Objective: Develop an OOP-based system to manage books and users in a library. 

Concepts to Apply: 

Classes & Objects: Book, User, Library. 

Attributes & Methods: Store book details (title, author, ISBN, availability), user details (name, user ID, borrowed books), and library collection. Methods for borrowing, returning, adding/removing books, registering/unregistering users. 

Encapsulation: Make book_id, user_id, and is_available private/protected where appropriate, with public methods for access and modification. 

Inheritance (Optional but Recommended): 
User base class, with subclasses Librarian and Member. Librarian might have additional methods like add_book() or remove_book(). 
Book base class, with subclasses FictionBook and NonFictionBook, potentially having unique attributes or methods. 

Polymorphism (Optional): If you implement different User types, you could have a perform_action() method that behaves differently based on the user type (e.g., Librarian can add_book, Member can borrow_book). 

Core Features: 
Book Management: Add new books, remove existing books, search for books by title/author/ISBN.

User Management: Register new users, remove users. 

Borrowing & Returning: Allow users to borrow books (if available) and return them. 

Tracking: Keep track of which books are borrowed by which user. 

User Interface: Simple text-based menu interface for interaction. 
'''

#Book Class
class Book:
    bookCount = 5

    def __init__(self, book_id, title, author, ISBN, is_available):
        self.__book_id = book_id
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self._is_available= is_available

    def check_availability(self):
        return self._is_available    

    def set_availability(self, value):
        self._is_available = value    

    def get_book_id(self):
        return self.__book_id    

# user Class
class User:
    userCount=1

    def __init__(self, user_id, name, borrowed_books):
        self.__user_id = user_id
        self.name = name
        self.borrowed_books = list(borrowed_books)

    def get_user_id(self):
        return self.__user_id  
  
    def borrow_book(self, book_id):
        pass              

    def return_book(self, book_id):
        pass

    def show_borrowed_books(self):
        pass 
      


# Librarian Class
class Librarian(User):
    def __init__(self, user_id, name, borrowed_books):
        super().__init__(user_id, name, borrowed_books)
        self.designation = "librarian" 

    def add_book(self, title, author, ISBN, is_available):
        print("\n------------------------------------")
        print("Creating New Book...")
        print("------------------------------------")        
        Book.bookCount+=1
        new_book = Book(Book.bookCount, title, author, ISBN, is_available)
        library.books.append(new_book)

    def remove_book(self):
        library.display_books()
        book_id = int(input("Which Book do you want to remove, Enter ID: "))

        for book in library.books:
            if book.get_book_id() == book_id:
                library.books.remove(book)
                print(f"Book \"{book.title}\" removed")
            else:
                print("nope")

# Member Class
class Member(User):
    def __init__(self, user_id, name, borrowed_books):
        super().__init__(user_id, name, borrowed_books)
        self.designation = "member" 

    def borrow_book(self, book_id):
        selected_book = 0
        for book in library.books:
            if book.get_book_id() == book_id:
                selected_book = book 
        
        self.borrowed_books.append(selected_book)               

    def return_book(self, book_id):
        selected_book = 0
        for book in library.books:
            if book.get_book_id() == book_id:
                selected_book = book 
        
        self.borrowed_books.remove(selected_book)

    def show_borrowed_books(self):
        for book in self.borrowed_books:
            print(f"Book \"{book.title}\" borrowed by User {self.get_user_id()}")  


# Library Class
class Library:
    def __init__(self, books, users):
        self.books = list(books)
        self.users = list(users)

    def display_books(self):
        print("\nBooks:")
        for book in self.books:
            if book.check_availability():
                print(f"{book.get_book_id()}. \"{book.title}\" by {book.author}")

    def display_users(self):
        print("\nUsers:")
        for user in self.users:
            print(f"{user.get_user_id()}. {user.name}")

    def register_user(self, name):
        print("\n------------------------------------")
        print("Creating New User...")
        print("------------------------------------")
        User.userCount+=1
        new_user = Member(User.userCount, name, [])
        self.users.append(new_user)

    def unregister_user(self):
        self.display_users()
        user_id = int(input("Enter the ID of the user you want to unregister: "))

        for user in self.users:
            if user.get_user_id() == user_id:
                self.users.remove(user)
                print(f"User \"{user.name}\" removed successfully.")


    def search_book(self):
        option = int(input("What thing do you want to search by?\n1. Title\n2. Author\n3. ISBN\n"))
        keyword = input("Enter your search keyword: ").lower()

        found = False


        match option:
            case 1:
                for book in self.books:
                    if keyword in book.title.lower():
                        print(f"{book.get_book_id()}. \"{book.title}\" by {book.author}")
                        found = True

            case 2:
                for book in self.books:
                    if keyword in book.author.lower():
                        print(f"{book.get_book_id()}. \"{book.title}\" by {book.author}")
                        found = True

            case 3:
                for book in self.books:
                    if keyword == book.isbn.lower():
                        print(f"{book.get_book_id()}. \"{book.title}\" by {book.author}")
                        found = True

            case _:
                print("Invalid option selected.")

        if not found:
            print("No books found")

# Some Predefined books
b1 = Book(1, "7 Habits Of Successful People", "Stephen Covey", 2001, bool(1))
b2 = Book(2, "Ego is the Enemy", "Ryan Holiday", 2002, bool(1))
b3 = Book(3, "Harry Potter and the Phiosophers Stone", "J. K. Rowling", 2003, bool(1))
b4 = Book(4, "Harry Potter and the Deathly Hallows", "J. K. Rowling", 2004, bool(1))
b5 = Book(5, "To Kill a Mockingbird", "Harper Lee", 2005, bool(1))
books = [b1,b2,b3,b4,b5] 

u1 = Member(1, "Mahad", [])
u2 = Librarian(2, "Mr. Usman", [])

users = [u1, u2]

library = Library(books, users)

print("------------------------------------")
print("Welcome to Library Managment System!")
print("------------------------------------")


mainLoop= 1
restart = 1
while(mainLoop):

    current_user = int(input("Enter your User id to continue: "))

    restart= 1
    while(restart):
        print("\n1. Add User\n2. Remove User" \
        "\n3. Add Book\n4. Remove Book \n" \
        "5. Borrow Book \n6. Return Book \n" \
        "7. Show Borrowed Books \n8. Search a Book" \
        "\n9. Logout\n0. Exit\n\nEnter your choice:")
        option = int(input())

        match option:
            case 0:
                restart = 0
                mainLoop = 0
            case 1:
                name = input("Enter Name:")
                library.register_user(name)
            case 2:
                library.unregister_user()    
            case 3:

                for user in library.users:
                    if user.get_user_id()==current_user and user.designation == "librarian":     
                        name = input("Enter Title:")
                        author = input("Enter Author Name:")
                        isbn = input("Enter ISBN:")
                        avail = input("Enter availability(0 or 1):")
                        user.add_book(name, author, isbn, avail)
                    else:
                        print("Members cant add books\n")    

            case 4: 
                for user in library.users:
                    if user.get_user_id()==current_user and user.designation == "librarian":     
                        user.remove_book()
                    else:
                        print("Members cant Remove books\n")   
            case 5: 
                library.display_books()
                id = int(input("\nPlease Choose A Book: "))
                
                for user in library.users:
                    if user.get_user_id() == current_user:
                        user.borrow_book(id)
                        
                # u1.borrow_book(id)

                for book in library.books:
                    if book.get_book_id() == id:
                        book.set_availability(0)

            case 6:
                id = int(input("\nEnter ID of the Book you wish to return: "))
                
                for user in library.users:
                    if user.get_user_id() == current_user:
                        user.return_book(id)
                # u1.return_book(id)

                for book in library.books:
                    if book.get_book_id() == id:
                        book.set_availability(1)

            case 7: 
                for user in library.users:
                    user.show_borrowed_books()

            case 8:
                library.search_book()

            case 9:
                restart = 0    

            case 55: #For Debugging
                library.display_books()
                library.display_users()    

            case _:  
                print("Invlaid input\n")            
        
