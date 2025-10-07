# Importing the modules ===>
import tkinter as tk
from tkinter import ttk
import time
# import mysql.connector
from tkinter import messagebox
import sqlite3
from telethon.sync import TelegramClient
import requests

# from telethon.errors.rpcerrorlist import PhoneNetworkError


# Initializing the basic window
root = tk.Tk()
root.geometry("1350x700+0+0")
root.resizable(False , False)
root.title("Library Managment System")

# Initializing the vaiales 
currentDate = 0
currentTime = 0
searchFlag = 0
row = 0
flag = 0

################################################################################ ################CONNECTION OF DATABASE####### ##############################CONNECTION OF DATABASE############## ##################CONNECTION OF DATABASE############################ ################CONNECTION OF DATABASE############################ #######################################################################

# connection = mysql.connector.connect(host = "localhost" , user = "root" , password = "root123" )


database = "LibraryDatabase"


connection = sqlite3.connect(database)
cursor = connection.cursor()


# Creating database with name LibraryDatabase

# databaseCreateQuery = f"CREATE DATABASE IF NOT EXISTS  {database}"
# cursor.execute(databaseCreateQuery)

# Query for use the database
# cursor.execute(f"USE {database}")

# Query to create table For =========> BOOK NAME >>>> AUTHER NAME ==========>
tableName = "BookData"
cursor.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (BookName VARCHAR(50) UNIQUE ,AutherName VARCHAR(50) , numberOfBooks  INT) ")

# 
####################Creating table for store the student details##################
#
tableName2 = "studentData"
studentDetailTableQuery = f"CREATE TABLE IF NOT EXISTS {tableName2}(bookName VARCHAR(50) , autherName VARCHAR(50) , studentName VARCHAR(50) , branch VARCHAR(50) , year VARCHAR(50) , id VARCHAR(50) , dateOfReturn VARCHAR(50) , daysLeft INT , mobileNumber INT)"

cursor.execute(studentDetailTableQuery)

# pyinstaller --onefile --noconsole --icon=E:\ALL_PROGRAMS\PYTHON\project\LibraryManagmentSystem\icon2.ico --name "Library Management System" main.py


# pyinstaller --onefile --noconsole --icon=icon2.ico --name "Library Management System" main.py


# cursor.execute(f"DROP TABLE {tableName}" )
# cursor.execute(f"DROP TABLE {tableName2}" )
# print("drop")

#################################################################################
#################################################################################


# Defining the Functions

#Function for diffinng the date and time
def dateTime():
    currentDate = time.strftime("%d/%m/%Y")
    currentTime = time.strftime("%H:%M:%S")
    date = tk.Label(nameFrame , text = f"    Date : {(currentDate)} \nTime : {currentTime}" , fg = "skyblue" , font = ("Arial" , 20 , "bold") , bg = "green")
    date.place(x = 0 , y = 0)
    root.after(1000 , dateTime)


