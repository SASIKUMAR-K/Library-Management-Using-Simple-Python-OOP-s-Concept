# main file
# -----------
from libraryClass import Library

sist = Library(['C', 'C++', 'Python', 'Java', 'JavaScript'])
while True:
    print("""
   Welcome to Sist Library
+----------------------------+
| 1. Display all Books       |
| 2. Display Available Books |
| 3. Lent the Book           |
| 4. Return the book         |
| 5. Exit                    |
+----------------------------+ \n""")
    userChoice = int(input("Enter Your Choice : "))
    if userChoice == 1:
        sist.displayAllBooks()
    elif userChoice == 2:
        sist.displayAvailableBooks()
    elif userChoice == 3:
        print("\nPlease Enter the Following Details")
        userName = input("Enter Your Name : ")
        bookName = input("Enter The Book Name : ")
        sist.takeBook(userName, bookName)
    elif userChoice == 4:
        print("\nPlease Enter the Following Details")
        bookName = input("Enter the Book Name : ")
        sist.returnBook(bookName)
    elif userChoice == 5:
        print("\nThank you ...\nYou are exited")
        break
    else:
        print("Invalid Choice. Try Again")
    print("-----------------------------------------------------------------------------------")
