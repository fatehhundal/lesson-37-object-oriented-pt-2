class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print("We have the following books in our library: ")
        for book in self.booksList:
            print(book)
        print(self.name)
    
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    
    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the list.")
    
    def returnBook(self, book):
        self.lendDict.pop(book)
    
if __name__ == '__main__':
    books = Library(["Python", "Rich Dad Poor Dad", "Harry Potter", "C++ Basics", "Algorithms by CLRS"], "Let's Upskill")

    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue.")
        print("1. Display books")
        print("2. Borrow a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input()

        if user_choice not in ["1", "2", "3", "4"]:
            print("Please enter a valid option.")
            continue
        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            books.displayBooks()
        elif user_choice == 2:
            user = input("Enter your username: ")
            book = input("Enter the name of the book you want to borrow: ")
            books.lendBook(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            books.returnBook(book)
        else:
            ("Not a valid option.")
        
        print("Press Q to quit and press C to continue:")
        user_choice2 = ""
        while(user_choice2 != "C" or user_choice2 != "c" and user_choice2 != "Q" or user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "Q" or user_choice2 == "q":
                exit()
            elif user_choice2 == "C" or user_choice == "c":
                continue