##################################################################################
##########################CLASS FOR ADDING THE BOOK'S DATA########################
##########################CLASS FOR ADDING THE BOOK'S DATA########################
##########################CLASS FOR ADDING THE BOOK'S DATA########################
##################################################################################   
class NewRecord:
    def __init__(self , cursor):
        # self.bookNameEntryDb = None
        # self.autherNameEntryDb = None
        pass
        
    def addNewBook(self):
        self.addNewBookFrame = tk.Toplevel(root )
        self.addNewBookFrame.title("Add new book ->")
        self.addNewBookFrame.geometry("500x300+650+100")
        self.addNewBookFrame.resizable(width = False , height = False)

        # Adding Entry field for book name and auther name
        # book name label
        bookName = tk.Label(self.addNewBookFrame , text = "Enter Book Name : " , font = ("Ariel" , 16 , "bold"))
        bookName.grid(row = 0 , column = 0  , pady = 20)
        # book nameEntry
        self.bookNameEntryDb = tk.Entry(self.addNewBookFrame , font = ("Ariel" , 15 ,) , bd = 3 , bg= "pink" )
        self.bookNameEntryDb.grid(row = 0 , column = 1  , pady = 20)
            
        # Auther name label
        autherName = tk.Label(self.addNewBookFrame , text = "   Enter Auther Name : " , font = ("Ariel" , 16 , "bold"))
        autherName.grid(row = 1 , column = 0  , pady = 20)
        # auther nameEntry
        self.autherNameEntryDb = tk.Entry(self.addNewBookFrame , font = ("Ariel" , 15 ,) , bd = 3 , bg= "pink" )
        self.autherNameEntryDb.grid(row = 1 , column = 1   , pady = 20)

        numberOfBooks = tk.Label(self.addNewBookFrame , text = "Enter number of copies :" ,  font = ("Ariel" , 16 , "bold"))
        numberOfBooks.grid(row = 2 , column = 0  , pady = 20)

        self.numberOfBooksEntry = tk.Entry(self.addNewBookFrame ,  font = ("Ariel" , 15 ,) , bd = 3 , bg= "pink")
        self.numberOfBooksEntry.grid(row = 2 , column = 1 , pady = 20)
        # Add book nameand auther name button
        addBookAutherName = tk.Button(self.addNewBookFrame , text = " Add " , font = ("Ariel" , 15 , "bold") , bg = "black" , fg = "white" , width = 10 , command = self.addNewData)
        addBookAutherName.place( x = 200 , y = 230 )

    # function to add to new data (book name and auther name ) in the database
    def addNewData(self):
        bookName = self.bookNameEntryDb.get()
        autherName = self.autherNameEntryDb.get()
        numberOfBooks = self.numberOfBooksEntry.get()
        if(bookName == "" or autherName == "" or numberOfBooks == ""):
            messagebox.showerror("Error" , "Please enter valid details")        
        else:
            try:
                cursor.execute(f"INSERT INTO BookData (BookName , AutherName , numberOfBooks) VALUES {(bookName , autherName , numberOfBooks)}")
                messagebox.showinfo("Success" , f"Successfully add new book with: \n\n Book Name : {bookName} \n Auther Name : {autherName} \n with {numberOfBooks} number of copies")
                connection.commit()
                # destoying the add new book frame after adding the book
                self.addNewBookFrame.destroy()
            except:
                messagebox.showerror("Error" , "Duplicate entry not allow") 


            tableName = "BookData" 
            getBookNameQuery = f"SELECT * FROM {tableName}  "
            cursor.execute(getBookNameQuery)
            rows = cursor.fetchall()
            # print(rows)
           
    
        
    def deleteBook(self):
        self.deleteBookFrame = tk.Toplevel(root )
        self.deleteBookFrame.title("Delete Book Record ->")
        self.deleteBookFrame.geometry("530x300+650+100")
        self.deleteBookFrame.resizable(width = False , height = False)

        # Adding Entry field for book name and auther name
        # book name label
        bookName = tk.Label(self.deleteBookFrame , text = "Enter Book Name : " , font = ("Ariel" , 16 , "bold"))
        bookName.grid(row = 0 , column = 0  , pady = 20)
        # book nameEntry
        self.bookNameEntryDb = tk.Entry(self.deleteBookFrame , font = ("Ariel" , 15 ,) , bd = 3 , bg= "pink" )
        self.bookNameEntryDb.grid(row = 0 , column = 1  , pady = 20)
            
        # Auther name label
        autherName = tk.Label(self.deleteBookFrame , text = "   Enter Auther Name : " , font = ("Ariel" , 16 , "bold"))
        autherName.grid(row = 1 , column = 0  , pady = 20)
        # auther nameEntry
        self.autherNameEntryDb = tk.Entry(self.deleteBookFrame , font = ("Ariel" , 15 ,) , bd = 3 , bg= "pink" )
        self.autherNameEntryDb.grid(row = 1 , column = 1   , pady = 20)

        self.numberOfBooks = tk.Label(self.deleteBookFrame , text = "   Enter Number of copies : " , font = ("Ariel" , 16 , "bold"))
        self.numberOfBooks.grid(row = 2 , column = 0  , pady = 20)
        # auther nameEntry
        self.numberOfBooksEntry = tk.Entry(self.deleteBookFrame , font = ("Ariel" , 15 ,) , bd = 3 , bg= "pink" )
        self.numberOfBooksEntry.grid(row = 2 , column = 1   , pady = 20)


        # Add delete button
        deleteBookAutherName = tk.Button(self.deleteBookFrame , text = " Delete " , font = ("Ariel" , 15 , "bold") , bg = "black" , fg = "white" , width = 10 ,command = self.deleteEntelightgreenBook )
        deleteBookAutherName.place( x = 210 , y = 230 )
    
    def deleteEntelightgreenBook(self):
        numberOfBooks = 0
        bookName = self.bookNameEntryDb.get()
        autherName = self.autherNameEntryDb.get()
        numberOfBooks = self.numberOfBooksEntry.get()
        data = 0
        cursor.execute(f"SELECT * FROM {tableName} WHERE bookName = '{bookName}' and autherName = '{autherName}' ")

        data = cursor.fetchall()
        # print("before update" , data)
        if (data == []):
            messagebox.showerror("Error" , "Book is not available")
        else:
            numberOfBooksAvailable = 0
            # print(data[0][2])
            numberOfBooksAvailable = ( (data[0][2]) - int(numberOfBooks) )
            # print(numberOfBooksAvailable)
            if(bookName == "" or autherName == "" or numberOfBooks == ""):
                messagebox.showerror("Error" , "Please enter valid datails")
            else:
                if(numberOfBooksAvailable <= 0):
                    cursor.execute(f"DELETE FROM {tableName} WHERE bookName = '{bookName}' and autherName = '{autherName}' ")
                    messagebox.showinfo("Success" , f"Successfully delete book \n\n book Name : {bookName} \n Auther Name : '{autherName}'")
                    connection.commit()
                    self.deleteBookFrame.destroy()
                else:
                    cursor.execute(f"UPDATE {tableName} SET numberOfBooks =       '{numberOfBooksAvailable}' WHERE bookName = '{bookName}' and autherName = '{autherName}' ")
                    connection.commit()
                    messagebox.showinfo("Success" , f" Number of copies removed : {numberOfBooks}  \n\n Number of copies available : {numberOfBooksAvailable}")                
                    self.deleteBookFrame.destroy()
                    

                    cursor.execute(f"SELECT * FROM {tableName}")
                    data = cursor.fetchall()
                    # print("after uptate" , data)
                connection.commit()
        # tableName = "BookData" 
        # getBookNameQuery = f"SELECT (bookName ,autherName)  FROM {tableName} WHERE bookName = {bookName} , autherName = {autherName}  "
        # cursor.execute(getBookNameQuery)
        # rows = cursor.fetchall()
        # print(rows)
    def searchData(self):
        tableName = "BookData"
        bookName = bookNameEntry.get()
        autherName = autherNameEntry.get()
        if(bookName == "" or autherName == ""):
            messagebox.showerror("Error" , "Enter valid details")
        else:
            selectQuery = f"SELECT * FROM {tableName} WHERE bookName = '{bookName}' AND autherName = '{autherName}'"
            cursor.execute(selectQuery)
            data = cursor.fetchall()
            # present = (data == [(f'{bookName}', f'{autherName}')])
            
            if(data == []):
                searchFlag = 0
                messagebox.showerror("Error" , "Book is not availble")
                return(searchFlag)
            else:
                searchFlag = 1
                messagebox.showinfo("Success" , f"Find the book with :\n\n Book Name : {bookName} \n Auther Name : {autherName} \n Number of copies : {data[0][2] }" )
                return (searchFlag)


