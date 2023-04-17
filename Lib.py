# class file
# ------------
class Library:
    def __init__(self, books):
        self.allBooks = books
        self.availabeBooks = books[:]
        self.bookBuy = {}

    def displayAllBooks(self):
        print("\nAll Books")
        print("-----------------")
        for book in self.allBooks:
            print(book)

    def displayAvailableBooks(self):
        print("\nAvailable Books")
        print("-----------------")
        for book in self.availabeBooks:
            print(book)

    def takeBook(self, userName, bookName):
        if bookName in self.availabeBooks:
            self.bookBuy.update({bookName: userName})
            self.availabeBooks.remove(bookName)
            print("""====================================
Welcome %s
Take the %s book. Please Return in one month.
Thank You ....
=====================================
        """ % (userName, bookName))
        elif bookName in self.allBooks:
            print("\nThe %s book is already taken by %s" %
                  (bookName, self.bookBuy[bookName]))
        else:
            print(
                "\nSorry %s, The %s book is not Available. Press 1 to check Whether this book is available or not" % (userName, bookName))

    def returnBook(self, bookName):
        if bookName in list(self.bookBuy.keys()):
            print("Thank you %s. The %s book is returned" %
                  (self.bookBuy[bookName], bookName))
            self.bookBuy.pop(bookName)
            self.availabeBooks.append(bookName)
        elif bookName not in self.allBooks:
            print("Incorrect Book")
