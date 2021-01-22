from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import os
from os import system, name 

global Home
Home = ''


class Functions:
        
        @staticmethod
        def addbook():

            
            booknameVar = simpledialog.askstring(title="Add Book To Library",
                                  prompt="Give Bookname To Add:")

            
            
                
            print(booknameVar)
            if booknameVar != "":
                    
                a = Main()
                Main.command = f"add {booknameVar}"
                output = a.main()
                print(Main.command)
                print(output)
                root = Tk()
                root.title("Success")
                lab = Label(root, text=output, fg='green').grid(row=1, column=1)
                root.mainloop()
         
            else:
                root = Tk()
                root.title("Error")
                lab = Label(root, text="Please Enter A Name Before Submitting!! ", fg='red')
                lab.grid(row=3, column=1)
                root.mainloop()

            # btn = Button(add_root, text="Add Book", command=input_get).grid(row=2, column=1)

            


        @staticmethod
        def rmbbook():


            
            booknameVar = simpledialog.askstring(title="Remove Book From Library",
                                  prompt="Give Bookname To Remove:")

            
            
                
            print(booknameVar)
            if booknameVar != "":
                    
                a = Main()
                Main.command = f"remove {booknameVar}"
                output = a.main()
                print(Main.command)
                print(output)
                
                if "not in our Library" in output:
                
                    root = Tk()
                    root.title("Not Found")
                    lab = Label(root, text=output, fg='red').grid(row=1, column=1)
                    root.mainloop()
                else:
                    root = Tk()
                    root.title("Success")
                    lab = Label(root, text=output, fg='green').grid(row=1, column=1)
                    root.mainloop()
         
            else:
                root = Tk()
                root.title("Error")
                lab = Label(root, text="Please Enter A Name Before Submitting!! ", fg='red')
                lab.grid(row=3, column=1)
                root.mainloop()



        @staticmethod
        def ckname():
            # check name $$name$$
            studentName = simpledialog.askstring(title="Search For Name",
                                  prompt="Give Name To Search:")

            
            if studentName != "":
                    
                a = Main()
                Main.command = f"check name {studentName}"
                output = a.main()
                print(Main.command)
                print(output)
                
                if "Didn't borrowed" in output:
                
                    root = Tk()
                    root.title("No Record")
                    lab = Label(root, text=output, fg='green').grid(row=1, column=1)
                    root.mainloop()
                
                else:
                    root = Tk()
                    root.title("Found")
                    lab = Label(root, text=output, fg='green').grid(row=1, column=1)
                    root.mainloop()
         
            else:
                root = Tk()
                root.title("Error")
                lab = Label(root, text="Please Enter A Name Before Submitting!! ", fg='red')
                lab.grid(row=3, column=1)
                root.mainloop()


        @staticmethod
        def chname():
            # change $$oldName$$ to $$newName$$

            old_Name = simpledialog.askstring(title="Change Name Of Student",
                                  prompt="Give Old Name:")

            
            if old_Name != "":
                    
                a = Main()
                Main.command = f"check name {old_Name}"
                output = a.main()
                
                
                
                if "Didn't borrowed" in output:
                
                    root = Tk()
                    root.title("No Record")
                    lab = Label(root, text="There is no recorde with this name can't change anything", fg='red').grid(row=1, column=1)
                    root.mainloop()
                
                else:
                    new_name = simpledialog.askstring(title="Change Name Of Student",
                                  prompt="Give Old Name:")
                    
                    if new_name != "":
                        # change $$oldName$$ to $$newName$$
                        cmd = f"change {old_Name} to {new_name}"
                        Main.command = cmd
                        a.main()
                        root = Tk()
                        
                        root.title("Name Changed All Over")
                        lab = Label(root, text=f"Student Name: \"{old_Name}\" Changed To: \"{new_name}\"", fg='green').grid(row=1, column=1)
                        root.mainloop()
                
                    else:
                        root = Tk()
                        root.title("Error")
                        lab = Label(root, text="Please Enter A New Name!! ", fg='red')
                        lab.grid(row=3, column=1)
                        root.mainloop()
         
            else:
                root = Tk()
                root.title("Error")
                lab = Label(root, text="Please Enter A Name Before Submitting!! ", fg='red')
                lab.grid(row=3, column=1)
                root.mainloop()            
            

            

        @staticmethod
        def gvbook():
            a = Main()
            
            # give $$bookname$$ to $$studentName$$
            book_name = simpledialog.askstring(title="Issue Which Book??",
                                  prompt="Give Bookname:")
            student_name = simpledialog.askstring(title="Issuer Name??",
                                  prompt="Give The Student Name:")
            
            if book_name != '' and student_name != '':
                Main.command = f"give {book_name} to {student_name}"                 
                output = a.main()
                print(output)
                if "Sorry" in output:
                
                    root = Tk()
                    root.title("Return Book First !!")
                    lab = Label(root, text=output, fg='red').grid(row=1, column=1)
                    root.mainloop()              

                elif "Issued the Book" in output:

                    root = Tk()
                    root.title(f"Success!!  Book Issued to {student_name}")
                    lab = Label(root, text=output, fg='green').grid(row=1, column=1)
                    root.mainloop()
                
                elif "Borrowed" in output:
                    
                    root = Tk()
                    root.title(f"Borrowed By SomeOne Else!!")
                    lab = Label(root, text=output, fg='red').grid(row=1, column=1)
                    root.mainloop()
                
                elif "no book name's" in output:

                    root = Tk()
                    root.title(f"Not Found")
                    lab = Label(root, text=output, fg='red').grid(row=1, column=1)
                    root.mainloop()

            else:
                root = Tk()
                root.title("Error")
                lab = Label(root, text="Please Enter A Name Before Submitting!! ", fg='red')
                lab.grid(row=3, column=1)
                root.mainloop()            
 

        @staticmethod
        def tkbook():
            
            # taken $bookname$ from $studentName$
            a = Main()
            
            book_name = simpledialog.askstring(title="Taking Which Book??",
                                  prompt="Give Bookname:")
            student_name = simpledialog.askstring(title="Borrower Name??",
                                  prompt="Give The Student Name:")
            
            if book_name != '' and student_name != '':
                Main.command = f"taken {book_name} from {student_name}"                 
                output = a.main()
                
                
                if "has returned Book" in output:
                
                    root = Tk()
                    root.title("Book Returned To Library !!")
                    lab = Label(root, text=output, fg='green').grid(row=1, column=1)
                    root.mainloop()              

                elif "can't return The Book" in output:

                    root = Tk()
                    root.title(f"Error")
                    lab = Label(root, text=output, fg='red').grid(row=1, column=1)
                    root.mainloop()
                
                

            else:
                root = Tk()
                root.title("Error")
                lab = Label(root, text="Please Enter A Name Before Submitting!! ", fg='red')
                lab.grid(row=3, column=1)
                root.mainloop()            

    
        
        @staticmethod
        def shAvialble():
            def clear():
                if name == 'nt': 
                    _ = system('cls') 
  
                # for mac and linux(here, os.name is 'posix') 
                else: 
                    _ = system('clear') 
            
            clear()
            a = Main()
            Main.command = "show available"
            output = a.main()
            
            num = 0
            for i in output:
                num += 1
                print(f"{num}) {i}")
            

        
        
        @staticmethod
        def shBorrowers():
            
            def clear():
                if name == 'nt': 
                    _ = system('cls') 
  
                # for mac and linux(here, os.name is 'posix') 
                else: 
                    _ = system('clear') 
            
            clear()
            a = Main()
            Main.command = "show borrowers"
            output = a.main()
            
            num = 0
            for i in output:
                num += 1
                print(f"{num}) {i}")

  

        @staticmethod
        def Quit():
            exit()