##################################################################################
##################################################################################


##################################################################################
##########################CLASS FOR ADDING THE STUDENT DATA#######################
##########################CLASS FOR ADDING THE STUDENT DATA#######################
##########################CLASS FOR ADDING THE STUDENT DATA#######################
##################################################################################

class StudentData:
    def __init__(self , cursor):
        pass

    def borrowList(self  ):
        

        cursor.execute(f"SELECT *FROM {tableName2}")
        data = cursor.fetchall()
        # print("data : " , data)
        row = 0
        for ele in range (data.__len__() + 10):
            row += 1
            for i in range(10):

                self.borrowListOfStudent = tk.Label(borrowListFrame , text = "                     " , bg = "lightgreen" , font = ("Arial" , 14))
                # print(ele[i])
                self.borrowListOfStudent.grid(row = row, column = i )            
    
        # print(data.__len__())
        # self.borrowListOfStudent.grid_forget()
        row = 0
        if(data):
            for ele  in data:
                # print(ele)
                row += 1
                
                for i in range(ele.__len__()):

                    self.borrowListOfStudent = tk.Label(borrowListFrame , text = f"{ele[i]}" , fg = "black" , bg = "lightgreen" , font = ("Arial" , 14 , "bold"))
                    # print(ele[i])
                    self.borrowListOfStudent.grid(row = row, column = i )            

        connection.commit()
        root.after((1000 * 60) , self.borrowList)



    def getStudentData(self):
        bookName = bookNameEntry.get()
        autherName = autherNameEntry.get()
        studentName = studentNameEntry.get()
        studentBranch = studentBranchEntry.get()
        studentYear = studentYearEntry.get()
        studentID = studentIdEntry.get()
        studentNumber = studentNumberEntry.get()
        searchFlag = nR.searchData()
        
        if(searchFlag == 0):
            messagebox.showerror("Error" , "Book is not available.")
        elif(searchFlag == 1):
            numberOfBooksAvailable = 0
            cursor.execute(f"SELECT * FROM {tableName} WHERE bookName = '{bookName}' and autherName = '{autherName}'")

            data = cursor.fetchall()
            numberOfBooksAvailable = (int(data[0][2]) - int(1))
            if(numberOfBooksAvailable < 0):
                messagebox.showerror("Error" , "No copy of book is available.")
                flag = 0
            else:
                flag = 1
                if(studentName == "" or studentBranch == "" or studentYear == "" or studentBranch == "" or studentID == "" or bookName == "" or autherName == "" or studentNumber == ""):
                    messagebox.showerror("Error" , "Please fill the all nessesary details.")  
                    flag = 0          

        if(flag == 1):
            flag = 0
            try:
                todaysDate = time.strftime("%d/%m/%y")
                todaysDateFormat = time.strptime(todaysDate , "%d/%m/%y")
                todaysDateFormat = time.mktime(todaysDateFormat) + (15*24*60*60)
                returnDateFormat = time.localtime(todaysDateFormat)
                returnDate = time.strftime("%d/%m/%y" , returnDateFormat)
                dateOfReturn = returnDate
                        
                if(studentNumber.__len__() != 10):
                    messagebox.showerror("Error" , "Please enter 10 digit number.")
                else:
                    cursor.execute(f"INSERT INTO {tableName2} (bookName , autherName  , studentName , branch , year , id , dateOfReturn , daysLeft , mobileNumber) VALUES {(bookName , autherName ,studentName , studentBranch , studentYear , studentID , dateOfReturn , 0 ,int(studentNumber))}")
                    self.daysLeft()
                    connection.commit()

                    messagebox.showinfo("Success" , f"Student added to borrow list with \n Student Name : '{studentName}'\n Student ID : '{studentID}'")
                    addFlag = 1
            except:
                # print("error")
                messagebox.showerror("Error" , "Something went wrong.")

                cursor.execute(f"SELECT *FROM {tableName2}")
                data = cursor.fetchall()
                    # print(data)
        connection.commit()                    


        try:
            if(addFlag == 1):
                cursor.execute(f"UPDATE {tableName} SET numberOfBooks = '{numberOfBooksAvailable}' WHERE bookName = '{bookName}' and autherName = '{autherName}'")
                connection.commit()
                addFlag = 0

        except:
            messagebox.showerror("Error" , "Something went wrong.")
            searchFlag = 0

        self.borrowList()
                
    # Function for deleting the student record from the student data table
    def deleteStudentRecord(self):
        deleteFlag = 0
        studentIDForDelete = searchEntryForDeleteRecord.get()
        
        if(studentIDForDelete == ""):
            messagebox.showerror("Error" , "Enter valid 'student ID' ")
        else:
            try:
                # cursor.execute(f"SELECT *FROM {tableName2} WHERE id = '{studentIDForDelete}' ")
            
                cursor.execute(f"SELECT * FROM {tableName2} WHERE id = '{studentIDForDelete}' ")
                data = cursor.fetchall()
                # print(data)
                if(data == []):
                    messagebox.showerror("Error" , "Student is not found in borrow list.")
                    # print("if")
                else:
                    # print("else")

                    cursor.execute(f"DELETE FROM {tableName2} WHERE id = '{studentIDForDelete}' ")

                    connection.commit()
                    messagebox.showinfo("Success" , f"Student is remove with: \n Student ID : {studentIDForDelete}")    
            



                    # {data[0][0]}  book name
                    # {data[0][1]}  auther name
                    # print("data :" , data)
                    # print(data[0][0])
                    # print(data[0][1])
                    cursor.execute(f"SELECT *FROM {tableName} WHERE bookName = '{data[0][0]}' and autherName = '{data[0][1]}'")
                    data = cursor.fetchall()
                    # print("success")
                    # print("data",data[0][2])
                    numberOfBooksAvailable = (int(data[0][2]) + int(1))
                    # connection.commit()
                    # print(numberOfBooksAvailable)
                    # print("sucees 2")
                    try:
                        # print(data)
                        # print("ok",data[0][1])
                        cursor.execute(f"UPDATE {tableName} SET numberOfBooks = '{numberOfBooksAvailable}' WHERE bookName = '{data[0][0]}' and autherName = '{data[0][1]}'")
                        # print("update")


                        connection.commit()
                    except:
                        messagebox.showerror("Error" , "Something went wrong.")   
                        connection.commit()

            except:
                messagebox.showerror("Error" , "Student is not found in borrow list.")
                connection.commit()
        # cursor.execute(f"SELECT *FROM {tableName2}")
        # data = cursor.fetchall()
        # print(data)
        # connection.commit()
        self.borrowList()

  
    def daysLeft(self):
        cursor.execute(f"SELECT *FROM {tableName2}")
        data = cursor.fetchall()
        # print(data)
        connection.commit()
        for i in range(data.__len__()):
            dateOfReturn = data[i][6]
            
            todaysDate = time.strftime("%d/%m/%y")
            todaysDateFormat = time.strptime(todaysDate , "%d/%m/%y")
            dateOfReturnFormat = time.strptime(dateOfReturn , "%d/%m/%y")
            daysLeftFormat = (time.mktime(dateOfReturnFormat) - time.mktime(todaysDateFormat))  
            # print(daysLeftFormat)
            # daysLeft = 0
            try:
                daysLeftFormat = time.localtime(daysLeftFormat)
                daysLeft = int(time.mktime(daysLeftFormat) / (24*60*60))

            except:
                daysLeft = 0
                # print("adsfjkodjsv")
            #  print(daysLeft)
            if(daysLeft >= 0):
                cursor.execute(f"UPDATE {tableName2} SET daysLeft = '{daysLeft}' WHERE bookName = '{data[i][0]}' and autherName = '{data[i][1]}' and id = '{data[i][5]}'")
            connection.commit()
            
            
        root.after(1000 , self.daysLeft)
    
    def functionCallerForMessage(self):
        # print("hello")
        
        # self.dataCount = 0
        # self.msg = 0
        self.messageSend = False
        cursor.execute(f"SELECT *FROM {tableName2}")
        data = cursor.fetchall()
        if(data.__len__() == 0):
            messagebox.showerror("Error" , "No any student in the borrow list.")
        for i in range(data.__len__()):
            bookName = data[i][0]
            daysLeft = data[i][7]
            mobileNumber = data[i][8]
            if(daysLeft <= 2 and daysLeft >= 0):
                # self.dataCount =+ 1
                if(self.checkInternet()):
                    try:
                        self.returnBookMessage(daysLeft , bookName , mobileNumber , data)
                        self.messageSend = True

                    except:
                        self.messageSend = False
                        
                else:
                    messagebox.showwarning("Warning" , "Check Internet Connection....")
                    self.messageSend = False
        if(self.messageSend == True):
            messagebox.showinfo("Success" , "Messages send succefully.")
        
    def checkInternet(self):
        try:
            requests.get("http://www.google.com" , timeout = 1)
            return True
        except:
            return False

    def returnBookMessage(self , daysLeft , bookName , mobileNumber , data):
        
        # print(self.msg)
        mobileNumber = "+91" + str(mobileNumber)
        # Replace the values below with your own credentials
        api_id = 'Enter your telegeram api id here.'
        api_hash = 'Enter your telegram api hash here.'
        phone_number = 'Enter your mobile no here with the country cide.'  # This should include the country code, e.g., +9134567890

        # Create a TelegramClient instance
        client = TelegramClient('session_name', api_id, api_hash)
        
    
        async def send_telegram_message(mobileNumber):
            try:
                # Connect to Telegram
                await client.start()
                    
                # messagebox.showerror("Error" , "Connect Internet Connection.")

                # Get the input entity (user, group, or channel) of the recipient
                entity = await client.get_input_entity(mobileNumber)  # Replace with the recipient's phone number

                # Send the message

                message = f"""
                Subject: Reminder: Renew or Return Your TSSM Library Book\n\nDear Student,\n\n          We hope this message finds you well. We wanted to remind you that the validity period for the book titled "  {bookName}  " you borrowed from our TSSM library will end in "  {daysLeft} days  ". As per our library policy, the validity period for borrowed books is 15 days.\n\n          You have the option to renew the book for another 15 days if you still need it. To renew, please visit the library's circulation desk or contact our library staff at [Library Contact Information] before the current validity expires.\n\n          If you no longer need the book, we kindly request that you return it to the TSSM Library at your earliest convenience so that other students may have the opportunity to utilize it for their studies.\n\n          Thank you for your cooperation in maintaining our TSSM library's resources for all students.\n\n              Warm regards,\n              Your TSSM Library Team.
                """
                  
                await client.send_message(entity,message)
                

                # Disconnect from Telegram
                await client.disconnect()
                # print(data.__len__())
                # print(self.i)
                
            except :
                pass
        # Run the send_telegram_message function
        with client:
            client.loop.run_until_complete(send_telegram_message(mobileNumber))






        # body of the program
