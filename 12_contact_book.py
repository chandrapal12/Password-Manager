namesList=[]
phoneNumbersList=[]
num=1

print(
'''
1. Save the contacts
2. List of saved contacts 
3. Search the contacts 
4. Delete the contacts
5. Deletes all the contacts
6. Exit
'''
)

while True:
    option = int(input("\nEnter your option: "))
    if option == 1:
        for i in range(num):
            phoneNumber=input("\nPhone number:  ")
            name=input("Name:  ")
            phoneNumbersList.append(phoneNumber)
            namesList.append(name)

    elif option == 2:
        try:
            print("\nPhone number\t\t\tName\n") 
            for i in range(num):
                print(f"{namesList[i]}\t\t\t{phoneNumbersList[i]}")
        except:
            print("")

    elif option == 3:
        findContacts=input("\nEnter name to search phone number: ")
        if findContacts in namesList:
            nameIndex=namesList.index(findContacts)
            phoneNumberIndex=phoneNumbersList[nameIndex]
            print(f"\nPhone number: {phoneNumberIndex}")
        else:
            print("\nNot found in the contact list")
    
    elif option == 4:
        deleteContacts=input("\nEnter name to delete form the contacts list: ")
        if deleteContacts in namesList:
            namesList.remove(deleteContacts)
            print(f"{deleteContacts} has been deleted from the contact list")
        else:
            print(f"{deleteContacts} is not found in the contact list")

    elif option == 5:
        print(f"{len(namesList)} contact(s) deleted from the contact list")
        namesList.clear()
        phoneNumbersList.clear()
        

    elif option == 6:
        exit() 
