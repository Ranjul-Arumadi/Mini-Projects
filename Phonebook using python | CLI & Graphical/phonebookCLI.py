#Ranjuls Phonebook App
phonebook={}
inpt = 0




def addNumber():
    stop=1
    while (stop!=0):
        try:
            name=input('Enter name: ')
        except:
            print('\nEnter name')
            addNumber()
        if name in phonebook:
            print(f'\nName {name} already associated with {phonebook[name]}')
        else:   
            try:
                number=int(input('Enter number: '))
                phonebook[name]=number
            except ValueError:
                print('\nEnter number only!')
                number=int(input('Enter number: '))
                phonebook[name]=number
        stop=int(input('\nEnter 1 - continue 0 - stop :'))
    
    
    
def deleteNumber():
    name=input('\nEnter name: ')
    if name in phonebook:
        phonebook.pop(name)


def displayNumber():
    if (not phonebook):
        print('\nPhoneBook is empty !')
    else:
        print('Name | Number')
        print('-------------')
        for key, value in phonebook.items():
            print(key, ' - ', value)


while inpt!= -1 :  
    inpt = int(input('\n\n Phonebook \n\n 1 - Add number \n 2 - Delete Number \n 3 - View Numbers \n 4 - Exit\n'))
    if inpt==1:
        addNumber()
    elif inpt == 2:
        deleteNumber()
    elif inpt == 3:
        displayNumber()
    elif inpt == 4:
        input = -1
    else :
        print('Invalid input')
    
        
    
