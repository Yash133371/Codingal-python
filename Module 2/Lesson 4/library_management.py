class Libary:
    def __init__(self, list, name):
        self.list = list
        self.name = name
        self.lend = {}
    
    def display_books(self):
        print(f"We have the following books in our libary: {self.name}")
        for book in self.list:
            print(book)
    
    def lend_book(self, user, book):
        if book not in self.lend.keys():
            self.lend.update({book:user})
            print("Lend database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lend[book]}")
    
    def add_book(self, book):
        self.list.append(book)
        print("Book has been added to book list")
    
    def return_book(self, book):
        self.lend.pop(book)
    
# After class code
books = Libary(["Python OOP", "Java basics", "C++ basics", "Javascript guide"], "Let's upskill")
while True:
    f"Welcome to the {books.name} libary. Enter your choice to continue"
    print("1. Display books")
    print("2. Lend a book")
    print("3. Add a book")
    print("4. Return a Book")
    user_choice = input()
    if user_choice not in ("1", "2", "3", "4"):
        print("Please enter a valid option")
        continue
    else:
        user_choice = int(user_choice)
    
    if user_choice == 1:
        books.display_books()
    elif user_choice == 2:
        book = input("Enter the name of the book you want to lend: ")
        user = input("Enter your name: ")
        books.lend_book(book, user)
    elif user_choice == 3:
        book = input("Enter the name of the book you want to add: ")
        books.add_book(book)
    elif user_choice == 4:
        book = input("Enter the name of the book you want to return: ")
        books.return_book(book)
    
    print("Press q to quit")
    user_choice = input()
    if user_choice == "q":
        break