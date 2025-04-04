#USER INFO STORAGE
#Author: Nick Lei

#Import
from datetime import datetime
import copy

#Import UI
from tkinter import *

#Create person
class Person:

    def __init__(self, index, name, phoneNum):
        self.index = int(index)
        self.name = str(name)
        self.phoneNum = int(phoneNum)
    
    def __str__(self):
        temp = f'{self.index}|Name: {self.name} | Phone: {self.phoneNum}'
        return temp
    
    def updateName(self, newName):
        self.name = newName

    def updatePhoneNum(self, newPhoneNum):
        self.phoneNum = newPhoneNum

#Create main window
def createGUI():

    global root, buttonSave, buttonHistory, userHistoryListBox
    global userSearch, userListBox, userNameLabel
    global historySearch, historyListBox, historyLabel

    global editUserNameLable, editUserPhoneLable, editUserMoneyLable
    global userNameEdit, userPhoneEdit, userMoneyEdit

    root = Tk()
    root.geometry('1400x720')
    root.title('Program')

    #Labels
    Label(
        root,
        text="User Information",
        background="white",
        foreground="dark green",
        width=30,
        font=("Arial", 12),
        relief="raised"
        ).grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    #display chosen user information
    userNameLabel = Label(
                        root,
                        background="white",
                        width=30,
                        font=("Arial", 12),
                        relief="raised"
                        )
    userNameLabel.grid(row=0, column=3, columnspan=2, padx=5)

    #display chosen date information
    historyLabel = Label(
                        root,
                        background="white",
                        width=30,
                        font=("Arial", 12),
                        relief="raised"
                        )
    historyLabel.grid(row=0, column=6, columnspan=2, padx=5)

    #Searches
    userSearch = Entry(
                        root,
                        bg="light steel blue",
                        width=30,
                        font=("Arial", 12),
                        )
    userSearch.grid(row=1, column=0, columnspan=2, padx=5)

    userNameEdit = Entry(
                        root,
                        bg="light steel blue",
                        width=30,
                        font=("Arial", 12),
                        )
    userNameEdit.grid(row=2, column=3, columnspan=2, padx=5)
    userPhoneEdit = Entry(
                        root,
                        bg="light steel blue",
                        width=30,
                        font=("Arial", 12),
                        )
    userPhoneEdit.grid(row=3, column=3, columnspan=2, padx=5)
    userMoneyEdit = Entry(
                        root,
                        bg="light steel blue",
                        width=30,
                        font=("Arial", 12),
                        )
    userMoneyEdit.grid(row=4, column=3, columnspan=2, padx=5)

    historySearch = Entry(
                        root,
                        bg="light steel blue",
                        width=30,
                        font=("Arial", 12),
                        )
    historySearch.grid(row=1, column=6, columnspan=2, padx=5)

    #Buttons
    #user search bar button
    Button(
        text="Search",
        bg="light grey",
        activebackground="yellow",
        font=("Arial", 12),
        width=6,
        cursor="target",
        command=searchUserCommand
        ).grid(row=1, column=2)
    
    #change money money
    Button(
        text="Edit\nName",
        bg="light grey",
        activebackground="yellow",
        font=("Arial", 12),
        width=6,
        height=2,
        cursor="target",
        command=changeUserNameCommand
        ).grid(row=2, column=5)
    Button(
        text="Edit\nPhone",
        bg="light grey",
        activebackground="yellow",
        font=("Arial", 12),
        width=6,
        height=2,
        cursor="target",
        command=changeUserPhoneCommand
        ).grid(row=3, column=5)
    Button(
        text="Empty",
        bg="light grey",
        activebackground="yellow",
        font=("Arial", 12),
        width=6,
        cursor="target"
        ).grid(row=4, column=5)
    
    #history search bar button
    Button(
        text="Search",
        bg="light grey",
        activebackground="yellow",
        font=("Arial", 12),
        width=6,
        cursor="target",
        command=searchHistoryCommand
        ).grid(row=1, column=8)
    #check user button
    Button(
        text="Check This User",
        bg="light grey",
        activebackground="yellow",
        font=("Arial", 12),
        padx=80,
        pady=10,
        cursor="target",
        command=buttonListBoxSearchCommand
        ).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    #check date button
    Button(
        text="Check This Date",
        bg="light grey",
        activebackground="yellow",
        font=("Arial", 12),
        padx=80,
        pady=10,
        cursor="target",
        command=buttonListBoxHistorySearchCommand
        ).grid(row=5, column=6, columnspan=2, padx=5, pady=5)
    #save button
    buttonSave = Button(
        text="SAVE", 
        bg="green", 
        fg="white",
        border=3,
        font=("Arial", 16),
        padx=20,
        pady=10, 
        cursor="target",
        state="disabled",
        command=buttonSaveCommand
        )
    buttonSave.grid(row=5, column=9, padx=5, pady=5)
    #exit button
    Button(
        text="EXIT", 
        bg="red",
        fg="white",
        border=3,
        font=("Arial", 16),
        padx=20,
        pady=10, 
        cursor="target",
        command=buttonExitCommand
        ).grid(row=5, column=10, padx=5, pady=5)
    #button to create new user
    Button(
        text="Add New User",
        bg="blue",
        fg="white",
        border=3,
        font=("Arial", 12),
        padx=50,
        pady=15,
        cursor="target",
        command=newUserGUI
        ).grid(row=0, column=9, columnspan=2, padx=5)
    Button(
        text="RESET ENTRIES",
        bg="blue",
        fg="white",
        border=3,
        font=("Arial", 12),
        padx=50,
        pady=15,
        cursor="target",
        command=buttonClearCommand
        ).grid(row=6, column=3, columnspan=2, padx=5)
    
    #ListBoxes/scrollbars
    #User list
    userListBox = Listbox(
                        root, 
                        width=30, 
                        height=25,
                        font=("Arial", 12)
                        )
    userListBox.grid(row=2, column=0, rowspan=3, columnspan=2)
    userListBoxScroll = Scrollbar(root,
                              cursor="target",
                              )
    userListBoxScroll.grid(row=2, column=2, rowspan=2, sticky="ns")
    userListBox.config(yscrollcommand=userListBoxScroll.set)
    userListBoxScroll.config(command=userListBox.yview)
    #history list
    historyListBox = Listbox(
                            root, 
                            width=30, 
                            height=25,
                            font=("Arial", 12)
                            )
    historyListBox.grid(row=2, column=6, rowspan=3, columnspan=2)
    historyListBoxScroll = Scrollbar(root,
                              cursor="target",
                              )
    historyListBoxScroll.grid(row=2, column=8, rowspan=2, sticky="ns")
    historyListBox.config(yscrollcommand=historyListBoxScroll.set)
    historyListBoxScroll.config(command=historyListBox.yview)
    #user history list
    userHistoryListBox = Listbox(
                            root, 
                            width=35, 
                            height=25,
                            font=("Arial", 12)
                            )
    userHistoryListBox.grid(row=2, column=9, rowspan=3, columnspan=2)
    userHistoryListBoxScroll = Scrollbar(root,
                              cursor="target",
                              )
    userHistoryListBoxScroll.grid(row=2, column=11, rowspan=2, sticky="ns")
    userHistoryListBox.config(yscrollcommand=userHistoryListBoxScroll.set)
    userHistoryListBoxScroll.config(command=userHistoryListBox.yview)
 

    updateNewestUI(userListBox, userInfo)
    updateNewestUI(historyListBox, backupUserInfo)

    root.mainloop()