nR = NewRecord(cursor)
nSR = StudentData(cursor)
nSR.daysLeft()
# nSR.borrowList()


# Creating the """"""""frame"""""""" for NAME && (DATE , TIME)
nameFrame = tk.Frame(root, bg = "green" ,width = 1350 , height = 80 , highlightbackground = "black" , highlightthickness = 5 )
nameFrame.place(x = 0 , y = 0)
# name
name = tk.Label(nameFrame , text = "LIBRARY MANAGEMENT SYSTEM" , font = ("Arial",30,"bold") , fg = "gold" , bg = "green" )
name.place(x = 400 , y = 10)

# Call to the dateTime function
dateTime() 

# Creating """""""""frame""""""""" for adding new record 

recordFrame = tk.Frame(root , width = 400 , height = 400 , bg = "skyblue" ,highlightbackground = "black" , highlightthickness = 3)
recordFrame.place(x = 0 , y = 80)

# Label for ==>

# Book Name
# Label
bookName = tk.Label(recordFrame , text = "Book Name" , font = ("Ariel",18,"bold") , fg = "black" , bg = "skyblue")
bookName.grid(row = 0 , column = 0 , padx = 10 , pady = (3 , 0))
# Entry
bookNameEntry = tk.Entry(recordFrame , width = 30 , font = ("Ariel",15) , bd = 2 )
bookNameEntry.grid(row = 1 , column = 0  , padx = 50 , pady =  (0,7) )
# Auther name
# Label
autherName = tk.Label(recordFrame , text = "Auther Name" , font = ("Ariel",18,"bold") , fg = "black" , bg = "skyblue")
autherName.grid(row = 2 , column = 0 , padx = 10 , pady = (3 , 0))
# Entry
autherNameEntry = tk.Entry(recordFrame , width = 30 , font = ("Ariel",15) , bd = 2 )
autherNameEntry.grid(row = 3 , column = 0  , padx = 50 , pady =  (0,7) )

