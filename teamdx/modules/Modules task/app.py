import meetings
import customer
def menu():
    print("1.Meeting \n 2. Customer \n 3.Quit \n")
    choice = input("Select an option: ")
    if choice == '1':
        print('\nWelcome to meeting page')
        print("\n a. create meeting \n b. update meeting \n c. delete meeting \n d. get the meeting")
        choice = input("Select an option:  ")
        if choice == 'a':
                meetings.create_meeting()
        elif choice == 'b':
                meetings.update_meeting()
        elif choice == 'c':
                meetings.delete_meeting()
        elif choice == 'd':
                meetings.get_meeting()
        else:
                print("Invalid choice.")
    if choice == '2':
        print('\n Welcome to customer page')
        print("\na. create customer \n b. update customer \n c. delete customer\n d. get the customer")
        choice = input("Select an option:  ")
        if choice == 'a':
                customer.create_customer()
        elif choice == 'b':
                customer.update_customer()
        elif choice == 'c':
                customer.delete_customer()
        elif choice == 'd':
                customer.get_customer()
        else:
                print("Invalid choice.")
    if choice == '3':
        print('\n Quit')

menu()