#GUI for creating a new user
def newUserGUI():

    newWindow = Tk()
    newWindow.title("Add New User")
    newWindow.geometry("800x600")

    Label(
        newWindow,
        text="Name: ",
        background="light grey",
        width=10,
        font=("Arial", 12),
        relief="raised"
        ).grid(row=0, column=0, padx=5, pady=5)
    userNameAdd = Entry(
                        newWindow,
                        background="light steel blue",
                        font=("Arial", 12)
                        )
    userNameAdd.grid(row=0, column=1, padx=5, pady=5)

    Label(newWindow, 
        text="Phone:",
        background="light grey",
        width=10,
        font=("Arial", 12),
        relief="raised"
        ).grid(row=1, column=0, padx=5, pady=5)
    userPhoneNumAdd = Entry(
                        newWindow,
                        background="light steel blue",
                        font=("Arial", 12)
                        )
    userPhoneNumAdd.grid(row=1, column=1, padx=5, pady=5)

    Button(newWindow,
           text="添加",
           bg="light grey",
           activebackground="green",
           activeforeground="white",
           font=("Arial", 12),
           cursor="target",
           command=lambda: addUser(createUser(userNameAdd.get(), userPhoneNumAdd.get(), userInfo), newWindow)
           ).grid(row=2, column=0, columnspan=2, padx=5, pady=5)


    newWindow.mainloop()