#Search button using the auther and book name
searchButton = tk.Button(recordFrame , text = "Search" , font = ("Ariel",13,"bold") , fg = "white" , bg = "black" , width = 13 , command = nR.searchData)
searchButton.grid(row = 4 , column = 0 , padx = 50 , pady =  (0,7))


# Student Name
# Label
studentName = tk.Label(recordFrame , text = "Student Name" , font = ("Ariel",18,"bold") , fg = "black" , bg = "skyblue")
studentName.grid(row = 5 , column = 0 , padx = 10 , pady = (3 , 0))
# Entry
studentNameEntry = tk.Entry(recordFrame , width = 30 , font = ("Ariel",15) , bd = 2 )
studentNameEntry.grid(row = 6 , column = 0  , padx = 50 , pady =  (0,7))
# Student Branch
# Label
studentBranch = tk.Label(recordFrame , text = "Branch" , font = ("Ariel",18,"bold") , fg = "black" , bg = "skyblue")
studentBranch.grid(row = 7 , column = 0 , padx = 10 , pady = (3 , 0))
# Entry
studentBranchEntry = tk.Entry(recordFrame , width = 30 , font = ("Ariel",15) , bd = 2 )
studentBranchEntry.grid(row = 8 , column = 0  , padx = 50 , pady =  (0,7))

