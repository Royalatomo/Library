import os

class Library():

    # Available Books
    availableBooks = []

    # Borrowers List with Book
    borrowedBook = {}

    @staticmethod  # Used For Giving Books
    def take_book(name, book):

        # Name of borrowers with books they have taken
        borrowers = list(Library.borrowedBook.keys())
        borrowed = list(Library.borrowedBook.values())

        # Check if book is available or not
        if book in Library.availableBooks:

            # Check if the borrower aleready taken book in past or not
            if name in borrowers:
                print(
                    f"Sorry! {name}. You need to return {Library.borrowedBook[name]} Book First. Before taking another book!!")

            # If the borrower havn't taken any book in past and the book is available in the Library
            else:
                Library.borrowedBook[name] = book
                Library.availableBooks.remove(book)
                print(f"{name} borrowed {book} !!")

        # If someone already taken the book
        elif book in borrowed:
            print(f"Sorry {book} is already Borrowed By someone else!!")

        # If the library doesn't have the book meaning nor borrowers have borrowed and not it is available in the Library!!
        else:
            print(f"There is no book names {book} in our Library!!")

    @staticmethod  # If someone want's to return the book
    def return_book(name, book):

        # Geeting the list of borrowers(name) with books name.
        borrowed = list(Library.borrowedBook.values())
        borrower_name = list(Library.borrowedBook.keys())

        # Checking if they really borrowed the book which they are trying to return!!
        doesBookBorrowed = False

        try:
            # Checking if the person(name) is borrowing the book he is returing
            if Library.borrowedBook[name] == book:
                doesBookBorrowed = True

            # If he didn't borrowed that book whic he is returing. He borrowed different book.
            else:
                doesBookBorrowed = False

        # He didn't Borrowed any book from the library!
        except KeyError:
            doesBookBorrowed = False

        # If he was giving the right book and the right person is giving it(Who borrowed it)
        if doesBookBorrowed:

            Library.borrowedBook.pop(name)
            Library.availableBooks.append(book)
            print(f"{name} has returned Book: {book}")

        # IF no then,
        else:
            print(f"{name} can't return The Book: {book}")

    @staticmethod
    def browers():  # Returning the list of borrowers to the Admin!

        # Getting all borrowers name and books which they took
        borrowed = list(Library.borrowedBook.values())
        borrower_name = list(Library.borrowedBook.keys())

        # Returning in format ->  ""name: book ""
        borrowers_are = []

        for index, value in enumerate(borrowed):
            borrowers_are.append(
                f"Name: {borrower_name[index]},   Book: {value}")

        return borrowers_are

    @staticmethod  # If the user typed the name wrong he can change the name by this!!
    def changeName(name, newName):

        # Getting new and old name from the user
        old = name
        name = newName

        # Checking if the old name is there in any record!
        # If YES:
        try:
            # Changing It's name everywhere
            value = Library.borrowedBook[old]
            Library.borrowedBook.pop(old)
            Library.borrowedBook[newName] = value
            print(f"Name Updated From {old} to -> {newName}")

        # If NO: Telling the user that the old name hasn't mantioned anywhere so there is no point in changing it
        except KeyError:
            print(f"There is no student with name \"{old}\" Registered!! ")

    @staticmethod
    def import_data():

        stored_data = ""
        
        try:
            with open("borrow_data.txt", "r") as data:
                stored_data = data.read()
        except FileNotFoundError:
            return ''

        stored_data = stored_data.split('\n')
        borrowers_list = []
        books_name = []
        for i in stored_data:
            name = i.split(": ")
            for b in name:
                if b == name[0] and b != "":
                    borrowers_list.append(b)
                else:
                    if b != "":
                        books_name.append(b)
        
        Library.borrowedBook = {}
        for i in range(len(borrowers_list)):
            try:
                Library.borrowedBook[borrowers_list[i]] = books_name[i]
            except:
                return None

        # Book
        available_books = ''
        try:
            with open('book_data.txt', 'r') as book:
                available_books = book.read()
        except FileNotFoundError:
            return None

        available_books = available_books.split('\n')
        Library.availableBooks = []
        
        for i in available_books:
            if i != "":
                Library.availableBooks.append(i)
        


    @staticmethod
    def export_data():
        names = list(Library.borrowedBook.keys())
        books = list(Library.borrowedBook.values())
        
        try:
            os.remove('borrow_data.txt')
        except:
            pass

        with open('borrow_data.txt', 'w') as borrow:
            for i in range(len(names)):
                borrow.write(f"{names[i]}: {books[i]}\n")


       # Books ------------
        available_books = Library.availableBooks

        try:
            os.remove('book_data.txt')
        except:
            pass
        

        if len(available_books) > 0:

            with open("book_data.txt", "w") as book:
                for i in available_books:
                    book.write(f"{i}\n")