#Function to get date
def getDate():
    return (datetime.now().strftime("[Date: (%Y %m %d) | Time: (%H:%M:%S)]"))

#Function to read file and store data
def readFile(name):
    fileInput = open(name, "r", encoding="utf-8")
    userList = []

    #Store Data
    for line in fileInput:
        temp = line.replace("\n", "").split("|")
        p = Person(temp[0], temp[1], temp[2])
        userList.append(p)

    fileInput.close()

    return userList

def readHistoryFile(name):
    fileInput = open(name, "r", encoding="utf-8")
    historyList = []

    #Store Data
    temp = fileInput.read().replace("\n", "").split("[")

    for index in range(len(temp)-1):
        date = temp[index+1].split("]")
        historyList.append(date[0])

    fileInput.close()

    return historyList

#Function to update file
def updateFile(outputFileName, backupFileName, userList):
    fileOutput = open(outputFileName, "w", encoding="utf-8")
    fileBackup = open(backupFileName, "a", encoding="utf-8")

    #Write Data
    index = 0
    for p in userList:
        fileOutput.write(f'{index}|{p.name}|{p.phoneNum}\n')
        index+=1

    #Write Data in Backup 
    date = getDate()
    fileBackup.write(f'{date}\n\n')
    for k in userList:
        fileBackup.write(f'{k}\n')
    fileBackup.write('-----END OF INFO-----\n\n')

    fileOutput.close()
    fileBackup.close()

def createUser(name, phoneNum, userList):
    return Person((len(userList)), name, phoneNum)

def addUser(user, window):
    window.destroy()
    tempUserInfo.append(user)
    updateNewestUI(userListBox, tempUserInfo)

    buttonSave.config(state="normal")

#def removeUser(index, userList):
#    userInfo.pop(int(index))

def updateNewestUI(listBox, userList):
    listBox.delete(0, END)
    for p in userList:
        listBox.insert(0, str(p))

def updateOldestUI(listBox, userList):
    listBox.delete(0, END)
    for p in userList:
        listBox.insert(END, str(p))

def getUserFileData(index):
    userFilePath = f"User Files\{index}.txt"
    fileOfUser = open(userFilePath, "r", encoding="utf-8")

    temp = fileOfUser.read().split("\n")
    updateOldestUI(userHistoryListBox, temp)

    fileOfUser.close()

def getHistoryFileData(date, fileName):
    historyFile = open(fileName, "r", encoding="utf-8")
    temp = historyFile.read().split('-----END OF INFO-----\n\n')
   
    for d in temp:
        if date in d:
            day = d.replace(f"[{date}]\n\n", "").split("\n")
            updateOldestUI(userHistoryListBox, day)

    historyFile.close()

#commands
def searchUserCommand():
    temp = []
    for p in userInfo:
        if (userSearch.get() in p.name)or(userSearch.get() in str(p.phoneNum)):
            temp.append(p)
    updateNewestUI(userListBox, temp)