# Student Year of sudying
# Label 
studentYear = tk.Label(recordFrame , text = "Year" , font = ("Ariel",18,"bold") , fg = "black" , bg = "skyblue" )
studentYear.grid(row = 9 , column = 0 ,padx = 10 , pady = (3 , 0))
# Entry
studentYearEntry = tk.Entry(recordFrame , width = 30 , font = ("Ariel",15,), bg = "white" , bd = 2 )
studentYearEntry.grid(row = 10 , column = 0 ,padx = 50 , pady = (0,7)  )

# Student ID
# Label 
studentId = tk.Label(recordFrame , text = "ID" , font = ("Ariel",18,"bold") , fg = "black" , bg = "skyblue" )
studentId.grid(row = 11 , column = 0 ,padx = 10 , pady = (3 , 0))
# Entry
studentIdEntry = tk.Entry(recordFrame , width = 30 , font = ("Ariel",15,), bg = "white" , bd = 2 )
studentIdEntry.grid(row = 12 , column = 0 ,padx = 50 , pady = (0,7)  )


# Student mobile Number
# Label 
studentNumber = tk.Label(recordFrame , text = "Mobile Number" , font = ("Ariel",17,"bold") , fg = "black" , bg = "skyblue" )
studentNumber.grid(row = 13 , column = 0 ,padx = 10 , pady = (3 , 0))
# Entry
studentNumberEntry = tk.Entry(recordFrame , width = 30 , font = ("Ariel",15,), bg = "white" , bd = 2 )
studentNumberEntry.grid(row = 14 , column = 0 ,padx = 50 , pady = (0,7)  )



