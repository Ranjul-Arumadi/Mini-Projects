'''
Name of application: PhoneBook [GUI version] using tkinter 
Language used: python
Modules used: tkinter
Author: Ranjul Arumadi
'''

from tkinter import *
from tkinter import messagebox

box = Tk()
box.geometry("300x80")
box.title('Phone Book')

menu = Menu(box)
box.config(menu=menu)
helpmenu = Menu(menu)
menu.add_cascade(label='About', menu=helpmenu)
helpmenu.add_command(label='About')

L1 = Label(box, text='Contact Name').grid(row=0)
L2 = Label(box, text='Phone Number').grid(row=1)

e1 = Entry(box)
e2 = Entry(box)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

phonebook={}


#This is to open a new window while pressing display button
def openNewWindow():
    if not bool(phonebook):
        messagebox.showerror("Empty phonebook", "Phonebook is empty!")
    else:    
        newWindow = Toplevel(box)
        newWindow.title("Saved Contacts")
        newWindow.geometry("200x100")
        Label(newWindow, text = phonebook).pack()
        for key, value in phonebook.items() :
            label = Label(box, text= key)
            label = Label(box, text= value)
    
        
    
#Reads values of user input
def readvalues():

    name = e1.get()
    number = e2.get()
    
    if len(name)==0 or len(number)==0:
        messagebox.showerror("Input missing", "Please input name and number")
    else:
        if name in phonebook:
            messagebox.showerror("showerror", f'\nName {name} already associated with {phonebook[name]}')
        else:
            phonebook[name]=number
            messagebox.showinfo("Added", "Contact added successfully!")
    


#deletes entries from phonebook
def deletevalues():
    if not bool(phonebook):
        messagebox.showerror("Empty phonebook", "Phonebook is empty!")
    else:
        name = e1.get()
        if name in phonebook:
            messagebox.showinfo("Deleted", "Contact deleted!")
            phonebook.pop(name)
        else:
            messagebox.showerror("Delete error", "Contact does not exist!")


  
button1 = Button(text='Add', width=10, command = readvalues).grid(row=2, column=0)
button2 = Button(text='Display', width=10,command = openNewWindow).grid(row=2, column=1)
button3 = Button(text='Delete', width=10, fg='red', command = deletevalues).grid(row=2, column=2)

box.mainloop()