def changeUserNameCommand():
    userName = currentSelectedPerson.split("|")[1].split(":")[1].strip()
    phoneNum = currentSelectedPerson.split("|")[2].split(":")[1].strip()

    k = -1
    for info in tempUserInfo:
        k+=1
        if(userName in info.name and phoneNum in str(info.phoneNum)):
            info.name = userNameEdit.get()
    userNameLabel.config(text=tempUserInfo[k])
    updateNewestUI(userListBox, tempUserInfo)

    buttonSave.config(state="normal")

def changeUserPhoneCommand():
    userName = currentSelectedPerson.split("|")[1].split(":")[1].strip()
    phoneNum = currentSelectedPerson.split("|")[2].split(":")[1].strip()

    k = -1
    for info in tempUserInfo:
        k+=1
        if(userName in info.name and phoneNum in str(info.phoneNum)):
            info.phoneNum = userPhoneEdit.get()
    userNameLabel.config(text=tempUserInfo[k])
    updateNewestUI(userListBox, tempUserInfo)

    buttonSave.config(state="normal")

def searchHistoryCommand():
    temp = []
    
    for d in backupUserInfo:
        date = d.split("|")
        if historySearch.get() in date[0]:
            temp.append(d)

    updateNewestUI(historyListBox, temp)

def buttonListBoxSearchCommand():
    userNameChose = userListBox.curselection()
    global currentSelectedPerson
    currentSelectedPerson = userListBox.get(userNameChose[0])
    if userNameChose:
        userName = userListBox.get(userNameChose)
        userNameLabel.config(text=userName)

    getUserFileData(int(userName.split("|")[0]))

def buttonListBoxHistorySearchCommand():
    dateChose = historyListBox.curselection()
    if dateChose:
        date = historyListBox.get(dateChose)
        historyLabel.config(text=date)

    getHistoryFileData(date, "backupData.txt")

def buttonClearCommand():
    userNameLabel.config(text="")
    historyLabel.config(text="")

    userNameEdit.delete(0,END)
    userPhoneEdit.delete(0,END)
    userMoneyEdit.delete(0,END)
    userSearch.delete(0,END)
    historySearch.delete(0,END)

    updateOldestUI(userHistoryListBox, "")
    updateNewestUI(userListBox, userInfo)
    backupUserInfo = readHistoryFile(backupFileName)
    updateNewestUI(historyListBox, backupUserInfo)

def buttonSaveCommand():
    global userInfo
    global tempUserInfo
    if len(tempUserInfo) > len(userInfo):
        for k in range(len(userInfo), len(tempUserInfo)):
            userFilePath = f"User Files\{k}.txt"
            fileOfUser = open(userFilePath, "a", encoding="utf-8")

            date = getDate()
            user = tempUserInfo[k]
            fileOfUser.write(f'{date}\n\n')
            fileOfUser.write(f'{user}\n')
            fileOfUser.write('-----END OF INFO-----\n\n')

            fileOfUser.close()

    for p in userInfo:
        if(p.name != tempUserInfo[p.index].name or p.phoneNum != tempUserInfo[p.index].phoneNum):
            userFilePath = f"User Files\{p.index}.txt"
            fileOfUser = open(userFilePath, "a", encoding="utf-8")

            date = getDate()
            user = tempUserInfo[p.index]
            fileOfUser.write(f'{date}\n\n')
            fileOfUser.write(f'{user}\n')
            fileOfUser.write('-----END OF INFO-----\n\n')
    
            fileOfUser.close()

    userInfo = copy.deepcopy(tempUserInfo)
    updateFile(fileName, backupFileName, userInfo)

    backupUserInfo = readHistoryFile(backupFileName)
    updateNewestUI(userListBox, userInfo)
    updateNewestUI(historyListBox, backupUserInfo)

    buttonSave.config(state="disabled")

def buttonExitCommand():
    root.destroy()

# ***MAIN BODY OF PROGRAM

#Open and read file
fileName = "data.txt"
backupFileName = "backupData.txt"
userInfo = readFile(fileName)
backupUserInfo = readHistoryFile(backupFileName)
tempUserInfo = copy.deepcopy(userInfo)


createGUI()
    