# Add to record button
addRecordButton = tk.Button(recordFrame , font = ("Ariel",14,"bold") , text = "Add to Record" , width = 13 , height = 1 , bg = "black" , fg = "white" , command = nSR.getStudentData)
addRecordButton.grid(row = 15 , column = 0 , padx = 10 ,  pady = (0,17.8)  )


# Creating """""""""frame""""""""" for adding  or deledeting book record from database and searchong field and delenting he record

updateDbFrame = tk.Frame(root , width = 905.5 , height = 70 , bg = "skyblue" , highlightthickness= 4 ,highlightbackground = "black" )
updateDbFrame.place(x = 444 , y = 80)








def on_entry_click(event):
    if searchEntryForDeleteRecord.get() == 'Enter student ID to delete':
        searchEntryForDeleteRecord.delete(0, "end") # Deletes default text in entry
        searchEntryForDeleteRecord.config(fg='black') 
        #  Change text color to black

def on_focus_out(event):
    if searchEntryForDeleteRecord.get() == '':
        searchEntryForDeleteRecord.insert(0, 'Enter student ID to delete')
        searchEntryForDeleteRecord.config(fg='grey') # Change text color to grey

# Entry field for search 
searchEntryForDeleteRecord = tk.Entry(updateDbFrame , fg='grey', font = ("Ariel" , 14) , bd = 3 )