def gui():

    root = Tk()
    root.title("Python: Simple Login Application")
    width = 400
    height = 280
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    # ==============================METHODS========================================

    def Login(event=None):

        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(
                text="Please complete the required field!", fg="red")
        else:

            correct_uname = ''
            correct_pass = ''
            info = ''
            with open('password.txt', 'r') as read:
                a = read.read().split('\n')
                correct_uname = a[0]
                correct_pass = a[1]

            if USERNAME.get() == correct_uname and PASSWORD.get() == correct_pass:
                HomeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")

    def HomeWindow(event=None):

        global Home
        root.withdraw()
        Home = Toplevel()
        Home.title("Python: Simple Login Application")
        width = 600
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # ============= Waste ==============
        lb = Label(Home, text='          ', font=(
            'times new roman', 20)).grid(row=1, column=1, pady=10)
        lb = Label(Home, text='          ', font=(
            'times new roman', 20)).grid(row=1, column=2, pady=10)

        name = Library()
        name.import_data()

        all_func = Functions()

        lbl_home = Label(Home, text=f"Logged in as: {str(USERNAME.get()).title()} !", font=(
            'times new roman', 20)).grid(row=1, column=3, pady=10)

        btn_addbook = Button(Home, text='Add Books To Library', command=all_func.addbook).grid(
            row=2, column=3, pady=10)
        btn_rmbbook = Button(Home, text='Remove Books From Library',
                             command=all_func.rmbbook).grid(row=3, column=3, pady=10)
        btn_ckname = Button(Home, text='Search Student Name',
                            command=all_func.ckname).grid(row=4, column=3, pady=10)
        btn_chname = Button(Home, text='Change Student Name',
                            command=all_func.chname).grid(row=5, column=3, pady=10)
        btn_gvbook = Button(Home, text='Issue Book To Student',
                            command=all_func.gvbook).grid(row=6, column=3)
        btn_tkbook = Button(Home, text='Book Returned By The Student',
                            command=all_func.tkbook).grid(row=7, column=3, pady=10)
        btn_shAvialble = Button(Home, text='Show all the books in our Library',
                                command=all_func.shAvialble).grid(row=8, column=3, pady=10)
        btn_shBorrowers = Button(Home, text='Show all the Borrowers',
                                 command=all_func.shBorrowers).grid(row=9, column=3, pady=10)
        btn_shHelp = Button(Home, text='Help', command=all_func.shHelp).grid(
            row=10, column=3, pady=10)
        btn_back = Button(Home, text='Logout', command=Back).grid(
            row=10, column=4, pady=10)
        btn_quit = Button(Home, text='Quit', command=all_func.Quit).grid(
            row=10, column=5, pady=10)

    def Back():

        global Home

        Home.destroy()
        root.deiconify()

    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()
    BOOKNAME = StringVar()
    STUDENT_NAME = StringVar()
    OLD_NAME = StringVar()
    NEW_NAME = StringVar()


    # ==============================FRAMES=========================================
    Top = Frame(root, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    # ==============================LABELS=========================================
    lbl_title = Label(
        Top, text="Python: Simple Login Application", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)
 


    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.grid(pady=25, row=3, columnspan=2)
    btn_login.bind('<Return>', Login)

    root.mainloop()


class Library:

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
                return f"Sorry! \"{name}\". You need to return \"{Library.borrowedBook[name]}\" Book First. Before taking another book!!"

            # If the borrower havn't taken any book in past and the book is available in the Library
            else:
                Library.borrowedBook[name] = book
                Library.availableBooks.remove(book)
                return f"\"{name}\" Issued the Book: \"{book}\" !!"

        # If someone already taken the book
        elif book in borrowed:
            return f"Sorry \"{book}\" is already Borrowed By someone else!!"

        # If the library doesn't have the book meaning nor borrowers have borrowed and not it is available in the Library!!
        else:
            return f"There is no book name's \"{book}\" in our Library!!"

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
            return f"{name} has returned Book: {book}"

        # IF no then,
        else:
            return f"{name} can't return The Book: {book}"

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
            return f"Name Updated From {old} to -> {newName}"

        # If NO: Telling the user that the old name hasn't mantioned anywhere so there is no point in changing it
        except KeyError:
            return f"There is no student with name \"{old}\" Registered!! "

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


class Main:

    global command
    command = ''

    global name
    name = Library()

    print(command)
    @staticmethod
    def main():

        if Main.command == "quit":
            exit()

        elif Main.command.lower() == "help":
            return """\n
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
                    $) ? : Displays the name of the Student Currently Working on\n"""

        try:
            if "change " in Main.command:
                # Fetching oldname and NewName from the command
                cmd = Main.command.split(' ')
                cmd.remove("change")
                index = cmd.index("to")

                oldname = cmd[0:index]
                oldname = " ".join(oldname)

                newName = cmd[index+1:]
                newName = " ".join(newName)
                name.export_data()
                return name.changeName(oldname, newName)


            elif "add " in Main.command:
                cmd = Main.command.split(" ")
                cmd.remove("add")
                bookname = cmd[0:]
                Library.availableBooks.append(" ".join(bookname))
                name.export_data()
                return f'Book: \"{" ".join(bookname)}\" is Added to the library!!'
                

            elif "remove " in Main.command:
                try:
                    cmd = Main.command.split(" ")
                    cmd.remove("remove")
                    bookname = cmd[0:]
                    Library.availableBooks.remove(" ".join(bookname))
                    name.export_data()
                    return f'Book: \"{" ".join(bookname)}\" is removed from the library!!'  
                except ValueError:
                    return f'Book: \"{" ".join(bookname)}\" Is not in our Library!!'  


            elif "check name" in Main.command:
                # Fetching $Name$ from the command
                cmd = Main.command.split(" ")
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
                        return i
                        got_some = True
                    else:
                        got_some = False

                # If there is no entry present with the name
                if got_some == False:
                    return f"{checking_name} Didn't borrowed any Book!!"

            elif "give " in Main.command:
                # Fetching $name$ and $bookname$ from the command
                cmd = Main.command.split(' ')
                cmd.remove("give")
                index = cmd.index("to")
                bookname = cmd[0:index]
                bookname = " ".join(bookname)

                studentName = cmd[index+1:]
                studentName = " ".join(studentName)
                
                # Sending the data to Library Function
                a = name.take_book(studentName, bookname)
                name.export_data()
                return a

            # taken $bookname$ from $studentName$
            elif "taken " in Main.command:
                # Fetching $name$ and $bookname$ from the command
                cmd = Main.command.split(" ")
                cmd.remove("taken")
                index = cmd.index("from")
                bookname = cmd[0:index]
                bookname = " ".join(bookname)

                studentName = cmd[index+1:]
                studentName = " ".join(studentName)
                # Sending the data to Library Function
                a = name.return_book(studentName, bookname)
                name.export_data()
                return a

            elif "show available" == Main.command:
                string = []
                # Printing a Design with all the books present in the availableBooks list in Library class
                
                num = 0
                for i in Library.availableBooks:
                    num += 1
                    string.append(f"{i}\n")
                
                return string

            # show borrowers
            elif "show borrowers" == Main.command:
                string = ''
                # Printing a Design with Name of borrowers and books they taken
                b_name = name.browers()
                
                return b_name

            elif "?" == Main.command:
                # Giving the username with which they logged in
                return f"Logged In as: {username}"

            elif "" == Main.command:
                # If user types enter key from some space
                pass

            elif 'help' == Main.command:
                pass

            else:
                # If user typed a not known command
                return f"Invalid Command: {Main.command}"

        except:
            # If user typed something which is unexpected!!
            return f"Check Your Command!!"


if __name__ == "__main__":
    ############## ACTUAL CODE ##############

    mode = 'g'

    if mode == 'c':

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
                name.import_data()  # ---------------------------------------

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

                else:
                    Main.command = command
                    a = Main()
                    a.main()

    else:
        gui()
        