if __name__ == "__main__":
    ############## ACTUAL CODE ##############

    while True:

        # Geeting Right username and password from the file.
        correct_uname = ""
        correct_pass = ""

        with open("password.txt", "r") as a:
            # Removing new line character at the end
            correct_uname = a.readline().replace('\n', '')
            correct_pass = a.readline().replace('\n', '')

        # Console For Log-in by the user...
        print("#"*10, " Login To Librclearary Dashboard ", "#"*10)
        username = input("Username: ")
        password = input("Password: ")

        # Checking If The password was correct..
        # IF CORRECT:-
        if str(username) == str(correct_uname) and str(password) == str(correct_pass):
            # Create a object for operations
            name = Library()
            name.import_data() # ---------------------------------------

        # IF INCORRECT:-
        else:
            print("Wrong Username or Password!!")
            # Start the loop again
            continue

        # After log-in Console:-
        while True:        

            # Taking command form the user
            command = input("($): ")

            if command == "logout":
                break

            elif command == "quit":
                exit()

            elif command.lower() == "help":
                print("""\n
                Note: $$give_value$$ ---> don't include $$ with the given value
                $) check name $$name$$ : print how many books taken by $name$,
                $) add $$bookName$$ : Adds book to library,
                $) remove $$Bookname$$ : Removes the book from library,
                $) change $$oldName$$ to $$newName$$ : Changes Oldname to NewName Every where,
                $) give $$bookname$$ to $$studentName$$ : Give Book to students for Borrowing,
                $) taken $$bookname$$ from $$studentName$$ : Take book from students,
                $) show available : Shows Available books in the Library,
                $) show borrowers : print all the borrowers with book name.
                $) quit : Quit The Application.
                $) logout: Log out From the Current Account.
                $) ? : Displays the name of the Student Currently Working on\n""")

            try:
                if "change " in command:
                    # Fetching oldname and NewName from the command
                    cmd = command.split(' ')
                    cmd.remove("change")
                    index = cmd.index("to")

                    oldname = cmd[0:index]
                    oldname = " ".join(oldname)

                    newName = cmd[index+1:]
                    newName = " ".join(newName)
                    name.changeName(oldname, newName)
                    
                    name.export_data()

                elif "add " in command:
                    cmd = command.split(" ")
                    cmd.remove("add")
                    bookname = cmd[0:]
                    Library.availableBooks.append(" ".join(bookname))
                    print(f'Book: \"{" ".join(bookname)}\" is Added to the library!!')
                    name.export_data()

                elif "remove " in command:
                    cmd = command.split(" ")
                    cmd.remove("remove")
                    bookname = cmd[0:]
                    Library.availableBooks.remove(" ".join(bookname))
                    print(f'Book: \"{" ".join(bookname)}\" is removed from the library!!')
                    name.export_data()

                elif "check name" in command:
                    # Fetching $Name$ from the command
                    cmd = command.split(" ")
                    cmd.remove("check")
                    cmd.remove("name")
                    checking_name = cmd[0:]
                    checking_name = " ".join(cmd)

                    # Getting all borrowers
                    list1 = name.browers()
                    # If got any entry with name given
                    got_some = False

                    for i in list1:
                        if checking_name in i:
                            # If the name is present returning it..
                            print(i)
                            got_some = True
                        else:
                            got_some = False

                    # If there is no entry present with the name
                    if got_some == False:
                        print(f"{checking_name} Didn't borrowed any Book!!")

                elif "give " in command:
                    # Fetching $name$ and $bookname$ from the command
                    cmd = command.split(' ')
                    cmd.remove("give")
                    index = cmd.index("to")
                    bookname = cmd[0:index]
                    bookname = " ".join(bookname)

                    studentName = cmd[index+1:]
                    studentName = " ".join(studentName)

                    # Sending the data to Library Function
                    name.take_book(studentName, bookname)
                    name.export_data()

                # taken $bookname$ from $studentName$
                elif "taken " in command:
                    # Fetching $name$ and $bookname$ from the command
                    cmd = command.split(" ")
                    cmd.remove("taken")
                    index = cmd.index("from")
                    bookname = cmd[0:index]
                    bookname = " ".join(bookname)

                    studentName = cmd[index+1:]
                    studentName = " ".join(studentName)
                    # Sending the data to Library Function
                    name.return_book(studentName, bookname)
                    name.export_data()

                elif "show available" == command:
                    #Printing a Design with all the books present in the availableBooks list in Library class
                    print("-"*10)
                    for i in Library.availableBooks:
                        print(i)
                    print("-"*10)

                # show borrowers
                elif "show borrowers" == command:
                    #Printing a Design with Name of borrowers and books they taken
                    b_name = name.browers()
                    print("*"*10)
                    for i in b_name:
                        print(i)
                    print("*"*10)

                elif "?" == command:
                    # Giving the username with which they logged in
                    print(f"Logged In as: {username}")

                elif "" == command:
                    # If user types enter key from some space
                    pass

                else:
                    # If user typed a not known command
                    print(f"Invalid Command: {command}")

            except:
                # If user typed something which is unexpected!!
                print(f"Check Your Command!!")
