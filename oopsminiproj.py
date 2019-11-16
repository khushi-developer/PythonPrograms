class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f"we have folloeing books in our librabry {self.name}")
        for book in self.booklist:
            print(book)

    def lendbooks(self,user,book):
        if book not in self.booklist:
            print("Book not available in our library")

        elif book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database has been updated. you can take the book now")
        else:
            print(f"book is already taken by {self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added to the booklist")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['python','c++','php'],"codewithharry")

    while True:
      print(f"welcome to the {harry.name} library. Enter your choice to continue")
      print("1. Display Books")
      print("2. lend a Book")
      print("3. add a Book")
      print("4. return a Book")

      user_choice = int(input())

      if user_choice==1:
          harry.displayBooks()

      elif user_choice==2:
          book = input("Enter the name of the book u want to lend")
          user = input("Enter your name")
          harry.lendbooks(user,book)

      elif user_choice==3:
          book=input("Enter the book you want to add")
          harry.addBook(book)

      elif user_choice==4:
          book = input("Enter the book you want to return")
          harry.returnBook(book)

      else:
          print("Not a valid option")

      user_choice2=''
      print("press q to quit and c to continue")
      while(user_choice2 != "c" and user_choice2!="q"):
          user_choice2 =input()
          if user_choice2=="q":
              exit()

          elif user_choice2=="c":
              continue

