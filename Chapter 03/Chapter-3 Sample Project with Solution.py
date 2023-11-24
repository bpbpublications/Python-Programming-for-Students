# Sample project with solution
# Create a personal telephone directory storing details such as names, numbers, alternate number, e-mail id, and so on. The contacts book enables searching through names or contact numbers. It also allows users to enter new contacts, delete a specific contact, or clear the directory completely:
# This project uses user-defined functions for implementation.
# Readers can refer Chapter-4 to learn Function Handling mechanism.

import sys  # importing the module sys for using exit() function
def initiate_contactlist():
    contacts = int(input("Please enter the number of contacts: "))
    details = 5
    contact_book = []
    for i in range(contacts):
        print("\nEnter details for contact %d :" % (i + 1))
        print("Details marked(*) are mandatory!!")
        print("....................................................................")
        temp_list = []
        for j in range(details):
            if j == 0:
                temp_list.append(str(input("Enter Contact Name* : ")))
                if temp_list[j] == '' or temp_list[j] == ' ':
                    sys.exit("Cannot leave Contact Name blank!!")
            if j == 1:
                temp_list.append(int(input("Enter contact number* : ")))
            if j == 2:
                temp_list.append(input("Add alternate contact number: "))
                if temp_list[j] == '' or temp_list[j] == ' ':
                    temp_list[j] = None
            if j == 3:
                temp_list.append(str(input("Enter e-mail address: ")))
                if temp_list[j] == '' or temp_list[j] == ' ':
                    temp_list[j] = None
            if j == 4:
                temp_list.append(str(input("Enter category(Home/Family/Friends/Work/Others): ")))
                if temp_list[j] == "" or temp_list[j] == ' ':
                    temp_list[j] = None
        contact_book.append(temp_list)
    print(contact_book)
    return contact_book

def menu_options():
    print("_______________________________________________")
    print("\t\t\tPHONE CONTACTS DIRECTORY")
    print("_______________________________________________")
    print("\tPress desired option of Contacts Book\n")
    print("1. Press 1 to Add new Contact")
    print("2. Press 2 to Remove a Contact")
    print("3. Press 3 to Clear Contacts Book")
    print("4. Press 4 to search a Contact")
    print("5. Press 5 to View Contacts")
    print("6. Exit Contacts Book")
    choice = int(input("Please enter your choice: "))
    return choice

def add_new_contact(obj):
    cont_list = []
    for i in range(len(obj[0])):
        if i == 0:
            cont_list.append(str(input("Enter contact name: ")))
        if i == 1:
            cont_list.append(int(input("Enter contact number: ")))
        if i == 2:
            cont_list.append(input("Enter alternate contact number: "))
        if i == 3:
            cont_list.append(str(input("Enter e-mail address: ")))
        if i == 4:
            cont_list.append(
                str(input("Enter category(Home/Family/Friends/Work/others): ")))
    if not obj:  # check if contact book object obj is empty
        obj = cont_list
    else:
        obj.append(cont_list)
    return obj

def delete_contacts(obj):
    if not obj:
        print("Contacts Book is empty!!")
    else:
        cont_name = str(input("Enter that contact name to delete: "))
        temp = 0
        for i in range(len(obj)):
            if cont_name == obj[i][0]:
                temp += 1
                print(obj.pop(i))
                print("This contact is removed")
                return obj
        if temp == 0:
            print("Contact does not exist!!")
            return obj

def delete_all(obj):
    if not obj:  # check if contact book object obj is empty
        print("Contacts Book is empty!!")
    else:
        return obj.clear()

def search_contact(obj):
    if not obj:  # check if contact book object obj is empty
        print("Contacts Book is empty!!")
    else:
        choice = int(input("For searching contact press\n1. Name\n2. Number\n"))
        temp = []
        flag = -1 # flag represents search result
        if choice == 1:  # For search using Contact Name
            c_name = str(input("Please enter the name of the contact you wish to search: "))
            for i in range(len(obj)):
                if c_name == obj[i][0]:
                    flag = i
                    temp.append(obj[i])
        elif choice == 2: # For search using Contact Number
            c_number = int(input("Please enter the number of the contact you wish to search: "))
            for i in range(len(obj)):
                if c_number == obj[i][1]:
                    flag = i
                    temp.append(obj[i])
        else:
            print("Invalid search criteria")
            return -1
        if flag == -1:
            return -1
        else:
            display_contacts(temp)
            return flag

def display_contacts(obj):
    if not obj:
        print("Contacts Book is empty!!")
    else:
        for i in range(len(obj)):
            print(obj[i])

def exit_book():
    sys.exit()

# Main Code to start Contacts Book
print("***************************************************")
print("Welcome to Personal Contacts Book")
print("***************************************************")
option = 1
obj = initiate_contactlist()
while True:
    option = menu_options()
    if option == 1:
        if not obj: # check if contact book object is empty
            obj = initiate_contactlist()
        else:
            obj = add_new_contact(obj)
    elif option == 2:
        obj = delete_contacts(obj)
    elif option == 3:
        obj = delete_all(obj)
    elif option == 4:
        result = search_contact(obj)
        if result == -1:
            print("The contact does not exist!! Search again")
    elif option == 5:
        display_contacts(obj)
    elif option == 6:
        exit_book()
    else:
        print("Enter a valid choice!!")
