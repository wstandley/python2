"""
    This is for Assignment OOP 4.2 -Serialization using Pickle
"""

import pickle

address_book = [
    {
        "first_name": "Will",
        "last_name": "Standley",
        "phone_number": "815-575-5909",
        "email_address": "wstandley@students.mchenry.edu"
    }
]

def save_contact_info(address_book, filename = "address_book.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(address_book, file)
    print("Contact info saved.")


def main():
    #TODO Create the menu interface 
    """
        This will include:
            - Add New User
            - Search for Existing User
            - Change Existing User
            - Delete Existing User
            - Exit
    """
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
            add_first_name = input("Enter First Name: ")
            add_last_name = input("Enter Last Name: ")
            add_phone_number = input("Enter Phone Number: ")
            add_email_address = input("Enter Email Address: ")

            address_book.append({
                "first_name": add_first_name,
                "last_name": add_last_name,
                "phone_number": add_phone_number,
                "email_address": add_email_address
                })
            print(f"{add_first_name} {add_last_name} has been added to your contacts.")
            save_contact_info(address_book)

        elif user_action == 2:
            # Search Existing User
            search_first_name = input("Enter First Name you'd like to search: ")
            search_last_name = input("Enter Last Name you'd like to search: ")

            for contact in address_book:
                if search_first_name == contact['first_name'] and search_last_name == contact['last_name']:
                    print(f"First Name: {contact['first_name']}\nLast Name: {contact['last_name']}\nPhone Number: {contact['phone_number']}\nEmail: {contact['email_address']}")
                    break
            else:
                print("Contact not found.")

        elif user_action == 3:
            # Update Existing Contact
            update_first_name = input("Enter First Name you'd like to update: ")
            update_last_name = input("Enter Last Name you'd like to update: ")

            for contact in address_book:
                if update_first_name == contact['first_name'] and update_last_name == contact['last_name']:
                    print(f"First Name: {contact['first_name']}\nLast Name: {contact['last_name']}\nPhone Number: {contact['phone_number']}\nEmail: {contact['email_address']}")

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
                            contact["first_name"] = new_first_name
                            print("First Name has been updated.")
                            save_contact_info(address_book)

                        elif update_user_action == 2:
                            # Update Last Name
                            new_last_name = input("What would you like to update the Last Name to? ")
                            contact["last_name"] = new_last_name
                            print("Last Name has been updated.")
                            save_contact_info(address_book)

                        elif update_user_action == 3:
                            # Update Phone Number
                            new_phone_number = input("What would you like to update the Phone Number to? ")
                            contact["phone_number"] = new_phone_number
                            print("Phone Number has been updated.")
                            save_contact_info(address_book)

                        elif update_user_action == 4:
                            # Update Email
                            new_email_address = input("What would you like to update the Email Address to? ")
                            contact["email_address"] = new_email_address
                            print("Email Address has been updated.")
                            save_contact_info(address_book)

                        elif update_user_action == 5:
                            # Exit Update
                            save_contact_info(address_book)
                            update_actions = False
                        else:
                            print("Action not found, try another.")
                else:
                    print("Contact Not Found.")

        elif user_action == 4:
            # Delete Existing User
            delete_first_name = input("Enter First Name you'd like to delete: ")
            delete_last_name = input("Enter Last Name you'd like to delete: ")

            for contact in address_book:
                if delete_first_name == contact["first_name"] and delete_last_name == contact["last_name"]:
                    address_book.remove(contact)
                    print(f"{delete_first_name} {delete_last_name} has been removed.")
                    save_contact_info(address_book)
            else:
                print("Contact not found")
            
        elif user_action == 5:
            # Exit Loop
            actions = False 
            
        else:
            # In case they don't enter an action s
            print("That's not an action entry, try again.")

main()