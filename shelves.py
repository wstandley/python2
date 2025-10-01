"""
    This is for Assignment OOP 4.3 Serialization using Shelve
"""

import shelve

def main():

    actions = True
    while actions == True: # Initialize Action Loop

        # Display Available Actions
        print("\nActions:")
        print("1.) Add new User")
        print("2.) Search for Existing User")
        print("3.) Change Existing User")
        print("4.) Delete Existing User")
        print("5.) Exit")

        user_action = int(input("Choose your action: ")) # User chooses Action
    
        if user_action == 1:
            # Add new User
            print("")
            add_first_name = input("Enter First Name: ")
            add_last_name = input("Enter Last Name: ")
            add_phone_number = input("Enter Phone Number: ")
            add_email_address = input("Enter Email Address: ")

            add_contact = add_first_name + add_last_name

            with shelve.open('address_book') as address_book:
                address_book[add_contact] = {
                    'first_name': add_first_name,
                    'last_name': add_last_name,
                    'phone_number': add_phone_number,
                    'email_address': add_email_address
                }
            
            print(f"{add_first_name} {add_last_name} has been added to your contacts.")
            

        elif user_action == 2:
            # Search Existing User
            print("")
            search_first_name = input("Enter First Name you'd like to search: ")
            search_last_name = input("Enter Last Name you'd like to search: ")

            search_name = search_first_name + search_last_name 

            with shelve.open('address_book') as address_book:
                if search_name in address_book:
                    contact = address_book[search_name]
                    print(f"First Name: {contact['first_name']}\nLast Name: {contact['last_name']}\nPhone Number: {contact['phone_number']}\nEmail: {contact['email_address']}")
                else:
                    print("Contact not found.")
            

        elif user_action == 3:
            # Update Existing Contact
            search_first_name = input("Enter First Name you'd like to update: ")
            search_last_name = input("Enter Last Name you'd like to update: ")

            search_name = search_first_name + search_last_name

            with shelve.open('address_book') as address_book:
                if search_name in address_book:
                    contact = address_book[search_name]

                    update_actions = True
                    while update_actions == True:
        
                        print("What would you like to update on this contact?\n")
                        print("1.) First Name")
                        print("2.) Last Name")
                        print("3.) Phone Number")
                        print("4.) Email")
                        print("5.) Exit Updates")

                        update_user_action = int(input("Select a numbered action: "))

                        if update_user_action == 1:
                            # Update First Name
                            new_first_name = input("What would you like to update the First Name to? ")

                            contact['first_name'] = new_first_name
                            address_book[new_first_name + contact["last_name"]] = contact # change first name without changing last name
                            del address_book[search_name] # deletes the old first name
                            search_name = new_first_name + contact["last_name"]

                            print("First Name has been updated.")

                        elif update_user_action == 2:
                            # Update Last Name
                            new_last_name = input("What would you like to update the Last Name to? ")

                            address_book[contact["first_name"] + new_last_name] = contact # change last name without changing first name
                            del address_book[search_name] # deletes the old last name
                            search_name = contact["first_name"] + new_last_name

                            print("Last Name has been updated.")

                        elif update_user_action == 3:
                            # Update Phone Number
                            new_phone_number = input("What would you like to update the Phone Number to? ")
                            contact['phone_number'] = new_phone_number
                            address_book[search_name] = contact # Saves the new phone number
                            print("Phone Number has been updated.")

                        elif update_user_action == 4:
                            # Update Email
                            new_email_address = input("What would you like to update the Email Address to? ")
                            contact['email_address'] = new_email_address
                            address_book[search_name] = contact # Saves the new email address
                            print("Email Address has been updated.")

                        elif update_user_action == 5:
                            # Exit Update
                            update_actions = False
                        else:
                            print("Action not found, try another.")
                        
                else:
                    print("Contact not found.")

        elif user_action == 4:
            # Delete Existing User
            delete_first_name = input("Enter First Name you'd like to delete: ")
            delete_last_name = input("Enter Last Name you'd like to delete: ")

            search_name = delete_first_name + delete_last_name

            with shelve.open('address_book') as address_book:
                if search_name in address_book:
                    del address_book[search_name]
                else:
                    print("Name not found.")
            print(f"{delete_first_name} {delete_last_name} has been removed.")

        elif user_action == 5:
            # Exit Loop
            actions = False 
            
        else:
            # In case they don't enter an action s
            print("That's not an action entry, try again.")

main()