searchEntryForDeleteRecord.insert(0, 'Enter student ID to delete')
searchEntryForDeleteRecord.bind('<FocusIn>', on_entry_click)
searchEntryForDeleteRecord.bind('<FocusOut>', on_focus_out)

searchEntryForDeleteRecord.place(x =10 , y = 17)




#Delete the selected record from the borrow list of student
deleteRecord = tk.Button(updateDbFrame , text = "Delete Record" , font = ("Serif" , 14 , "bold" ) , bg = "black" , fg = "white" , command = nSR.deleteStudentRecord)
deleteRecord.place(x =250 , y = 11)


sendMessage = tk.Button(updateDbFrame , text = "Send Message" , font = ("Serif" , 14 , "bold" ) , bg = "black" , fg = "white" , command = nSR.functionCallerForMessage)
sendMessage.place(x =410 , y = 11)


# Adding Buttons
# ADD new bookbutton
addButton = tk.Button(updateDbFrame , text = "Add New Book " , font = ("Serif" , 14 , "bold" ) , bg = "black" , fg = "white" , command =  nR.addNewBook)
addButton.place(x = 580 , y = 11)

# delete book from database
deleteButton = tk.Button(updateDbFrame , text = "Delete Book" , font = ("Serif" , 14 , "bold" ) , bg = "black" , fg = "white" , command = nR.deleteBook)
deleteButton.place(x = 755 , y = 10)


# creatingframe for adding borrow list


def on_configure(event):
    # Update the scrollable region to encompass the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))



# Create a canvas widget with a scrollbar
canvas = tk.Canvas(root, bg="lightgreen", width=870, height=520)
canvas.place(x=448, y=150)

scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar_x.place(x=448, y=670, width=870)
scrollbar_y = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar_y.place(x=1330, y=150, height=540)

canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

# Create a frame inside the canvas to hold your content
borrowListFrame = tk.Frame(canvas, bg="lightgreen", width=870, height=520)
canvas.create_window((0, 0), window=borrowListFrame, anchor="nw")

# Add some content to the inner frame

# creating the colunmm for the boro list

# column forr book name
column = ["Book Name" , "Auther Name" , "Student Name" , "Branch"  , "Year", "Student ID" , "Return Date" , "daysLeft" , "Mobile Number"]

for i in range(column.__len__()):
    bookNameColumn = tk.Label(borrowListFrame , text = f"{column[i]}" , bg = "chartreuse" , fg = "black" , font = ("Arial" , 16 , "bold" ))
    bookNameColumn.grid(row = 0 , column = i , padx = 5 , pady = 10)
# lightgreen


nSR.borrowList()





# for i in range(50):
#     tk.Label(borrowListFrame, text=f"Label {i}").grid(row=0, column=i, pady=5)

# Bind the configure event to update the scrollable region
borrowListFrame.bind("<Configure>", on_configure)









connection.commit()

root.mainloop()
connection.commit()
cursor.close()
# print("cursor close")
connection.close()
# print("connection close")
